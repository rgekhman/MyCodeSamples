#
# Roman Gekhman 
#
#
# 1. Creates a distribution from *.csv files
# 2. Uses Pandas DataFrames to group, count, sort frequencies of equity occurences
# 3. Output file of all equities.
# 4. Output file of selected equities based on standard deviation.
#

import pandas as pd
import chardet
import os
import socket
import csv
import configparser as cfg
import argparse 

#get folder to scan
parser = argparse.ArgumentParser()  
# ex: --folder 
parser.add_argument("--folder", "-f", type=str, required=True)
args = parser.parse_args()
_folder = args.folder

#Get file encoding
def get_encoding(_file1):
	rawdata = open(_file1, 'rb').read()
	enc = chardet.detect(rawdata)
	return(enc['encoding'])

# get config settings
curr_dir = os.path.dirname(os.path.realpath(__file__))
Config = cfg.ConfigParser()
Config._interpolation = cfg.ExtendedInterpolation()
Config.read(curr_dir + "\\config.ini")
root_dir = Config.get('BuildEquityFiles', 'root_dir')
csv_dir = Config.get('BuildEquityFiles', 'csv_dir')
output_dir = Config.get('Common', 'output_dir')
output_sub_dir = Config.get('BuildEquityFiles', 'output_sub_dir')
_fileName_universe = Config.get('BuildEquityFiles', 'fileName_universe')
_fileName_aboveMean = Config.get('BuildEquityFiles', 'fileName_aboveMean')
_fileName_belowMean = Config.get('BuildEquityFiles', 'fileName_belowMean')
_filename_output_AboveMean = Config.get('BuildEquityFiles', 'filename_output_AboveMean')
_filename_output_AboveMean_wsp = Config.get('BuildEquityFiles', 'filename_output_AboveMean_wsp')
_filename_output_BelowMean = Config.get('BuildEquityFiles', 'filename_output_BelowMean')

_filename_output_AboveMean = _filename_output_AboveMean.replace('%env%',_folder)
_filename_output_AboveMean_wsp = _filename_output_AboveMean_wsp.replace('%env%',_folder)
_filename_output_BelowMean = _filename_output_BelowMean.replace('%env%',_folder)

#set drive letter
_host = socket.gethostname()
_drive_letter = 'C'
if "RGEK-LAPTOP-" in _host:
	_drive_letter = 'D'

_root_dir = _drive_letter + ":" + root_dir
os.chdir(_root_dir)

_csv_dir = _root_dir + csv_dir 
_files = os.listdir(_csv_dir)

_output_dir = _root_dir + output_dir + output_sub_dir
if not os.path.exists(_output_dir):
    os.makedirs(_output_dir)

_dframes = []
for _file in _files:
	_fileName = _csv_dir + '\\' + _file
	df = pd.read_csv(_fileName,sep=',',encoding = get_encoding(_fileName))
	_dframes.append(df)

#Create sorted list of symbols by frequency of occurence
_df = pd.concat(_dframes, sort=False)
_dfCnt = _df.groupby(['Symbol']).size().reset_index(name='counts')
_dfCnt = _dfCnt.sort_values(by=['counts'], ascending=False)

_mean = round(_dfCnt.mean().values[0],2)
print("Mean : ", _mean)

#_intMax = _dfCnt.max()[1]
#print("Max : ", _intMax)

#Output all to *.csv file
_dfCnt.to_csv(_output_dir + "\\" + _fileName_universe, sep=',', header=False, index=False)

#Output selected to *.csv file 
# use 2 standard deviations as filter
_dfCnt.loc[_dfCnt['counts'] > _mean].to_csv(_output_dir + "\\" + _fileName_aboveMean, sep=',', header=False, index=False)
_dfCnt.loc[_dfCnt['counts'] <= _mean].to_csv(_output_dir + "\\" + _fileName_belowMean, sep=',', header=False, index=False)

# Output watch list for TradingView, above mean
_dfWLAboveMean = _dfCnt.loc[_dfCnt['counts'] > _mean]
with open(_output_dir + "\\" + _filename_output_AboveMean, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(_dfWLAboveMean['Symbol'].tolist())

#	Same as _filename_WLAboveMean but with spaces as delims for 
#	correlation analysis on https://www.portfoliovisualizer.com/asset-correlations
with open(_output_dir + "\\" + _filename_output_AboveMean_wsp, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=" ")
    writer.writerow(_dfWLAboveMean['Symbol'].tolist())

# Output watch list for TradingView, below mean
_dfWLBelowMean = _dfCnt.loc[_dfCnt['counts'] <= _mean]
with open(_output_dir + "\\" + _filename_output_BelowMean, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(_dfWLBelowMean['Symbol'].tolist())
