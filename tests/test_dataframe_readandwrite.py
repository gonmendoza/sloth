import pytest
import numpy as np
from sloth import dataframe

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the dataframe function allows modification
def check_df_read_write():
    test_df = dataframe(test_data)
    test_df['species'] = ['falcon', 'dog', 'monkey', 'fish', 'cat']
    test_df['num_specimen_seen'][0] = 1
    test_df['statistics'][4] = 0
    test_df['mammal'] = [False, False, False, False, False]
    
    expected_df = dataframe({'species':['falcon', 'dog', 'monkey', 'fish', 'cat'],
                                'num_legs': [2, 4, 8, 0, 4],
                                'num_wings': [2, 0, 0, 0, 0],
                                'num_specimen_seen': [1, 2, 1, 8, 9],
                                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0],
                                'mammal': [False, False, False, False, False]})
    for array in test_df.columns:
        assert np.array_equiv(test_df[array], expected_df[array])