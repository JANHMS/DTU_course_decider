
import pandas as pd
import json

#data = json.load(open('courses.json', 'r'))
#print(data)

df = pd.read_json('courses.json', 'r')
cols = df.columns.tolist()
print(df.head())
print(cols)

#All_Ai_c_str = ''.join(All_Ai_c)
#my_AI_courses_str = ''.join(my_AI_courses)
#print(All_Ai_c)


#df = pd.DataFrame(data={"c1": avg, 'grades': grades,"passpercent": passpercent, 'name': name, 'pp':pp})
df.to_csv("./c_DTU.csv", sep=',',index=False)
