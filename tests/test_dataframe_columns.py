import pytest
import numpy as np
from sloth import dataframe

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}
        
# Check the function df.colums returns the expected list of column names
def check_df_columns():
    test_df = dataframe(test_data)
    col_list = list(test_df.columns)
    expect_col_list = ['species','num_legs','num_wings','num_specimen_seen','statistics','mammal']
    assert col_list == expect_col_list
