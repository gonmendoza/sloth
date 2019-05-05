import pytest
import numpy as np
import sloth

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the function max returns the expected list of values
def test_set_item():
    test_df = sloth.dataframe(test_data)
    test_df["num_legs"] = 2
    expected_column2 = np.array([2, 2, 2, 2, 2])
    assert all(test_df["num_legs"] == expected_column2)