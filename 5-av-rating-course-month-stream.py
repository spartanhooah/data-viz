import justpy as jp
import pandas
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_course = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack()

chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    title: {
        floating: true,
        align: 'left',
        text: Average Rating by Month by Course
    },
    
    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            },
            accessibility: {
                exposeAsGroupOnly: true
            }
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

    chart_data = [{"name": v1, "data": [v2 for v2 in month_average_course[v1]]} for v1 in month_average_course.columns]

    chart.options.series = chart_data

    return page

jp.justpy(app)