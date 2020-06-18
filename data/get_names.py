
import pandas as pd
import json

#data = json.load(open('courses.json', 'r'))
#print(data)

df = pd.read_json('courses.json', 'r')
df.head()


'''
df = pd.DataFrame.from_dict(json_str['tags'][0]['results'][0]['values'])
df.columns = ['var1','var2', 'var3']
df.to_csv(filename)
df = pandas.DataFrame(data={"course": })
print(df)
df.to_csv("./A_entries.csv", sep=',',index=False)
'''
