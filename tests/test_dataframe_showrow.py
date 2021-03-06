import pytest
import numpy as np
import sloth

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the function show row returns the expected list of row values
def test_df_showrow():
    test_df = sloth.dataframe(test_data)
    row_list = test_df.showrow(3)
    expected_row_list = ['fish', 0, 0, 8, 1.047249, False]
    assert row_list == expected_row_list