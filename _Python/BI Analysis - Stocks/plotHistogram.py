#
# Roman Gekhman 
#

# pip install plotly
#
#Depends:
#pip install ConfigParser, pandas, plotly, matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import os, glob
import socket
import matplotlib.pylab as pylab
import configparser as cfg
import datetime

def getNumberOfUniqueSamples(_dir):
	# Count number of samples 
	os.chdir(_dir)

	files = glob.glob("*.csv")
	files.sort(key=os.path.getmtime)

	_uniqueDates = set()
	#construct list of unique dates 
	for file in files:
		_uniqueDates.add(file[:10])

	return len(_uniqueDates)

# get config settings
curr_dir = os.path.dirname(os.path.realpath(__file__))
Config = cfg.ConfigParser()
Config._interpolation = cfg.ExtendedInterpolation()
Config.read(curr_dir + "\\config.ini")
root_dir = Config.get('PlotHistogram', 'root_dir')
csv_dir = Config.get('PlotHistogram', 'csv_dir')
output_dir = Config.get('Common', 'output_dir')
output_sub_dir = Config.get('PlotHistogram', 'output_sub_dir')
input_sub_dir = Config.get('PlotHistogram', 'input_sub_dir')
fileName_allEquities = Config.get('PlotHistogram', 'fileName_allEquities')
distribFileName = Config.get('PlotHistogram', 'distribFileName')

#set drive letter
_host = socket.gethostname()
_drive_letter = 'C'
if "RGEK-LAPTOP-" in _host:
	_drive_letter = 'D'

#set work folders
_root_dir = _drive_letter + ":" + root_dir
_csv_dir = _root_dir + csv_dir 

_sample_count = getNumberOfUniqueSamples(_csv_dir)

os.chdir(_root_dir)

_output_dir = _root_dir + output_dir + output_sub_dir
_input_dir = _root_dir + output_dir + input_sub_dir
if not os.path.exists(_output_dir):
    os.makedirs(_output_dir)

_fileName_allEquities = fileName_allEquities #"_universe.csv"
_distribFileName = distribFileName #"tickers_distrib.png"

#get data, rename value column
df = pd.read_csv(_input_dir + "\\" + _fileName_allEquities, sep=',',header=None, index_col =0)
df = df.rename(columns = {1: 'frequency'})

# Std and Mean of population
_std = round(df.std().values[0],2)
_2std = round(df.std().values[0]*2,2)
_mean = round(df.mean().values[0],2)

params = {
          'figure.figsize': (10, 15),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large',
		 'legend.fontsize': 'x-large'}

pylab.rcParams.update(params)

#sort by value and index Frequency Descending, Tickers ascending
df['MyIdx'] = df.index
df = df.sort_values(by = ['frequency', 'MyIdx'], ascending = [True, False])

# Only want to see above mean
df = df.ix[df['frequency'] > _mean]
# Std and Mean of population
_count = round(df.count().values[0],2)
_mean2 = round(df.mean().values[0],2)
_std2 = round(df.std().values[0],2)
df.plot.barh() #figsize=(10,15)

plt.xlabel('Frequency')
plt.ylabel('Symbols')

_now = datetime.datetime.now()
_dateStr = _now.strftime("%d %b %Y - %I:%M %p")

_title = _dateStr + '\nSymbols distribution by frequency, above mean only.\n' + \
		  ' Sample Cnt : ' + str(_sample_count) + \
		  ', Symbol Cnt : ' + str(_count) #+ \
		  #'\n' + \
		  #'$\sigma$ (sample) : ' + str(_std2) + \
		  #', $\sigma$ (pop) : ' + str(_std)
		  

plt.title(_title, fontsize=16)

plt.axvline(x=_mean, color='g', linestyle='-')
#plt.axvline(x=_mean2, color='b', linestyle='--')
plt.axvline(x=_mean + _std, color='b', linestyle='-.')
plt.axvline(x=_mean + _2std, color='r', linestyle='-.')
plt.legend(['$\mu$ (pop) : ' + str(_mean), 
		   '$\sigma$ (pop) : ' + str(_std), 
		   '2$\sigma$ (pop) : ' + str(_2std)])

# TODO: Look into drawing a fitting line 
# https://plot.ly/matplotlib/histograms/

#plt.show()
plt.savefig(_output_dir + "\\" + _distribFileName)