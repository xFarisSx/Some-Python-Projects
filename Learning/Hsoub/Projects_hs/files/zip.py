import zipfile
import os
import shutil

compressZip = zipfile.ZipFile('zipfile1.zip')

# file names
# print(compressZip.namelist())

# to store info object
# fileinfo = compressZip.getinfo('images/video1.jpeg')

# normal file size
# print(fileinfo.file_size)

# compressed file size
# print(fileinfo.compress_size)

# extract here
# compressZip.extractall()

# os.chdir('folder')
# compressZip.extractall()

# extract a specific file
# compressZip.extract('images/video1.jpeg','.')

# compress a file
# newZip = zipfile.ZipFile('new.zip','w')
# newZip.write('images/video1.jpeg')

# compress folder
# folderZip = zipfile.ZipFile('newfolder.zip','w')
# folderZip.write('images')

# compress folder with shutil
# shutil.make_archive('compressedfolder','zip','images')