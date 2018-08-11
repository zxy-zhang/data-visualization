
# import requests
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

# req=requests.get(json_url)
# # 将数据写入文件
# with open('btc_close_2017_request.json', 'w') as f: 
#     f.write(req.text)
# file_requests=req.json()
import json 
import pygal
import math

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f) 

#打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month =int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close'])) 
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))

#创建5个列表，分别存储日期和收盘价
dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]

#每一天的信息
for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))


line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='收盘价对数变换(￥)'
line_chart.x_labels=dates
N=20#x坐标轴每隔20天显示一次
line_chart.x_labels_major=dates[::N]
close_log=[math.log10(_) for _ in close]
line_chart.add('log收盘价',close_log)
line_chart.render_to_file('收盘折对数变换价线图(￥).svg')

from itertools import groupby

def draw_line(x_date,y_date,title,y_legend):
    xy_map=[]
    for x,y in groupby(sorted(zip(x_date,y_date)),key=lambda _:_[0]):
        y_list=[v for _,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
        x_unique,y_mean=[*zip(*xy_map)]
        line_chart=pygal.Line()
        line_chart.title=title
        line_chart.x_labels=x_unique
        line_chart.add(y_legend,y_mean)
        line_chart.render_to_file(title+'.svg')
        return line_chart

        idx_month=dates.index('2017-12-01')
        line_chart_month=draw_line(months[:idx_month],close[:idx_month],'收盘价月日均值（￥）','月日均值')
        line_chart_month