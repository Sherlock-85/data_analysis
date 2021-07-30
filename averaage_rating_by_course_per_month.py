import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib as plt

data = pandas.read_csv(r"C:\Users\kirst\pythonProject1\pythonProject1\pythonProject\data_analysis\review_analysis\reviews.csv", parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack()
print(month_average_crs)

chart_definition = '''
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average rating by course per month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
             '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Ratings'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
'''

def app():
    webpage = jp.QuasarPage()
    h1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-right q-pa-md")
    p1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis", classes="text-h2")

    high_charts = jp.HighCharts(a=webpage, classes='m-2 p-2 border')
    high_charts.options = chart_definition
    high_charts.options.xAxis.categories = list(month_average_crs.index)

    high_charts_data = [{"name": v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    high_charts.options.series = high_charts_data

    return webpage


jp.justpy(app)
