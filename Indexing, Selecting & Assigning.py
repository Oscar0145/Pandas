#Lesson 2
import pandas as pd



reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews.head())

#1.
desc = reviews.description

#2.
first_description = desc.iloc[0]

#3.
first_row = reviews.iloc[0]

#4.
first_descriptions = desc.iloc[:10]

#5.
sample_reviews = reviews.iloc[[1,2,3,5,8]]

#6.
df = reviews.loc[[0,1,10,100],['country','province','region_1','region_2']]

#7.
df = reviews.loc[:99,['country','variety']]

#8.
italian_wines = reviews.loc[reviews.country == 'Italy']

#9.
top_oceania_wines = reviews.loc[reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)]
