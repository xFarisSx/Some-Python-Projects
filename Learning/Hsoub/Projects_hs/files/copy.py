import shutil
from pathlib import Path

# shutil.copy('folder/file1.txt', 'folder2/file1.txt')
shutil.copytree('folder', 'folder2')