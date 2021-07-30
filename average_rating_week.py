import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv(r"C:\Users\kirst\pythonProject1\pythonProject1\pythonProject\data_analysis\review_analysis\reviews.csv", parse_dates=["Timestamp"])
data["Week"] = data["Timestamp"].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

chart_definition = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Week'
    },
    subtitle: {
        text: 'According to the Course Reviews Data Set'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}

'''

def app():
    webpage = jp.QuasarPage()
    h1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-right q-pa-md")
    p1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis", classes="text-h2")

    high_charts = jp.HighCharts(a=webpage, classes='m-2 p-2 border')
    high_charts.options = chart_definition
    high_charts.options.title.text = "Average Rating by Week"

    high_charts.options.xAxis.categories = list(week_average.index)
    high_charts.options.series[0].data = list(week_average['Rating'])

    return webpage


jp.justpy(app)