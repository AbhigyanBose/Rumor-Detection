import json
import csv
import os
import pandas as pd

myfile = 'en-scheme-annotations.json'
mydict = {}
with open(
         './'+myfile) as f:
    text = f.read()
    for idx,line in enumerate(text.splitlines()):
        if(line.startswith('{')):
            j_data = json.loads(line)
            try:
                mydict[int(j_data['tweetid'])]=j_data['support']
            except KeyError:
                mydict[int(j_data['tweetid'])]=j_data['responsetype-vs-source']
(pd.DataFrame.from_dict(data=mydict, orient='index')
   .to_csv('dict_file.csv', header=False))
#with open('dict.csv', 'wb') as csv_file:
    #writer = csv.writer(csv_file)
    #for key, value in mydict.items():
       #writer.writerow([str(key), value])
    #j_data = json.load(f)
    #print(j_data)
    #user_data = j_data['user']
    #print(user_data['id'])


