$(document).ready(function () {
    $(function () {
        $('#daily-chart').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Power generation'
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Watt'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.1f} Watt</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0,
                    pointWidth: 3
                }
            },
            series: [
                {
                    name: 'Power Output',
                    data: data
                },
                {
                    name: 'Max Power Output ± 3 Days',
                    data: data_max
                }
            ]
        });
    });
});
    