import csv
from datetime import datetime
from matplotlib import pyplot as plt 
#从文件中获取日期和最高气温以及最低气温
filename='death_valley_2014.csv'
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)

	dates,highs,lows=[],[],[]
	for row in reader:
		try:
			current_date=datetime.strptime(row[0],"%Y-%m-%d")
			high=int(row[1])
			low=int(row[3])
		except ValueError:
			print(current_date,'missing data')

		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	# for index,column_header in enumerate(header_row):
	# 	print(index,column_header)
	
	#根据数据绘制图形
	flg=plt.figure(dpi=128,figsize=(10,6))
	#alpha为指定颜色透明度
	plt.plot(dates,highs,c='red',alpha=0.5)
	plt.plot(dates,lows,c='blue',alpha=0.5)
	plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

	#设置图形格式
	title="Daily high and low temperatures-2014 \nDeath Valley,CA"
	plt.title(title,fontsize=20)
	plt.xlabel("",fontsize=16)
	#绘制斜的日期标签
	flg.autofmt_xdate()
	plt.ylabel("Temperatures(F),fontsize=14")
	plt.tick_params(axis='both',which='major',labelsize=16)
	

	plt.show()