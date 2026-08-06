#Data Types and Missing Values
import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

#The data type for a column in a DataFrame or a Series is known as the dtype.
print(reviews.dtypes)

# we may transform the points column from its existing int64 data type into a float64 data type
print(reviews.points.astype('float64'))

#Entries missing values are given the value NaN
#To select NaN entries you can use pd.isnull()
print(reviews[pd.isnull(reviews.country)])

#Replacing missing values is a common operation
#fillna() provides a few different strategies for mitigating such data. For example, we can simply replace each NaN with an "Unknown"
print(reviews.region_2.fillna("Unknown"))

#Alternatively, we may have a non-null value that we would like to replace
print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))

#Exercises
#1. What is the data type of the points column in the dataset?
dtype = reviews.points.dtypes

#2. Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in native Python.
point_strings = reviews.points.astype('str')

#3. Sometimes the price column is null. How many reviews in the dataset are missing a price?
n_missing_prices = len(reviews[pd.isnull(reviews.price)])

#4. What are the most common wine-producing regions? Create a Series counting the number of times each value occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown. Sort in descending order.
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
