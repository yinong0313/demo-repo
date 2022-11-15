# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df1 = pd.read_csv('../Study/delta_price_symbols_A_to_D.csv',index_col=0)
df2 = pd.read_csv('../Study/delta_price_symbols_E_to_H.csv',index_col=0)
df3 = pd.read_csv('../Study/delta_price_symbol_X.csv',index_col=0)
df3.head()