import boto
import pandas as pd
import numpy as np
import gzip
import sys,os
import fnmatch

import json
import itertools

access_key = '' #enter S3 access key
secret_key = '' #enter S3 secret key
dirpath = ('c:\\temp') #enter to desired local path
if not os.path.exists(dirpath):
    os.makedirs(dirpath)

#create connection to S3
conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        #host = 'objects.dreamhost.com',
        #is_secure=False,               # uncomment if you are not using ssl
        #calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

#from the connection list all files (keys) available for the selected bucket
bucket = conn.get_bucket('')

#use to copy multiple matching files to local directory
k = bucket.list(prefix='')
for x in k:
    try:
        if x.key.endswith('.gz'):
            basename = os.path.basename(x.name.split('/')[-1])
            path = os.path.join(dirpath, "%s" % basename)
            x.get_contents_to_filename(path)
            print ("wrote %s" % path)
    except:
        print (x.key +":"+"FAILED")


#use to decompress the selected file(s)
for f in os.listdir(dirpath):
    if fnmatch.fnmatch(f, 'filename*'):
        zipfile = gzip.open(dirpath + f, 'rb') # open the file
        data = zipfile.read() # get the decompressed data
        newfilepath = (dirpath + f + '.decompressed') # assuming the filepath ends with .bz2
        with open(newfilepath, 'wb') as new_file:
            new_file.write(data)# write a uncompressed file
            new_file.close()
        print ("decompressed %s" % f)
		

#use to parse out specific attributes and values from each file
def lines_per_n(f, n):
    for line in f:
        yield ''.join(itertools.chain([line], itertools.islice(f, n - 1)))

dirpath = ('c:\\temp') 

parse_json = []
for f in os.listdir(dirpath):
    if fnmatch.fnmatch(f, 'filename*' + '.decompressed'):
#        print (f)
 
        with open(dirpath + f) as file_:
            for chunk in lines_per_n(file_, 1):
                jfile = json.loads(chunk)
                vehicle_type = ''
                for item in jfile['data']['reports']:
                    if 'type' in item['measurements'][0].keys():
                        vehicle_type = item['measurements'][0]['type']
                    parse_json.append({
                    'sensorId': item['identity']['sensorId']
                    ,'coordinates': item['measurements'][0]['location']['coordinates']
                    ,'heading': item['measurements'][0]['location']['heading']
                    ,'speed': item['measurements'][0]['location']['speed']
                    ,'captureTime': item['measurements'][0]['observationTime']
                    ,'vehicleType': vehicle_type
                    })
#                    print (item)

#print parse_json

data_df = pd.DataFrame(parse_json) #,columns=['sensorId','temp','coordinates','heading','speed','captureTime']
data_df['lon'] = data_df.coordinates.apply(lambda x: x[0])
data_df['lat'] = data_df.coordinates.apply(lambda x: x[1])
#data_df.to_csv('xfcd_data_combined.csv') #save output