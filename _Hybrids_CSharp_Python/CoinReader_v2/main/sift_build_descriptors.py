# 
# Roman Gekhman
# 
#pip install Pillow

from PIL import Image 
from timeit import default_timer as timer
import os
from pylab import * 
import sift
import argparse 
import time
#from os import system

def main():
	try:
		parser = argparse.ArgumentParser()  
		# ex: --denomination 25
		parser.add_argument("--denomination", "-d", type=str, required=True)
		# ex: --imagetype _scenes
		parser.add_argument("--imagetype", "-ir", type=str, required=True)
		args = parser.parse_args()

		_denomination = args.denomination

		_isModels = args.imagetype == 'models' or args.imagetype == 'model'

		_root_folder = '_img\\_scenes\\_' + _denomination

		if _isModels:
			_root_folder = '_img\\_models\\_' + _denomination

		_sift_folder = _root_folder + '\\_sift'
		_features_folder = _root_folder + '\\_features'

		if not os.path.exists(_sift_folder):
			os.makedirs(_sift_folder)

		if not os.path.exists(_features_folder):
			os.makedirs(_features_folder)

		print("Creating descriptos for the models in folder {}\n".format(_root_folder))

		start = time.time()

		for _fileName in os.listdir(_root_folder):
			if _fileName.lower().endswith(".jpg") or _fileName.lower().endswith(".png"): 

				_start = timer()
				_l1 = sift.create_descriptors(_fileName, _root_folder, _sift_folder)
				_elapsed_time = timer() - _start
				print("Time spent on reading features of {} : {}".format(_fileName, _elapsed_time))
		
				print("Plotting and saving image ==> {}".format(_features_folder + '\\' + _fileName))
				_start = timer()
				sift.save_feature_image(_fileName, _l1, _features_folder, _root_folder)
				_elapsed_time = timer() - _start
				print("Time spent plotting and saving image .. ", _elapsed_time)

		end = time.time()
		print("\n+++ Elapsed time: {}\n".format(end - start))
		#input("Press Enter to continue...")
	except Exception as ex:
		print ("Error : ", ex.args)

main()


