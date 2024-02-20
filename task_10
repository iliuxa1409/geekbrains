import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

"""
data.loc[data['whoAmI'] == 'human', 'human'], data.loc[data['whoAmI'] != 'human', 'human'] = '1', '0'
data.loc[data['whoAmI'] == 'robot', 'robot'], data.loc[data['whoAmI'] != 'robot', 'robot'] = '1', '0'
del data['whoAmI']
"""

unique_values = data['whoAmI'].unique()
print(unique_values)
for value in unique_values:
    data[value] = int(data['whoAmI'] == value).astype(int)
    print(data)
data.drop(columns=['whoAmI'], inplace=True)
