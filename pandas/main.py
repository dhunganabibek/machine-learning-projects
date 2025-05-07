import pandas as pd
import numpy as np


df = pd.read_csv('currency.csv')

for label, row in df.iterrows():
    print(label, row['currency'])