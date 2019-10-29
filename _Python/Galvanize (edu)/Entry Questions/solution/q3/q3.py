import csv 
import numpy.random as npr
import matplotlib.pyplot as plt

#common vars
_strVQIdx = "'Viewer Quotes Index'"
_lstHeader = ["Bucket","Quotes","Views"]

#CASE 1
with open("out_data.csv", 'w', newline='') as outfile:
	outWriter = csv.writer(outfile, delimiter=',')
	with open("in_data.csv", 'r') as infile:
		inReader = csv.reader(infile, delimiter=',')
		for line in inReader:
			line = [x.strip(' ') for x in line]
			if line == _lstHeader:
				outfile.write("CASE 1: \n")
				outfile.write("\nOutput: \n")
				line.append(_strVQIdx)
				outWriter.writerow(line)
				continue
			else:
				try: 
					_ratio = round(int(line[1])/int(line[2]), 3)
					print(line[0], int(line[1]), int(line[2]), _ratio)
					line.append(_ratio)
					outWriter.writerow(line)
				except Exception as ex:
					print("Error in line : ", ex.args[0])

	#CASE 2
	with open("in_data.csv", 'r') as infile:
		inReader = csv.reader(infile, delimiter=',')
		_avgViewsPerViewer = 1.75
		for line in inReader:
			line = [x.strip(' ') for x in line]
			if line == _lstHeader:
				outfile.write("\n")
				outfile.write("CASE 2: \n")
				outfile.write("Assume avg N of form views per viewer = {}\n".format(_avgViewsPerViewer))
				outfile.write("\nOutput: \n")
				line.append(_strVQIdx)
				outWriter.writerow(line)
				continue
			else:
				try: 
					_ratio = round(int(line[1])/ (int(line[2]) / _avgViewsPerViewer), 3)
					print(line[0], int(line[1]), int(line[2]), _ratio)
					line.append(_ratio)
					outWriter.writerow(line)
				except Exception as ex:
					print("Error in line : ", ex.args[0])

	##CASE 3
	#with open("in_data.csv", 'r') as infile:
	#	inReader = csv.reader(infile, delimiter=',')
	#	for line in inReader:
	#		line = [x.strip(' ') for x in line]
	#		if line == _lstHeader:
	#			outfile.write("\n")
	#			outfile.write("CASE 3: \n")
	#			outfile.write("\nOutput: \n")
	#			line.append(_strVQIdx)
	#			line.append("'Avg N of Views per Viewer'")
	#			outWriter.writerow(line)
	#			continue
	#		else:
	#			try: 
	#				_avgViewsPerViewer2 = round(npr.uniform(0.5, 10),2)
	#				_ratio = round(int(line[1])/ (int(line[2]) / _avgViewsPerViewer2), 3)
	#				print(line[0], int(line[1]), int(line[2]), _ratio)
	#				line.append(_ratio)
	#				line.append(_avgViewsPerViewer2)
	#				outWriter.writerow(line)
	#			except Exception as ex:
	#				print("Error in line : ", ex.args[0])