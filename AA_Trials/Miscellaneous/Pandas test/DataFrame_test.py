import pandas as pd
import numpy as np

# # Series
# s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# print(s)
# print(s.index)
# s_1 = pd.Series(np.random.randn(5))     # if we give no indexes it gives them starting from 0
# print(s_1)
# s_2 = pd.Series(5.0, index=["a", "b", "c", "d", "e"])   # all the values connected to the indexes are 5.0
# print(s_2)

# # Series from dict
# d = {"b": 1, "a": 0, "c": 2}    # b, a, c are the indexes of the series
# print(pd.Series(d))
# print(pd.Series(d, index=["b", "c", "d", "a"]))     # here the index "d" has no corresponding value, thus it puts NaN

# # Series operations
# s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# print(s)
# print(s[0])     # it prints the first value
# print(s[:3])    # it prints the first 3 values, it also prints the corresponding indexes
# print(s[s > s.median()])     # it prints the values and corresponding indexes in the series that fulfill the statement
# print(s[[4, 3, 1]])     # it prints the values and corresponding indexes of the elements (fifth, fourth and second)
# print(np.exp(s))    # it prints the series with the same indexes and the values are e^value
# # We can access the actual array backing a Series, use Series.array
# print(s.array)  # it creates an array with all the values only of the series, without the indexes
# # We can convert into an actual ndarray, then use Series.to_numpy()
# print(s.to_numpy())     # it creates an ndarray

# # Series is dict like
# s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# print(s)
# print(s["a"])   # we can call the values in the series just like a dict by calling the corresponding index
# s["e"] = 12.0   # we assign at the index e the value 12.0
# print(s)
# print("e" in s)     # returns True since e is an index
# print("f" in s)     # returns False since f is not an index
# print(s.get("f"), np.nan)   # returns the value corresponding to the index, if there is no index returns NaN

# # Vectorized operations and labels alignment with Series
# s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# print(s)
# print(s + s)    # we sum the values of the two series
# print(s * 2)    # we multiply every values by two
# # A key difference between Series and ndarray is that operations between Series automatically align the data based on
# # label. We can sum unaligned Series
# print(s[1:] + s[:-1])   # we are summing the last four with the first four, we get two NaN since the first and last are not summed
# # We can name the Series
# s = pd.Series(np.random.randn(5), name="something")
# print(s)
# print(s.name)
# s2 = s.rename("different")  # we are creating a new series with a different name
# print(s2.name)

# # Dataframe
# # from dict of Series or dicts
# d = {
#     "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
#     "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"])
# }
# df_1 = pd.DataFrame(d)          # table with first column "one", and second column "two", the indexes are the rows
# df_2 = pd.DataFrame(d, index=["d", "b", "a"])     # recreates a new DataFrame with the indexes selected, if they don't exist it puts NaN
# df_3 = pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])   # recreates a new DataFrame with specified columns, if not it creates them and populates them with Nan
# print(df_1)
# print(df_2)
# print(df_3)
# print(df_1.index)     # it prints the indexes of the dataframe
# print(df_1.columns)   # it prints the columns of the dataframe

# # From dict of ndarrays / lists
# d = {
#     "one": [1.0, 2.0, 3.0, 4.0],
#     "two": [4.0, 3.0, 2.0, 1.0]
# }
# print(pd.DataFrame(d))  # we created a dataframe from a dict
# print(pd.DataFrame(d, index=["a", "b", "c", "d"]))      # we created a dataframe from a dict and changed the indexes

# # From a list of dict
# data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
# print(pd.DataFrame(data2))  # from a list of dict, the element in the list are the rows, with the columns are each element of the dict
# print(pd.DataFrame(data2, index=["first", "second"]))   # same as above but changing the index names
# print(pd.DataFrame(data2, columns=["a", "b"]))      # we create a dataframe with just the columns a and b

# # From a dict of tuples (we create a MultiIndexed frame by passing a tuples dictionary
# data3 = pd.DataFrame(
#     {
#         ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},     # a is the first level column, b is the second level column
#         ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},     # A is the first level index, C is the second level index
#         ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
#         ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
#         ("b", "b"): {("A", "D"): 9, ("A", "B"): 10},
#     }
# )
# print(data3)

# Columns selection, addition, deletion
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"])
}
df = pd.DataFrame(d)
print(df["one"])        # this is a Series
df["three"] = df["one"] * df["two"]     # created a third column with values equal to the product of the first two
df["flag"] = df["one"] > 2      # created a fourth column named flag that returns True or False based on the statement
print(df)
df["foo"] = "bar"
print(df)       # we created a fifth column named foo populated all with "bar"
df["one_trunc"] = df["one"][:2]
print(df)   # when we insert a series that is truncated, it auto fills with NaN
df.insert(2, "ins", df["one"])
print(df)       # inserted a column in third position with name ins and value equal to column "one"
# Row selection
print(df.loc["b"])      # it returns a Series with index the column names and values the values of the row b
print(df.iloc[2])       # it returns the second row as a Series
