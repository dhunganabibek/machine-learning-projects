import pandas as pd
import numpy as np


df = pd.read_csv('currency.csv')

is_true = [False] * 163
is_true[0] = True
is_true_series = pd.Series(is_true) 


print(df[is_true_series])