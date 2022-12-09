import os
from pathlib import Path

print(os.getcwd())
os.chdir(r'..')
print(os.getcwd())
print(Path.home())
myfile = open("files/folder2/file1.txt","r")

print(myfile.name)
print(myfile.mode)

print(myfile.readlines())
#print(myfile.read(9))
#print(myfile.readline(9))
# print(myfile.readlines())
# lines = myfile.readlines()
# print(lines[:5])

myfile.close()