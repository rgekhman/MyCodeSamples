# 
# Roman Gekhman
# 
import sift
import os
from numpy import *
import argparse 
import json
#import numba 
#from numba import jit


#def main():
try:
	parser = argparse.ArgumentParser()   
	# ex: --filename 25_1956_2.jpg
	parser.add_argument("--filename", "-f", type=str, required=True)
	
	# ex: --denomination 25
	parser.add_argument("--denomination", "-d", type=str, required=False)

	args = parser.parse_args()

	#init params
	_sceneFileName = args.filename #'scene1.jpg'
	if not _sceneFileName:
		print("Please select Input File")
		exit() 

	_sceneFileName, _sceneFileExt = os.path.splitext(_sceneFileName)

	_denomination = args.denomination
	if not _denomination: 
		_denomination = _sceneFileName[0:2]

	if	_denomination != '01' and \
		_denomination != '05' and \
		_denomination != '10' and \
		_denomination != '25':
		print("File name should start with denomination  (01, 05, 10, 25)")
		exit() 

	_root_models_folder = '_img\\_models\\_' + _denomination
	_sift_models_folder = _root_models_folder + '\\_sift'

	_root_scenes_folder = '_img\\_scenes\\_' + _denomination
	_sift_scenes_folder = _root_scenes_folder + '\\_sift'

	imlist = [_sift_scenes_folder + '\\' + _sceneFileName + '.sift']
	featlist = []

	#nbr_images = len([name for name in os.listdir(_sift_models_folder) if os.path.isfile(name)])
	#for _fileName in os.listdir(_root_models_folder):
	#	if os.path.isfile(_root_models_folder + '\\' + _fileName):
	#		imlist.append(_fileName)

	for _fileName in os.listdir(_sift_models_folder):
		if os.path.isfile(_sift_models_folder + '\\' + _fileName):
			featlist.append(_sift_models_folder + '\\' + _fileName)

	nbr_model_images = len(featlist)
	nbr_scene_images = 1	#len(imlist)

	matchscores = zeros((nbr_scene_images,nbr_model_images))

	good_results = {}

	for i in range(nbr_scene_images):
		for j in range(i,nbr_model_images): # only compute upper triangle
			#print('comparing ', imlist[i], featlist[j])
			l1,d1 = sift.read_features_from_file(imlist[i])
			l2,d2 = sift.read_features_from_file(featlist[j])
			matches = sift.match_twosided(d1,d2)
			nbr_matches = sum(matches > 0)
			#print('number of matches = ', nbr_matches)

			_fName = os.path.basename(featlist[j]).split('.')[0]
			_vals = _fName.split('_')
			matchscores[i,j] = nbr_matches
			if nbr_matches > 0:
				good_results['Denomination : ' + _vals[0]] = "Year : " + _vals[1]

	#with open(outputfilename, 'wb') as outfile:
	if len(good_results) > 0:
		print("Found: " + json.dumps(good_results))
	else:
		print("No matches found")
	# copy values
	#for i in range(nbr_images):
	#	for j in range(i+1,nbr_images): # no need to copy diagonal
	#		matchscores[j,i] = matchscores[i,j]
except Exception as ex:
	print ("Error : ", ex.args)

#main()