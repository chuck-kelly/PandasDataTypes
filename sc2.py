import pandas as pd
import numpy as np

df = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sales_data_types.csv?raw=True",
                    dtype={'Customer Number':'int'},
                    converters={'2016': lambda x: float(x.replace('$','').replace(',','')),
                                '2017': lambda x: float(x.replace('$','').replace(',','')),
                                'Percent Growth': lambda x: float(x.replace('%', '')) / 100,
                                'Jan Units': lambda x: pd.to_numeric(x , errors='coerce'),
                                'Active': lambda x: np.where( x == 'Y', True, False)
                    })

df['Start_Date'] = pd.to_datetime(df[['Month','Day','Year']])

print(df)