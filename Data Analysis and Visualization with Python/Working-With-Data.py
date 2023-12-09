import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Write user defined functions to perform repetive tasks
def generate_random_list(size):
    generated_list = []
    for i in range(0, size):
        random_num = random.randint(1, 100)
        generated_list.append(random_num)
    return generated_list

# Create and manipulate numpy arrays
np_array = np.array(generate_random_list(100))
np_shape = np_array.shape # (1, 100)
np_transposed = np_array.T # np_array transposed (X axis becomes Y axis and vice versa)
np_resized = np.resize(np_array, (1, 50)) # resize the array to be 1x50
np_resized_shape = np_resized.shape # (1, 50)

# Create and manipulate pandas series
pd_series = pd.Series(generate_random_list(100))
pd_added = pd_series.add(pd.Series(generate_random_list(100))) # add two series element-wise ([1,1] + [1,1] = [2,2])
pd_count = pd_series.count() # get size of series
pd_sorted = pd_series.sort_values() # sort the series (defaults to ascending)

# Create and manipulate dataframes
df = pd.DataFrame({"ints_1": generate_random_list(100), "ints_2": generate_random_list(100)}) # create a df with 100 random ints and name the column "ints"
df_sum = df["ints_1"].sum() # the sum of every value in the df
pd_filled = df["ints_1"].fillna(0) # replace every NaN in the df with 0
pd_replaced = df["ints_1"].replace(50, 77) # replace every occurrence of 50 in the df with 77
pd_sample = df["ints_1"].sample(n=10, random_state=1) # returns a 10-value sample from the array

# Describe how to index and "type" pandas Series and DataFrames
# pandas series can be indexed in three ways: .loc, .iloc, []
#     - .loc takes a label, such as 1 or "a" ("a" only works if the values have keys i.e set)
#     - .iloc takes an index/position, such as 1, [1, 2, 3], [1:7]
#     - [] works similarly as regular lists/sets
# pandas series can by "typed" by accessing the dtype property of the series or with type()
#     - Series.dtype or type(Series)
# pandas dataframes can be indexed in the same way as series, but are inherently multi-dimensional
#     - the methods from pd series work, but will return the column
#     - to access a specific element from a specific column, access the column, then use [] to select
#         - DataFrame.loc["ints_2"][0]
# pandas dataframes can be indexed by either dtypes or by calling type on each col
#     - DataFrame.dtypes (returns list of types - each col could have a diff type)
#     - type(DataFrame.loc["ints_2"]) (returns the type of this specific col)

# Create histograms and scatter plots for basic exploratory analysis
hist_data = pd.Series(generate_random_list(100))
hist_data.plot.hist(bins=10)
plt.title("Histogram")
plt.show()

scatter_data = pd.DataFrame({"x": generate_random_list(100), "y": generate_random_list(100)})
scatter_data.plot.scatter(x="x", y="y")
plt.title("Scatter Plot")
plt.show()