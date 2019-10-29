#
# Load Forex Data Files for H4, H1, H30 TFs and output graphs of average candles per TF
#
import numpy as np
import datetime 
#import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas_datareader import data as wb
import pandas as pd
import configparser as cfg
import socket
import os
import argparse
import csv
import arrow
#import oandapy as opy
#import plotly.graph_objs as go

# get config file params
curr_dir = os.path.dirname(os.path.realpath(__file__))
Config = cfg.ConfigParser()
Config._interpolation = cfg.ExtendedInterpolation()
Config.read(curr_dir + '\\config.ini')
root_dir = Config.get('getMarketPulse', 'root_dir')
output_dir = Config.get('Common', 'output_dir')
output_sub_dir = Config.get('getMarketPulse', 'output_sub_dir')
output_file_name = Config.get('getMarketPulse', 'output_file_name')
mt4csv_folder = Config.get('MT4CsvFolder', 'csv_dir')
oanda_access_token = Config.get('Oanda', 'access_token')
output_file_name_stats = Config.get('getMarketPulse', 'output_file_name_stats')

# get params
parser = argparse.ArgumentParser()
parser.add_argument('--ccy', '-ccy', type=str, required=True)
# in minutes ex: [240,60,15,5]
parser.add_argument('--timeframes', '-tfs', type=str, required=True)
parser.add_argument('--shift', '-s', type=str, required=True)
parser.add_argument('--title', '-ttl', type=str,
                    required=False)
args = parser.parse_args()

# 
_ccy = args.ccy
_title = args.title
_time_frames = args.timeframes.split(",")
_date_shift = int(args.shift)

#region " Prep folders "
_host = socket.gethostname()
_drive_letter = 'C'
if 'RGEK-LAPTOP-' in _host:
	_drive_letter = 'D'

_root_dir = _drive_letter + ':' + root_dir
_output_dir = _root_dir + output_dir + output_sub_dir + "\\"
if not os.path.exists(_output_dir):
	os.makedirs(_output_dir)

#endregion

def plotData(_dfs):
	"""	Plot Trends """
	_now = datetime.datetime.now()
	_dateStr = _now.strftime("%d %b %Y - %I:%M %p")
	_title = _dateStr + '   Currency : ' + _ccy + '   Shift (days): ' + str(_date_shift)
	
	#Plot Bar Chrats
	fig, (_subplots) = plt.subplots(nrows=1, ncols=len(_dfs), figsize=(len(_dfs)*5, 5))

	#ax = plt.axes()
	for i, _df in enumerate(_dfs):
		# plot chart
		_key = list(enumerate(_df))[0][1]
		_df[_key].plot(ax=_subplots[i],kind='bar')
		ax = _subplots[i]
		ax.title.set_text('Timeframe : {} min'.format(_key))
		if int(_key) < 60:
			ax.xaxis.set_major_formatter(plt.NullFormatter())

	#plt.savefig(_output_dir + '\\' + _output_file_name)
	#plt.close(fig)

	fig.suptitle(_title, fontsize=16)
	plt.show()


def plotTestChart2(_dfs):
	"""
	========
	Barchart 2
	========

	A bar plot with errorbars and height labels on individual bars
	"""
	import random
	
	_hours = 24
	
	_key = list(list(enumerate(_dfs))[0][1])[0]
	_fr = _dfs[0][_key]
	
	#convert index to cols
	#print("_fr : \n{}".format(_fr))
	#_fr.reset_index(level=0, inplace=True)
	#_fr.reset_index(level=0, inplace=True)
	#_fr.reset_index(level=0, inplace=True)
	#_fr = _fr.drop(columns=['WeekDayIndex'])
	#print("_fr : \n{}".format(_fr))

	# How many weeks are we considering? 
	# It will define the number of bar charts per one hour
	_weeks = len(_fr.WeekNumber.unique())

	ind = np.arange(_hours)  # the x locations for the groups
	width = 0.35       # the width of the bars

	mon_wk1 = tuple(random.sample(range(1, 100), _hours))
	mon_wk2 = tuple(random.sample(range(1, 100), _hours))
	mon_wk3 = tuple(random.sample(range(1, 100), _hours))

	#Plot Bar Chrats
	fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(25, 5))

	rects1 = ax.bar(ind, mon_wk1, width, color='r')
	rects2 = ax.bar(ind + width, mon_wk2, width, color='y')
	rects3 = ax.bar(ind + width, mon_wk3, width, color='g')
	rects4 = ax.bar(ind + width, women_means, width, color='b')
	rects5 = ax.bar(ind + width, women_means, width, color='o')


	# add some text for labels, title and axes ticks
	ax.set_ylabel('Value')
	ax.set_title('Week Day X')
	ax.set_xticks(ind + width / 2)
	k = ','.join(str(e) for e in list(range(0, 24)))
	ax.set_xticklabels(('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','23'))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Mon', 'Tue','Wed','Thur','Fri'))


	def autolabel(rects):
		"""
		Attach a text label above each bar displaying its height
		"""
		for rect in rects:
			height = rect.get_height()
			ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
					'%d' % int(height),
					ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)

	plt.show()

def getDataGrouppedByTime():
	""" Read data and filter """
	column_names = ['Date','Time','Open','High','Low','Close','Volume','Bar']

	_base_date = arrow.now()
	_start_date = _base_date.shift(days=_date_shift).format("YYYY-MM-DD")

