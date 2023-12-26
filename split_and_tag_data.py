# 'dataset' holds the input data for this script
from random import sample
import pandas as pd
import numpy as np
import random
random.seed(0)
total_rows = max(dataset['row_no'])
train_rows = int(np.floor(total_rows * 0.8))
test_rows = total_rows - train_rows

train_row_no = random.sample(sorted(dataset['row_no'].values), train_rows)
train_test = []
for row in dataset['row_no']:
    if row in train_row_no:
        train_test.append('Train')
    else:
        train_test.append('Test')
dataset['Train/Test'] = pd.Series(train_test) #Label the rows as either train or test