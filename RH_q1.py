import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#github key: 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

df1 = pd.read_csv('../Study/delta_price_symbols_A_to_D.csv',index_col=0)
df2 = pd.read_csv('../Study/delta_price_symbols_E_to_H.csv',index_col=0)
df3 = pd.read_csv('../Study/delta_price_symbol_X.csv',index_col=0)
df3.head()

df = df1.merge(df2, how='inner',on='Date').merge(df3,how='inner',on='Date')
df.head(10)