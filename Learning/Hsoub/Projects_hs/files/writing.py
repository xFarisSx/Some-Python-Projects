from pathlib import Path

myfile = open("folder/file1.txt", 'w')
myfile.write('11. hh')
myfile.write('12. hh')
myfile.writelines(['\n14 333\n','15fff'])
myfile.close()
myfile = open("folder/file1.txt", 'a')
myfile.write('\n11. hh')
myfile.write('\n12. hh')
myfile.writelines(['\n14 333\n','15fff'])
myfile.close()