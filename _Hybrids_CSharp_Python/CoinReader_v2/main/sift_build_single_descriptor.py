# 
# Roman Gekhman
# 
from PIL import Image 
from numpy import * 
from pylab import * 
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import os
import sift
import argparse 

try:
	parser = argparse.ArgumentParser()   
	# ex: --filename 25_1956_2.jpg
	parser.add_argument("--filename", "-f", type=str, required=True)
	
	# ex: --denomination 25
	parser.add_argument("--denomination", "-d", type=str, required=False)

	# ex: --imagetype _scenes
	parser.add_argument("--imagetype", "-ir", type=str, required=True)
	args = parser.parse_args()
	
	#print(args)
	#print(os.getcwd())

	_fileName = args.filename #'scene1.jpg'
	
	_denomination = args.denomination
	if not _denomination: 
		_denomination = _fileName[0:2]

	_imagetype = args.imagetype

	_fileNameNoExt, _fileExtension = os.path.splitext(_fileName)
	_root_folder = os.getcwd() + '\\_img\\' + _imagetype + '\\_' + _denomination
	_sift_folder = _root_folder + '\\_sift'
	_features_folder = _root_folder + '\\_features'

	_image_path = _root_folder + '\\' + _fileName
	_image_sift = _sift_folder + '\\' + _fileNameNoExt + '.sift'

	print(_image_path)

	im1 = array(Image.open(_image_path ).convert('L')) 

	if not os.path.exists(_sift_folder):
		os.makedirs(_sift_folder)

	if not os.path.exists(_features_folder):
		os.makedirs(_features_folder)

	_start = timer()

	_l1 = sift.create_descriptors(_fileName, _root_folder, _sift_folder)

	_elapsed_time = timer() - _start
	print("Time spent reading features", _elapsed_time)

	print("Plotting and saving image ...")
	_start = timer()
	sift.save_feature_image(_fileName, _l1, _features_folder, _root_folder)
	_elapsed_time = timer() - _start
	print("Time spent plotting and saving image .. ", _elapsed_time)

except Exception as ex:
	print ("Error : ", ex.args)