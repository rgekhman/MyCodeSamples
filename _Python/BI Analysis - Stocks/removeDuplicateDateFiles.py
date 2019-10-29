#
# Roman Gekhman 
#
#Depends:
#pip install ConfigParser

import glob, os
import socket
import configparser as cfg
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
csv_dir = Config.get('RemoveDuplicateDateFiles', 'csv_dir')
csv_dir = csv_dir.replace('$folder$', _folder)

#_encoding = 'utf-16-le'
os.chdir(csv_dir)

files = glob.glob("*.csv")
files.sort(key=os.path.getmtime)
#print("\n".join(files))

file_cnt = 0
_uniqueDatesSet = set()

#construct list of unique dates 
for file in files:
	_uniqueDatesSet.add(file[:10])
	file_cnt += 1
#print("Processed files : ", file_cnt)

_lstUniqueDates = sorted(list(_uniqueDatesSet))
_deleteFiles = []
_isDateFound = False

for _date in _lstUniqueDates:
	_isDateFound = False
	for file in files:
		if file[:10] == _date:
			if _isDateFound:
				_deleteFiles.append(file)
			else:
				_isDateFound = True

print("Duplicates list:")
#print("\n".join(_deleteFiles))

# remove duplicate files
for file in _deleteFiles:
	print("removing file: {}".format(file))
	os.remove(file)