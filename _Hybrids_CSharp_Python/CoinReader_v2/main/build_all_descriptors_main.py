# 
# Roman Gekhman
# 
import os 

# rebuild models
os.system("sift_build_descriptors.py --denomination 25 --imagetype model")
os.system("sift_build_descriptors.py --denomination 10 --imagetype model")
os.system("sift_build_descriptors.py --denomination 05 --imagetype model")
os.system("sift_build_descriptors.py --denomination 01 --imagetype model")

#rebuild scenes
os.system("sift_build_descriptors.py --denomination 25 --imagetype scenes")
os.system("sift_build_descriptors.py --denomination 01 --imagetype scenes")
