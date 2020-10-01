'''
This file automates is a demo that shows some automated utility
for checking library versions

NOTE: The assertions are checked against attributes from the modules for version.
i.e. it is up to the module creator's what attribute they used to store the 
version, so be sure to check the dir(module) to have the correct version 
attribute when checking with automations.
'''
# Check Python >=3.5 (required)
import sys
assert sys.version_info >= (3, 5) #(type(Python2 or Python3), release of that type) so...3.5
# Scikit-Learn >=0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

# Common imports
import numpy as np
import os

# make a {notebook/file}'s output stable across runs
np.random.seed(42)

# To plot pretty figures
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "classification"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def saveFig(figId, tightLayout=True, figExtension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, figId + "." +8 )

