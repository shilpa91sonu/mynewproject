import pandas as pd
import math

data = {'area': ['new-hills', 'cape-town', 'mumbai'],
        'rainfall': [100, 70, 200],
        'temperature': [20, 25, 39]}

df = pd.DataFrame.from_dict(data)
print(df)
data = [{'area': 'new-hills', 'rainfall': 100, 'temperature': 20},
        {'area': 'cape-town', 'rainfall': 70, 'temperature': 25},
        {'area': 'mumbai', 'rainfall': 200, 'temperature': 39}]

df = pd.DataFrame.from_dict(data)
print(df)
