import justpy as jp
import pandas
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Day Number'] = data['Timestamp'].dt.strftime('%w')
weekday_average = data.groupby(['Weekday', 'Day Number']).mean(numeric_only=True)
weekday_average = weekday_average.sort_values('Day Number')

chart_def = """
{
    chart: {
        type: 'line'
    },
    title: {
        text: 'Average rating by day of week'
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
        },
        min: 4,
        max: 5
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
    chart.options.xAxis.categories = list(weekday_average.index)

    chart_data = [{"name": v1, "data": [v2 for v2 in weekday_average[v1]]} for v1 in weekday_average.columns]

    chart.options.series = chart_data
    # print(chart_data)

    return page

jp.justpy(app)