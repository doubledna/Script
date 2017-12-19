function loadcpu() {
    //发送请求
    $.getJSON('json/cpu.json', function (data) { //得到内容
$(document).ready(function() {
//var obj = JSON.parse('{ "hostname": ["192.168.229.128","192.168.229.129"],"used": [50,60] }');
   var chart = {
      type: 'bar'
   };
   var title = {
      text: 'CPU使用率'
   };
   var subtitle = {
      text: ''
   };
   var xAxis = {
      categories: data['hostname'],
      title: {
         text: null
      }
   };
   var yAxis = {
      min: 0,
	  max: 100,
      title: {
         text: '单位 (%)',
         align: 'high'
      },
      labels: {
         overflow: 'justify'
      }
   };
   var tooltip = {
      valueSuffix: ' %'
   };
   var plotOptions = {
      bar: {
         dataLabels: {
            enabled: true
         }
      },
	  series: {
	     stacking: 'normal'
	  }
   };
   var legend = {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'top',
      x: 10,
      y: 40,
      floating: true,
      borderWidth: 1,
      backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
      shadow: true
   };
   var credits = {
      enabled: false
   };

   var series= [ {
            name: 'precent',
            data: data['precent']
	    }
   ];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.subtitle = subtitle;
   json.tooltip = tooltip;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.series = series;
   json.plotOptions = plotOptions;
   json.legend = legend;
   json.credits = credits;
   $('#cpu').highcharts(json);

});
    });
}
function loadmemory() {
        $.getJSON('json/memory.json',function (data) {
            $(document).ready(function() {

   //var obj = JSON.parse('{ "hostname": ["192.168.229.128","192.168.229.129"],"used": [228,536],"free": [485,186] }');
   var chart = {
      type: 'bar'
   };
   var title = {
      text: '内存使用情况'
   };
   var subtitle = {
      text: ''
   };
   var xAxis = {
      categories: data['hostname'],
      title: {
         text: null
      }
   };
   var yAxis = {
      min: 0,
      title: {
         text: '单位 (M)',
         align: 'high'
      },
      labels: {
         overflow: 'justify'
      }
   };
   var tooltip = {
      valueSuffix: ' M'
   };
   var plotOptions = {
      bar: {
         dataLabels: {
            enabled: true
         }
      },
	  series: {
	     stacking: 'normal'
	  }
   };
   var legend = {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'top',
      x: 10,
      y: 40,
      floating: true,
      borderWidth: 1,
      backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
      shadow: true
   };
   var credits = {
      enabled: false
   };

   var series= [{
         name: 'free',
            data: data['free']
        },  {
            name: 'used',
            data: data['used']
	    }
   ];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.subtitle = subtitle;
   json.tooltip = tooltip;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.series = series;
   json.plotOptions = plotOptions;
   json.legend = legend;
   json.credits = credits;
   $('#memory').highcharts(json);
      });
    });
}

function loaduser() {
    //发送请求
    $.getJSON('json/user.json', function (data) { //得到内容
        var ret = [];
        $.each(data, function (i, entry) {
            var html = '<tr>'
            html = '<th>'+ "主机名" + '</th>'
            html += '<td  bgcolor="#FFFFFF">' + entry['hostname'] + '</td>';
            html += '</tr>'
            html += '<tr>'
            html += '<th rowspan="1">' + "在线用户" + '</th>'
            html += '<td  bgcolor="#ADFF2F">' + entry['user'] + '</td>';
            html += '</tr>';
            ret.push(html);
        });
        $('#user').html('<table border="1">' + ret.join('') + '</table>');
    });
}

function loaddisk() {
    //发送请求
    $.getJSON('json/disk.json', function (data) { //得到内容

        $(document).ready(function () {
            var chart = {
                type: 'bar'
            };
            var title = {
                text: '磁盘剩余情况'
            };
            var subtitle = {
                text: null
            };
            var xAxis = {
                categories: data['hostname'],
                title: {
                    text: null
                }
            };
            var yAxis = {
                min: 0,
                title: {
                    text: '单位 (M)',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
            };
            var tooltip = {
                valueSuffix: ' M'
            };
            var plotOptions = {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            };
            var legend = {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: 10,
                y: 40,
                floating: true,
                borderWidth: 1,
                backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
                shadow: true
            };
            var credits = {
                enabled: false
            };

            var series = [{
                name: '/',
                data: data['/']
            }, {
                name: '/boot',
                data: data['/boot']
            }
            ];

            var json = {};
            json.chart = chart;
            json.title = title;
            json.subtitle = subtitle;
            json.tooltip = tooltip;
            json.xAxis = xAxis;
            json.yAxis = yAxis;
            json.series = series;
            json.plotOptions = plotOptions;
            json.legend = legend;
            json.credits = credits;
            $('#disk').highcharts(json);

        });
    });
}
function loadprocess() {
    //发送请求
    $.getJSON('json/process.json', function (data) { //得到内容
        var ret = [];
        $.each(data, function (i, entry) {
            var html = '<tr>'
            html = '<th>'+ "主机名" + '</th>'
            html += '<td  bgcolor="#FFFFFF">' + entry['hostname'] + '</td>';
            html += '</tr>'
            html += '<tr>'
            html += '<th>'+ "进程名" + '</th>'
            html += '<td  bgcolor="#FFFFFF">' + entry['process'] + '</td>';
            html += '</tr>'
            html += '<tr>'
            html += '<th>'+ "状态" + '</th>'
            if (entry['status'] == "running"){
                html += '<td  bgcolor="#ADFF2F">' + entry['status'] + '</td>';
            }
            else{
                html += '<td  bgcolor="FF0000">' + entry['status'] + '</td>';
            }
            //html += '<td  bgcolor="#ADFF2F">' + entry['status'] + '</td>';
            html += '</tr>';
            ret.push(html);
        });
        $('#process').html('<table border="1">' + ret.join('') + '</table>');
    });
}
// 定时器
$(document).ready(function () {
    loadcpu();
    loaduser();
    loaddisk();
    loadprocess();
    loadmemory(); //先执行一次，将内容显示出来
    setInterval(loadcpu,10*1000);
    setInterval(loaduser,10*1000);
    setInterval(loaddisk,10*1000);
    setInterval(loadprocess,10*1000);
    setInterval(loadmemory,10*1000); //然后每隔10秒执行一次,时间请根据需要自己修改
});
