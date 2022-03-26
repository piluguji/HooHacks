import pandas as pd
import numpy as np

appl = pd.DataFrame()

for stock in ["NVDA/nvda"]:
    for year in range(2020, 2022):
        for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
            
              df = pd.read_csv(stock + "_eod_" + str(year) + str(month) + ".txt") 
              df = df.loc[:, [' [QUOTE_DATE]', ' [UNDERLYING_LAST]', ' [EXPIRE_DATE]', ' [DTE]',' [STRIKE]', ' [C_BID]', ' [C_ASK]']]
              df.columns = ['[QUOTE_DATE]', '[UNDERLYING_LAST]', '[EXPIRE_DATE]', '[DTE]','[STRIKE]', '[C_BID]', '[C_ASK]']
              df = df.replace(r'^\s*$', np.nan, regex=True)
              df.dropna()
              df['[STRIKE]'] = df[df['[STRIKE]'].apply(lambda x: isinstance(x, (int, np.int64)))]
              df['[UNDERLYING_LAST]'] = df['[UNDERLYING_LAST]'].astype('float32')
              df['[DTE]'] = df['[DTE]'].astype('int32')
              df['[STRIKE]'] = df['[STRIKE]'].astype('float32')
              df['[C_BID]'] = df['[C_BID]'].astype('float32')
              df['[C_ASK]'] = df['[C_ASK]'].astype('float32')
              df['[PRICE]'] = (df['[C_BID]'] + df['[C_ASK]'])/2
              df = df.drop(columns=['[C_BID]', '[C_ASK]'])
              print(df)
              appl = appl.append(df)
            
appl.to_csv("NVDA.csv")