import pytest
import numpy as np
from ie-pandas import dataframe

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the function show row returns the expected list of row values
def check_df_showrow():
    test_df = dataframe(test_data)
    row_list = test_df.showrow(3)
    expected_row_list = f"Row nº3: ['fish', 0, 0, 8, 1.047249, False]"
    assert row_list == expected_row_list