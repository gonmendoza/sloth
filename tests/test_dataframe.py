import numpy as np
from ie-pandas import dataframe

test_data = {'species':['falcon', 'dog', 'spider', 'fish', 'cat'],
                'num_legs': [2, 4, 8, 0, 4],
                'num_wings': [2, 0, 0, 0, 0],
                'num_specimen_seen': [10, 2, 1, 8, 9],
                'statistics':[-1.509059, 0.119209, -0.494929, 1.047249, 0.276232],
                'mammal': [False, True, False, False, True]}

# Check the function df["col_name"] returns NumPy arrays
def check_df_nparray():
    test_df = dataframe(test_data)
    for array in test_df.columns:
        assert isinstance(test_df[array], np.ndarray)

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
        
# Check the function df.colums returns the expected list of column names
def check_df_columns():
    test_df = dataframe(test_data)
    col_list = list(test_df.columns)
    expect_col_list = ['species','num_legs','num_wings','num_specimen_seen','statistics','mammal']
    assert col_list == expect_col_list
    
# Check the function show row returns the expected list of row values
def check_df_showrow():
    test_df = dataframe(test_data)
    row_list = test_df.showrow(3)
    expected_row_list = f"Row nº3: ['fish', 0, 0, 8, 1.047249, False]"
    assert row_list == expected_row_list
    
# Check the function sum returns the expected list of values
def check_df_sum():
    test_df = dataframe(test_data)
    sum_list = test_df.sum()
    expected_sum_list = ['String col', 18, 2, 21, -0.8375299999999999, 'String col']
    assert sum_list == expected_sum_list
    
# Check the function mean returns the expected list of values
def check_df_mean():
    test_df = dataframe(test_data)
    mean_list = test_df.mean()
    expected_mean_list = ['String col', 3.6000000000000005, 0.4, 4.2, -0.16750599999999993, 'String col']
    assert mean_list == expected_mean_list
    
# Check the function median returns the expected list of values
def check_df_median():
    test_df = dataframe(test_data)
    median_list = test_df.median()
    expected_median_list = ['String col', 4, 0, 2, 0.0, 'String col']
    assert median_list == expected_median_list
    
# Check the function min returns the expected list of values
def check_df_min():
    test_df = dataframe(test_data)
    min_list = test_df.min()
    expected_min_list = ['cat', 0, 0, 1, -1.509059, False]
    assert min_list == expected_min_list

# Check the function max returns the expected list of values
def check_df_max():
    test_df = dataframe(test_data)
    max_list = test_df.max()
    expected_max_list = ['monkey', 8, 2, 9, 1.047249, False]
    assert max_list == expected_max_list