import pytest
import numpy as np
import sloth

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the function sum returns the expected list of values
def test_df_sum():
    test_df = sloth.dataframe(test_data)
    sum_list = test_df.sum()
    expected_sum_list = ['String col', 18, 2, 30, -0.5612979999999999, 'String col']
    assert sum_list == expected_sum_list