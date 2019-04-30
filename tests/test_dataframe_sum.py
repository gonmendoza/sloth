import pytest
import numpy as np
from sloth import dataframe

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the function sum returns the expected list of values
def check_df_sum():
    test_df = dataframe(test_data)
    sum_list = test_df.sum()
    expected_sum_list = ['String col', 18, 2, 21, -0.8375299999999999, 'String col']
    assert sum_list == expected_sum_list