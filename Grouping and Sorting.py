import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)


print(reviews.groupby('points').points.count())

#groupby() created a group of reviews which allotted the same point values to the given wines.
#Then, for each of these groups,
#we grabbed the points() column and counted how many times it appeared.
#value_counts() is just a shortcut to this groupby() operation.

#We can use any of the summary functions we've used before with this data.
#For example, to get the cheapest wine in each point value category, we can do the following:
print(reviews.groupby('points').price.min())

#one way of selecting the name of the first wine reviewed from each winery in the dataset:
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

#here's how we would pick out the best wine by country and province:
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))

#Another groupby() method worth mentioning is agg()
#lets you run a bunch of different functions on your DataFrame simultaneously
#we can generate a simple statistical summary of the dataset
print(reviews.groupby(['country']).price.agg([len, min, max]))

#A multi-index differs from a regular index in that it has multiple levels.
#For example:

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)
mi = countries_reviewed.index
print(type(mi))

#multi-index method you will use most often is the one for converting back to a regular index
#reset_index() method:
print(countries_reviewed.reset_index())

#To get data in the order want it in we can sort it ourselves. The sort_values() method is handy for this.
countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by='len'))

#sort_values() defaults to an ascending sort
#we want a descending sort, where the higher numbers go first. That goes thusly:
print(countries_reviewed.sort_values(by='len', ascending=False))

#To sort by index values, use the companion method sort_index(). This method has the same arguments and default order:
print(countries_reviewed.sort_index())

#Finally, know that you can sort by more than one column at a time:
print(countries_reviewed.sort_values(by=['country', 'len']))


#EXERCISES
#1. Who are the most common wine reviewers in the dataset? Create a Series whose index is the taster_twitter_handle category from the dataset, and whose values count how many reviews each person wrote.
reviews_written = reviews.groupby('taster_twitter_handle').points.count()

#2. What is the best wine I can buy for a given amount of money? Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).
best_rating_per_price = reviews.groupby('price').points.max()

#3.What are the minimum and maximum prices for each variety of wine? Create a DataFrame whose index is the variety category from the dataset and whose values are the min and max values thereof.
price_extremes = pd.DataFrame({'min' : reviews.groupby('variety').price.min(), 'max' : reviews.groupby('variety').price.max()})
print(price_extremes)

#4.What are the most expensive wine varieties? Create a variable sorted_varieties containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).
sorted_varieties = price_extremes.sort_values(by=['min','max'], ascending = False)
print(sorted_varieties)

#5. Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the taster_name and points columns.
reviewer_mean_ratings = reviews.groupby(['taster_name']).points.mean()

#6. What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof {country, variety} pairs. For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. Sort the values in the Series in descending order based on wine count.
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending = False)
print(country_variety_counts)
