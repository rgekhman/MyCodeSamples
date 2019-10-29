#
# Roman Gekhman 
#
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas_datareader import data as wb
import pandas as pd
import configparser as cfg
import socket
import os
import argparse
import csv
from prettytable import PrettyTable as ptb

# get config settings

curr_dir = os.path.dirname(os.path.realpath(__file__))
Config = cfg.ConfigParser()
Config._interpolation = cfg.ExtendedInterpolation()
Config.read(curr_dir + '\\config.ini')
root_dir = Config.get('plotSparkLines', 'root_dir')
output_dir = Config.get('Common', 'output_dir')
output_sub_dir = Config.get('plotSparkLines', 'output_sub_dir')
output_file_name = Config.get('plotSparkLines', 'output_file_name')
output_file_tickerlist = Config.get('plotSparkLines', 'output_file_tickerlist')
output_file_full_report = Config.get('plotSparkLines', 'output_file_full_report')

parser = argparse.ArgumentParser()

# ex: --tickers

parser.add_argument('--tickers', '-t', type=str, required=False)

parser.add_argument('--ivgauge_file', '-ivg', type=str, required=True)

parser.add_argument('--corr_file', '-corr', type=str, required=True)

parser.add_argument('--corr_constraint', '-cc', type=str,
                    required=False)

parser.add_argument('--title', '-ttl', type=str,
                    required=False)

args = parser.parse_args()

_tickers = []

# tickers = []

if not args.tickers:
    _tickers = ['SPY', 'MU', 'GLD']
else:
    _tickers = args.tickers.split(',')

#print( 'tickers : {}'.format(_tickers))

_ivgauge_file = ''
if args.ivgauge_file:
    _ivgauge_file = args.ivgauge_file

_corr_file = ''
if args.corr_file:
    _corr_file = args.corr_file

_corr_constraint = ''
if args.corr_constraint:
    _corr_constraint = args.corr_constraint

_file_title = ''
if args.title:
	_now = datetime.datetime.now()
	_dateStr = _now.strftime('%d-%b-%Y_%I-%M-%p')
	_file_title = args.title
	output_file_tickerlist = output_file_tickerlist.replace("%title%",_file_title)
	output_file_full_report = output_file_full_report.replace("%title%",_file_title)
	output_file_full_report = output_file_full_report.replace("%timestamp%",_dateStr)
# set drive letter

#region "hi "
_host = socket.gethostname()
_drive_letter = 'C'
if 'RGEK-LAPTOP-' in _host:
    _drive_letter = 'D'
#endregion

_root_dir = _drive_letter + ':' + root_dir
_output_dir = _root_dir + output_dir + output_sub_dir
if not os.path.exists(_output_dir):
    os.makedirs(_output_dir)

def getDatesAndClose(df):
    i = 0
    _close = []
    _dates = []

    for _item in df:
        _dates.append(df['date'])
        i += 1

    for _item in df.close:
        _close.append(_item)

    return (_dates, _close)


def getIVGaugeData(ivgauge_file):
    if ivgauge_file == '':
        return pd.DataFrame({'A': []})
    else:
        return pd.read_csv(ivgauge_file, header=1, index_col=0)


def getCorrelationData(corr_file):
    if corr_file == '':
        return pd.DataFrame({'A': []})
    else:
        return pd.read_csv(corr_file, header=0, index_col=0, sep='\s+')


df_ivg = getIVGaugeData(_ivgauge_file)
df_corr = getCorrelationData(_corr_file)

# if constraints apply

if _corr_constraint != '':
    _col_name = df_corr.columns[0]
    _corr_constraint = _corr_constraint.replace('x', _col_name)
    _tickers_corr = \
        df_corr.index[df_corr.eval(_corr_constraint)].tolist()

    # intersection of two sets will be output list of tickers
    _tickers = list(set(_tickers) & set(_tickers_corr))

