#This script helps to unzip the zipfiles

from zipfile import ZipFile

# Create a ZipFile Object and load sample.zip in it
unzip=ZipFile(r'zipfile direcotry')

# Extract all the contents of zip file in different directory
unzip.extractall(r"extract directory")