import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import numpy as np




#Read the entire data from the csv file and do filtering
df = pd.read_csv('My_courses.csv')
x_axis = df.columns
t = df['avg'] = df['avg'].astype('float')

avg_g = df[df['cate'] =='avg']
sns.set(style="whitegrid")
print(t, avg_g, x_axis)
# way

f = sns.catplot(x=x_axis, y='02282',
                height=5, aspect=2.5,
                kind='point',
                palette=sns.color_palette('Set1',n_colors=9),
                data=df)
plt.show()
