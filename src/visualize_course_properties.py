import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


#read data out of different label csv file, which has been manaually created
#label_text = pd.read_csv("labels.csv")

#Read the entire data from the csv file and do filtering
df = pd.read_csv('My_courses.csv')

#counting the index

multy_id = df.index
multy_id = np.array(multy_id, dtype=float)

#setting the style for better overwiew
sns.set(style="whitegrid")



print(multy_id)
# way
