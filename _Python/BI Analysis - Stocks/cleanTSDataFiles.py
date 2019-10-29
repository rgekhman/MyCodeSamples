#
# Roman Gekhman 
#
#Depends:
#pip install configparser, codecs, argparse

import configparser as cfg
import glob, os
import socket
import codecs
import argparse 

_host = socket.gethostname()

#get folder to scan
parser = argparse.ArgumentParser()  
# ex: --folder 
parser.add_argument("--folder", "-f", type=str, required=True)
args = parser.parse_args()
_folder = args.folder

# get config settings
curr_dir = os.path.dirname(os.path.realpath(__file__))
Config = cfg.ConfigParser()
#Config._interpolation = cfg.ExtendedInterpolation()
Config.read(curr_dir + "\\config.ini")
csv_dir = Config.get('CleanTSDataFiles', 'csv_dir')
csv_dir = csv_dir.replace('$folder$', _folder)

_encoding = 'utf-16-le'
os.chdir(csv_dir)
file_cnt = 0
for file in glob.glob("*.csv"):
	fstr = ""
	file_cnt += 1
	with codecs.open(file, encoding=_encoding) as fr:
		for line in fr:
			if "Powered by TradeStation" not in line:
				fstr += line.replace("\r\n","\n")
	
	with codecs.open(file,'w',encoding=_encoding) as f:
		f.write(fstr)

print("Processed files : ", file_cnt)

