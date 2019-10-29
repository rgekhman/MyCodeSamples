from  PIL import Image
from pylab import *

def imresize(_im, _size):
	""" Resize an image array using PIL """
	pil_im = Image.fromarray(uint8(_im))
	return array(pil_im.resize(_size))

def histeq(_im, nbr_bins=256):
	""" Histogram equalization of a grayscale image. """

	# Get image histogram
	imhist, bins = histogram(_im.flatten(), nbr_bins, normed=True)
	cdf = imhist.cumsum() #cumulative distribution function 
	cdf = 255 * cdf / cdf[-1] #Normalize

	_im2 = interp(_im.flatten(), bins[:-1], cdf)
	return _im2.reshape(_im.shape), cdf

def compute_average(imlist):
	""" Compute the average of a list of images. """
	# open first image and make into array of type float
	averageim = array(Image.open(imlist[0]), 'f')
	for imname in imlist[1:]:
		try:
			averageim += array(Image.open(imname))
		except:
			print(imname + '...skipped')
		averageim /= len(imlist)
		# return average as uint8
		return array(averageim, 'uint8')
