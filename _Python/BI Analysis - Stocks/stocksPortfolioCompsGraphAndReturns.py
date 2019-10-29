#
# Roman Gekhman 
#
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from datetime import datetime
from datetime import date
import argparse 
from pandas.tseries.offsets import BDay
import matplotlib.pylab as pylab
import configparser as cfg
import socket

def getBizDaysCount(drg, start_date, endDate):
    A = [d.date() for d in drg]
    B = pd.Timestamp(endDate, 'B').date()
    return np.busday_count(A, B)

def getPortfolioReturnPercents(_mydata, _tickers, start_date):
	''' portfolio return '''
	returns = (_mydata / _mydata.shift(1)) - 1 
	#print(returns.head())

	#add weights, assumin equal number of shares of each stock
	cnt = len(_tickers)
	list = []
	for i in range (0, cnt):
		list.append(1/cnt)
	weights = np.array(list)

	startDate = datetime.strptime(start_date , '%Y-%m-%d') 
	endDate = datetime.today()
	drg = pd.date_range(startDate, endDate, freq='B')

	daysToDate = drg.size
	#getBizDaysCount(drg, startDate, endDate)

	#Calculate portfolio return in percents
	ann_ret = returns.mean() * 250
	to_date_ret = returns.mean() * daysToDate

	return round(np.dot(ann_ret, weights) * 100, 2), round(np.dot(to_date_ret, weights) * 100, 2)

def plotGraph(_tickers, _output_file_name, start_date):
	''' build dataframe of ticker data '''
	mydata = pd.DataFrame()
	for t in tickers:
		mydata[t] = wb.DataReader(t, data_source='iex', start=_startDate)['close']

	print(mydata.head())

	annRet, toDateRet = getPortfolioReturnPercents(mydata, tickers, start_date)

	#Normalize data on graphs to start from one point.
	myValues = mydata / mydata.iloc[0] * 100
	myDates = mydata.index.values
	
	# Sort legend based on last values of the lines
	t = myValues.plot(figsize = (10,6))

	lineVal = []
	for line, ticker in zip(t.lines, _tickers):
		lineVal.append((ticker, line._y[-1], line))

	lineVal.sort(key=lambda tup: tup[1], reverse=True)

	#tVals = tuple(x[1] for x in lineVal)
	tLabels = tuple(x[0] for x in lineVal)
	tLines = tuple(x[2] for x in lineVal)

	params = {
			  'figure.figsize': (15, 10),
			 'axes.labelsize': 'x-large',
			 'axes.titlesize':'x-large',
			 'xtick.labelsize':'x-large',
			 'ytick.labelsize':'x-large',
			 'legend.fontsize': 'x-small'}

	pylab.rcParams.update(params)

	plt.legend(tLines, tLabels, loc='upper left')
	plt.axhline(y=100, color='r', linestyle='--')
	plt.title('Portfolio return since {}\nYTD : {}%      Annualized : {}%'.format(_startDate, toDateRet,annRet))
	plt.xlabel('Time')
	plt.ylabel('Relative stock performance')

	ticks = np.arange(0,myDates.size,step=30)
	plt.xticks(ticks,(myDates[_tick] for _tick in ticks))
	plt.yticks([])
	
	plt.gcf().autofmt_xdate()

	#plt.show()
	plt.savefig(_output_file_name)

	print("Annualized return {}%".format(annRet))
	print("YTD return {}%".format(toDateRet))

parser = argparse.ArgumentParser()  
# ex: --tickers 
parser.add_argument("--tickers", "-t", type=str, required=False)
# ex: --startdate 2018-01-01
parser.add_argument("--startdate", "-sd", type=str, required=False)
# ex: --infilename 
parser.add_argument("--infilename", "-ifn", type=str, required=False)
# ex: --outfilename 
parser.add_argument("--outfilename", "-ofn", type=str, required=False)
# ex: --spy 
parser.add_argument("-spy", type=str, required=False)
args = parser.parse_args()

# get config settings
curr_dir = os.path.dirname(os.path.realpath(__file__))
Config = cfg.ConfigParser()
Config._interpolation = cfg.ExtendedInterpolation()
Config.read(curr_dir + "\\config.ini")
root_dir = Config.get('stocksPortfolioCompsGraphAndReturns', 'root_dir')
input_file_name = Config.get('stocksPortfolioCompsGraphAndReturns', 'input_file_name')
output_file_name = Config.get('stocksPortfolioCompsGraphAndReturns', 'output_file_name')
output_dir = Config.get('Common', 'output_dir')
output_sub_dir = Config.get('stocksPortfolioCompsGraphAndReturns', 'output_sub_dir')

_startDate = ''
if not args.startdate:
	# Get first day of the year
	_startDate = datetime.now().date().replace(month=1, day=1).strftime('%Y-%m-%d')
else:
	_startDate = args.startdate

#set drive letter
_host = socket.gethostname()
_drive_letter = 'C'
if "RGEK-LAPTOP-" in _host:
	_drive_letter = 'D'

#driveLetter = os.path.splitdrive(os.getcwd())
#driveLetter = driveLetter[0]

_dir = _drive_letter + ":" + root_dir
os.chdir(_dir)

_output_dir = _dir + output_dir + output_sub_dir

if not os.path.exists(_output_dir):
    os.makedirs(_output_dir)

_output_file_name = ''
if not args.outfilename:
	_output_file_name = output_file_name
else:
	_output_file_name = args.outfilename

_input_file_name = ''
if not args.infilename:
	_input_file_name = input_file_name
else:
	_input_file_name = args.infilename

#tickers = ["STX","AMAT","LNG","MOMO","CAR","NUE","TRIP","SCHW","DVN","FSLR","SLCA","QCOM"]
tickers = []
if not args.tickers:
	#read data from file of selected stocks
	df = pd.read_csv(_input_file_name, sep=',',header=None, index_col =0)

	#get ticker names in a list
	tickers = list(df.index.values)
else:
	tickers = args.tickers.split(",")

if args.spy:
	tickers.append("SPY")

plotGraph(tickers, _output_dir + "\\" + _output_file_name, _startDate)


