
import pandas as pd
import json

#data = json.load(open('courses.json', 'r'))
#print(data)

df = pd.read_json('courses.json', 'r')
cols = df.columns.tolist()



#Row1 = ['passpercent', 'avg', 'grades', 'name', 'pp', 'avgp', 'qualityscore', 'workload', 'lazyscore']
#df['index'] = Row1

print(df.head())

#df = pd.DataFrame(data={"c1": avg, 'grades': grades,"passpercent": passpercent, 'name': name, 'pp':pp})

df.to_csv("./c_DTU.csv", sep=',',index=False)
