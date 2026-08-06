#Renaming and Combining
import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

#The first function we'll introduce here is rename(), which lets you change index names and/or column names
reviews.rename(columns={'points': 'score'})

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

#Both the row index and the column index can have their own name attribute. The complimentary rename_axis() method may be used to change these names
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

#The simplest combining method is concat(). Given a list of elements, this function will smush those elements together along an axis.
#This is useful when we have data in different DataFrame or Series objects but having the same fields (columns).
canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

print(pd.concat([canadian_youtube, british_youtube]))

#join() lets you combine different DataFrame objects which have an index in common. For example, to pull down videos that happened to be trending on the same day in both Canada and the UK, we could do the following:
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')

#Exercises

#1. region_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns={'region_1': 'region' , 'region_2': 'locale' })

#2. Set the index name in the dataset to wines.
reindexed = reviews.rename_axis("wines", axis='rows')

#3. The Things on Reddit dataset includes product links from a selection of top-ranked forums ("subreddits") on reddit.com. Run the cell below to load a dataframe of products mentioned on the /r/gaming subreddit and another dataframe for products mentioned on the r//movies subreddit.
gaming_products = pd.read_csv("gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("movies.csv")
movie_products['subreddit'] = "r/movies"

#Create a DataFrame of products mentioned on either subreddit.
combined_products = pd.concat([gaming_products, movie_products])

#The Powerlifting Database dataset on Kaggle includes one CSV table for powerlifting meets and a separate one for powerlifting competitors. Run the cell below to load these datasets into dataframes:
powerlifting_meets = pd.read_csv("meets.csv")
powerlifting_competitors = pd.read_csv("openpowerlifting.csv")
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))

