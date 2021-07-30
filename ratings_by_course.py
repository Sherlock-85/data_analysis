import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib as plt

data = pandas.read_csv(r"C:\Users\kirst\pythonProject1\pythonProject1\pythonProject\data_analysis\review_analysis\reviews.csv",
                       parse_dates=["Timestamp"])
share = data.groupby(['Course Name'])['Rating'].count()

chart_definition = '''
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Percentage of course reviews by course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
'''

def app():
    webpage = jp.QuasarPage()
    h1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-right q-pa-md")
    p1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis", classes="text-h2")

    high_charts = jp.HighCharts(a=webpage, classes='m-2 p-2 border')
    high_charts.options = chart_definition
    high_charts_data = [{"name": v1, "y":v2} for v1,v2 in zip(share.index,share)]
    high_charts.options.series[0].data = high_charts_data
    return webpage


jp.justpy(app)