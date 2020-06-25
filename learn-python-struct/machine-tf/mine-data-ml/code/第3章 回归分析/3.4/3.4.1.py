# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
# read csv file directly from a URL and save the results
data = pd.read_csv('./Advertising.csv', index_col=0)

print(data.head())
print(data.tail())
print(data.shape)