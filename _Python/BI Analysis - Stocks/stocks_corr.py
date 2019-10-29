"""

	Build stocks to SPY correlation 1D vector

"""
#
# Roman Gekhman 
#
from _reqs import pip_install_requirements as pir
_reqs = ['numpy','pandas','pandas_datareader','matplotlib','seaborn','configparser','argparse']
pir.install_requirements(_reqs)

import numpy as np
import pandas as pd
#used to grab the stock prices, with IEX api
import pandas_datareader as web
from datetime import datetime
#to visualize the results
import matplotlib.pyplot as plt
import seaborn
import socket, os
import datetime as dt
import configparser as cfg
import argparse 
import matplotlib.pylab as pylab
#import datetime as dt

parser = argparse.ArgumentParser()  
# ex: --tickers 
parser.add_argument("--tickers", "-t", type=str, required=False)
# ex: --tickers 
parser.add_argument("--shift_years", "-sy", type=int, required=False)
args = parser.parse_args()

tickers = []
#tickers = []
if not args.tickers:
	#read data from file of selected stocks
	tickers = ['GLD','NEM','RGLD','KGC','GFI','PVG','HMY','ALIAF','MUX','GSS','GORO','VGZ']
else:
	tickers = args.tickers.split(",")

if "SPY" not in tickers:
	tickers.append("SPY")
	
#how many years back to fetch data
shift_years = 5
if args.shift_years:
	shift_years = args.shift_years

#select start date for correlation window as well as list of tickers
now = dt.datetime.now()
start_year = now.year - shift_years
start = datetime(start_year, 1, 1)


#remove new lines
tickers = list(map(lambda s: s.strip(), tickers))

# get config settings
curr_dir = os.path.dirname(os.path.realpath(__file__))
Config = cfg.ConfigParser()
Config._interpolation = cfg.ExtendedInterpolation()
Config.read(curr_dir + "\\config.ini")
root_dir = Config.get('stocks_corr', 'root_dir')
output_dir = Config.get('Common', 'output_dir')
output_sub_dir = Config.get('stocks_corr', 'output_sub_dir')
output_file_name = Config.get('stocks_corr', 'output_file_name')
output_file_name_txt = Config.get('stocks_corr', 'output_file_name_txt')
api_key = Config.get('stocks_corr', 'api_key')
api_host = Config.get('stocks_corr', 'api_host')

# iex api pk_1e5665176d574d81993f8c6fbcfef71d

#set drive letter
_host = socket.gethostname()
_drive_letter = 'C'
if "RGEK-LAPTOP-" in _host:
	_drive_letter = 'D'

_root_dir = _drive_letter + ":" + root_dir
_output_dir = _root_dir + output_dir + output_sub_dir
if not os.path.exists(_output_dir):
    os.makedirs(_output_dir)

#array to store prices
symbols=[]

#pull price using iex for each symbol in list defined above
for ticker in tickers: 
	try:
		#r = web.DataReader(name=ticker, data_source=api_host, start=start, access_key=api_key)
		r = web.DataReader(name=ticker, data_source=api_host, start=start)
		r['Symbol'] = ticker
		
		# add a symbol column
		symbols.append(r)
	except Exception as ex:
		print(ex);		


# concatenate into df
df = pd.concat(symbols)
df = df.reset_index()
df = df[['Date', 'Close', 'Symbol']]
print("df.head() : {}", df.head())

df_pivot = df.pivot('Date','Symbol','Close').reset_index()
print("df_pivot : {}",df_pivot)

# move the column to head of list using index, pop and insert
cols = list(df_pivot)
cols.insert(1, cols.pop(cols.index('SPY')))
print("cols : \n{}\n",cols)
df_pivot = df_pivot.loc[:, cols]

corr_df = df_pivot.corr(method='pearson')
#reset symbol as index (rather than 0-X)
corr_df.head().reset_index()
del corr_df.index.name
print("corr_df : \n{}\n",corr_df)

#
#smooth-adjust output size of the image proportionally to number of tickers
#
fig_side = 5
ticker_count = len(tickers)
fig_side *= int(round(np.log(ticker_count),0))

params = {
          'figure.figsize': (fig_side, fig_side),
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'large',
		 'legend.fontsize': 'large'}

pylab.rcParams.update(params)

_now = datetime.now()
_dateStr = _now.strftime("%d %b %Y")
_startDateSt = start.strftime("%d %b %Y")

_title = _dateStr + '\nSymbols correlation matrix.\n Since ' + _startDateSt

plt.title(_title, fontsize=fig_side)

#take the bottom triangle since it repeats itself
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True

#drop numbers above diagonal
t_corr_df = (mask * corr_df).T
t_corr_df = t_corr_df.round(2)
t_corr_df = t_corr_df.replace(-0.00, 0.00)
print(t_corr_df)

#output correlations to a table
with open(_output_dir + "\\" + output_file_name_txt,'w') as outfile:
	t_corr_df["SPY"].to_string(outfile)

#generate plot
seaborn.heatmap(corr_df, cmap='coolwarm', vmax=1.0, vmin=-1.0 , mask = mask, linewidths=2.5)
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
#plt.show()
plt.savefig(_output_dir + "\\" + output_file_name)