import pandas as pd


All_Ai_c = ['42634', '42575', '42436', '02282', '02504', '02561','02582','02806','02807', '02809', '02238', '02266', '02454', '02455', '02458', '02506', '02507', '02562', '02564', '02565','02614','02808','02823','02826','02840','02841','42081','02504', '02805', '02806', '02285', '02454', '02456', '02460', '02830']
my_AI_courses = ['42634', '42575', '42436', '02282', '02450', '02504', '02805', '02806', '02285', '02454', '02456', '02460', '02830','42081' ]

df = pd.read_csv('c_DTU.csv', skipinitialspace=True, usecols=my_AI_courses)
df_1 = pd.read_csv('c_DTU.csv', skipinitialspace=True, usecols=All_Ai_c)

# See the keys
print(df)
df.to_csv("./My_courses.csv", sep=',',index=False)
df_1.to_csv("./All_Ai_c.csv", sep=',',index=False)
