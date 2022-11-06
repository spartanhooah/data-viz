import justpy as jp
import pandas
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_course = data.groupby(['Month', 'Course Name']).mean(numeric_only=True).unstack()
# print(month_average_course)

chart_def = """
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average rating by course and by month'
    },
    subtitle: {
        align: 'center',
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        title: ''
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.0
        }
    },
    series: []
}"""

def app():
    page = jp.QuasarPage()

    h1 = jp.QDiv(a=page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=page, text="These graphs represent course review analysis")

    chart = jp.HighCharts(a=page, options=chart_def)
    chart.options.xAxis.categories = list(month_average_course.index)

    chart_data = [{"name": v1[1], "data": [v2 for v2 in month_average_course[v1]]} for v1 in month_average_course.columns]

    chart.options.series = chart_data

    return page

jp.justpy(app)