_1yrAgo = (datetime.datetime.now()
           - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
_5yrAgo = (datetime.datetime.now() - datetime.timedelta(days=5
           * 365)).strftime('%Y-%m-%d')
_1moAgo = (datetime.datetime.now()
           - datetime.timedelta(days=30)).strftime('%Y-%m-%d')

_tickers = sorted(_tickers)

#Output comma delimited list of tickers for this report
with open(_output_dir + "\\" + output_file_tickerlist, 'w',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(_tickers)


_ticker_data = [] 
_ticker_data_table = ptb(["Symbol", "IVG Desc", "IVG %" , "S&P Corr %"])

#output ticker spark lines, comma delimited ticker list and report file for all tickers.
for _ticker in _tickers:
	print( 'ticker : {}'.format(_ticker))

	df1yr = wb.DataReader(_ticker, data_source='iex', start=_1yrAgo)
	df5yr = wb.DataReader(_ticker, data_source='iex', start=_5yrAgo)
	df1mo = wb.DataReader(_ticker, data_source='iex', start=_1moAgo)

	(fig, (ax5yr, ax1yr, ax1mo)) = plt.subplots(nrows=1, ncols=3,
			figsize=(20, 3))
	_x1yr = []
	_x5yr = []
	_x1mo = []

	# print(df1mo.info())

	df1mo.reset_index(inplace=True, drop=False)
	df1yr.reset_index(inplace=True, drop=False)
	df5yr.reset_index(inplace=True, drop=False)

	# print(df1mo.info())

	years = mdates.YearLocator()  # every year
	months = mdates.MonthLocator()  # every month
	yearsFmt = mdates.DateFormatter('%Y')

	(dates1mo, _x1mo) = getDatesAndClose(df1mo)
	(dates1yr, _x1yr) = getDatesAndClose(df1yr)
	(dates5yr, _x5yr) = getDatesAndClose(df5yr)

	# plot 5yr chart

	ax5yr.xaxis.set_visible(False)
	ax5yr.plot(_x5yr, color='r', ls='solid', linewidth=1)
	ax5yr.set_title(_ticker + ' - 5yr')
	ax5yr.grid(True)

	# plot 1yr chart

	ax1yr.xaxis.set_visible(False)
	ax1yr.plot(_x1yr, color='b', ls='solid', linewidth=1)
	ax1yr.set_title(_ticker + ' - 1yr')
	ax1yr.grid(True)

	# plot 1mo chart

	ax1mo.xaxis.set_visible(False)
	ax1mo.plot(_x1mo, color='g', ls='solid', linewidth=1)
	ax1mo.set_title(_ticker + ' - 1mo')
	ax1mo.grid(True)

	_now = datetime.datetime.now()
	_dateStr = _now.strftime('%d-%b-%Y_%I-%M-%p')

	"""Add IV Gauge and Time Stamp to output File Name """
	#region 
	_ivg_val = ''
	_ivg_perc = 0
	_ivg_desc = ''
	try:
		if not df_ivg.empty:
			_ivg_desc = df_ivg.loc[_ticker][1]
			#_ivg_desc = _ivg_desc.replace(' ', '_')
			_ivg_perc = df_ivg.loc[_ticker][0]
			_ivg_val = _ivg_desc.replace(' ', '_') + '-' + str(_ivg_perc) + '%'
	except Exception as ex: 
		print("ivg error handler: \n{}".format(ex))
	#endregion

	_output_file_name = output_file_name.replace('%sym%', _ticker)
	_output_file_name = _output_file_name.replace('%ivg%', _ivg_val)
	_output_file_name = _output_file_name.replace('%timestamp%',
			_dateStr)

	_corr_val = 0
	"""Add S&P500 Correlation to output File Name """
	#region 
	try:
		if not df_corr.empty:
			_corr_val = df_corr.loc[_ticker][0]
	except Exception as ex: 
		print("Corr val error handler: {}".format(ex))
	#endregion

	_output_file_name = _output_file_name.replace('%spycorr%', str(_corr_val))

	# fig.autofmt_xdate()

	plt.savefig(_output_dir + '\\' + _output_file_name)
	plt.close(fig)

	#output line to a full report file
	_ticker_data.append([_ticker, _ivg_desc, int(_ivg_perc), int(_corr_val*100)])

#Sort by IV Gauge
_ticker_data = sorted(_ticker_data, key=lambda x: x[2], reverse=True)
#write report file
for _ticker_row in _ticker_data:
	_ticker_data_table.add_row(_ticker_row)

with open(_output_dir + "\\" + output_file_full_report, 'w', newline='') as report_file:
	report_file.write(str(_ticker_data_table))
	#writer = csv.writer(csvfile, delimiter="\t",lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	#write header
#	writer.writerow(["Symbol", "IVG Desc", "IVG %" , "S&P Corr %"])

	#write tickers
#	for _ticker_row in _ticker_data:
#		writer.writerow(_ticker_row)