def getDataGrouppedByWeekDayAndTime():
	""" Read data and filter """
	column_names = ['Date','Time','Open','High','Low','Close','Volume']

	_base_date = arrow.now()
	_start_date = _base_date.shift(days=_date_shift).format("YYYY-MM-DD")
	_end_date = _base_date.shift(days=0).format("YYYY-MM-DD")

	def getSignalToNoise(row):
		try: 
			return np.round(row.OC / row.HL,5)
		except: 
			return float('NaN')

	def getIsExciting(row):
		if abs(row.HL) == 0:
			row.isExciting = False
		else:
			if abs(row.OC / row.HL)   >= 0.6 :
				row.isExciting = True
			else:
				row.isExciting = False
		return row.isExciting

	_dfs = []
	for _tf in _time_frames:
		_df = pd.read_csv(mt4csv_folder + _ccy + _tf + ".csv", delimiter=';', parse_dates=True, header=None, names=column_names)
		_df['Date'] = pd.to_datetime(_df['Date'])
		print("_df : \n{}".format(_df))
		_df = _df.loc[(_df['Date'] >= _start_date)]
		_df['OC'] = np.round(_df["Close"] - _df["Open"], 5)
		_df['absOC'] = abs(_df['OC'])
		_df['HL'] = np.round(_df["High"] - _df["Low"], 5)
		_df['SignalToNoise'] = _df.apply(getSignalToNoise, axis=1)
		_df['isExciting'] = _df.apply(getIsExciting, axis=1)
		_df['WeekDay'] = _df['Date'].dt.weekday_name
		_df['WeekNumber'] = _df['Date'].dt.week
		_df['WeekDayIndex'] = _df['Date'].dt.dayofweek 
		_df['WeekDay'] = _df['Date'].dt.weekday_name
		#print("_df.shape before sat/sun removed: \n{}".format(_df.shape))
		#remove Saturdays and sundays
		_df = _df.loc[(_df.WeekDay != 'Saturday') & (_df.WeekDay != 'Sunday')]
		#print("_df.shape after sat/sun removed: \n{}".format(_df.shape))
		print("_df : \n{}".format(_df))

		#build pivot table volatility
		p_df = _df.groupby(['WeekNumber','WeekDayIndex','WeekDay','Time'])['HL'].mean()
		p_df = p_df.to_frame()
		p_df = p_df.sort_values(['WeekDayIndex','Time','WeekNumber'], ascending=[True, True, True])
		p_df = p_df.rename(columns={p_df.columns[0]: "Volatility"})
		
		print("p_df : \n{}".format(p_df))

		#build pivot table of excited bars
		#	Remove unexciting candles	
		_df = _df.loc[(_df['isExciting'] == True)]
		p_df2 = _df.groupby(['WeekNumber','WeekDayIndex','WeekDay','Time'])['absOC'].mean()
		p_df2 = p_df2.to_frame()
		p_df2 = p_df2.sort_values(['WeekDayIndex','Time','WeekNumber'], ascending=[True, True, True])
		p_df2 = p_df2.rename(columns={p_df2.columns[0]: "Exciting_OC"})
		
		print("p_df2 : \n{}".format(p_df2))

		df_res = pd.merge(p_df, p_df2, how='left', on=['WeekNumber','WeekDayIndex','WeekDay','Time'])
		#df_res = pd.merge(df_res, p_df3, how='left', on=['WeekNumber','WeekDayIndex','WeekDay','Time'])
		df_res['ccy'] = _ccy
		df_res = df_res.fillna(0.0)
		print("df_res : \n{}".format(df_res))

		#convert index to columns
		df_res.reset_index(level=0, inplace=True)
		df_res.reset_index(level=0, inplace=True)
		df_res.reset_index(level=0, inplace=True)
		#df_res = df_res.drop(columns=['WeekDayIndex'])
		print("df_res : \n{}".format(df_res))

		_dfs.append({_tf : [df_res, np.round(_df.SignalToNoise.mean(),5)]})

	return _dfs

def saveToCsv(_dfs):
	""" Output to CSV file """

	for i, _df in enumerate(_dfs):
		_tf = list(enumerate(_df))[0][1]

		_output_file_name = output_file_name.replace('%ccy%', _ccy)
		_output_file_name = _output_file_name.replace('%timeframe%', _tf)

		_output_file_name_stats = output_file_name_stats.replace('%ccy%', _ccy)
		_output_file_name_stats = _output_file_name_stats.replace('%timeframe%', _tf)

		#output df to csv file
		print("==> data to : {}".format(_output_dir + _output_file_name))
		_df[_tf][0].to_csv(_output_dir + _output_file_name, sep=',', encoding='utf-8')

		print("==> stats data to : {}".format(_output_dir + _output_file_name_stats))
		with open(_output_dir + _output_file_name_stats, mode='w') as _file:
			_writer = csv.writer(_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			#_writer.writerow(['SignalToNoise'])
			_writer.writerow([_ccy, _tf, _df[_tf][1]])


def main():
	_dfs = getDataGrouppedByWeekDayAndTime()
	saveToCsv(_dfs)

if __name__== "__main__":
	main()

