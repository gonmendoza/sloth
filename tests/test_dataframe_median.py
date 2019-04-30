import pytest
import numpy as np
from sloth import dataframe

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the function median returns the expected list of values
def check_df_median():
    test_df = dataframe(test_data)
    median_list = test_df.median()
    expected_median_list = ['String col', 4, 0, 2, 0.0, 'String col']
    assert median_list == expected_median_list