import gzip
import sys,os
import fnmatch

dirpath = "c:\\temp\\BR\\2016\\06\\06\\"

#use to decompress the selected file(s)
for f in os.listdir(dirpath):
    if fnmatch.fnmatch(f, '*drivers-taxi_position*'):
        zipfile = gzip.open(dirpath + f, 'rb') # open the file
        data = zipfile.read() # get the decompressed data
        newfilepath = (dirpath + f + '.decompressed') # assuming the filepath ends with .bz2
        with open(newfilepath, 'wb') as new_file:
            new_file.write(data)# write a uncompressed file
            new_file.close()
        print "decompressed %s" % f
        
print "decompress files complete"
        
#use to copy multiple files to one merged file
import os
os.chdir('c:\\temp\\BR\\2016\\06\\06\\')
os.system('copy *.decompressed drivers-taxi_position_BR.json')

print "file merge complete"

#use to view X characters from beginning of file (quick validation)
f = open('c:\\temp\\BR\\2016\\06\\06\\drivers-taxi_position_BR.json', 'r')
f.read(1000)