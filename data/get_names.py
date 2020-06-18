
import pandas as pd
import json

#data = json.load(open('courses.json', 'r'))
#print(data)

df = pd.read_json('courses.json', 'r')
cols = df.columns.tolist()

print(cols)
All_Ai_c = [42634, 42575, 42436, 02282, 02504, 02561,02582,02806,02807, 02809, 02238, 02266, 02454, 02455, 02458, 02506, 02507, 0256202450, 02564, 02565,02614,02808,02823,02826,02840,02841,42081,02504, 02805, 02806, 02285, 02454, 02456, 02460, 02830]
my_AI_courses = [42634, 42575, 42436, 02282, 02450, 02504, 02805, 02806, 02285, 02454, 02456, 02460, 02830,42081 ]

All_Ai_c_str = ''.join(All_Ai_c)
my_AI_courses_str = ''.join(my_AI_courses)

print(All_Ai_c_str)
'''
df = pd.DataFrame(data={"value": })
print(df)
df.to_csv("./courses_DTU.csv", sep=',',index=False)
'''
