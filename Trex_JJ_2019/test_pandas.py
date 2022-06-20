import pandas as pd

df = pd.DataFrame({'ID': [1, 2],
                   'Value_2013': [100, 200],
                   'Value_2014': [245, 300],
                   'Value_2016': [200, float('NaN')]})

print(df)
