import pandas as pd
import re

df = pd.read_csv('output/result.csv')

 
def replace_non_numeric(value):
    
    if isinstance(value, str) and not re.match(r'^\d', value):
        return '' 
    return value

 
df['result'] = df['result'].apply(replace_non_numeric)


df.to_csv('output/finalresult.csv', index=False)
