!wget -qnc -P ./movielens https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/movielens/users.dat
!wget -qnc -P ./movielens https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/movielens/ratings.dat
!wget -qnc -P ./movielens https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/movielens/movies.dat

import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

unames = ['user_id', 'gender', 'age', 'occupation', "zip"]
users = pd.read_table('movielens/users.dat', sep="::", header=None, names=unames, engine='python')
print(users.shape)

rnames = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("movielens/ratings.dat", sep="::", header=None, names=rnames, engine="python")
print(ratings.shape)

mnames = ['movie_id', "title", "genres"]
movies = pd.read_table("movielens/movies.dat", sep="::", header=None,
                      names=mnames, engine="python")
print(movies.shape)

age_categories = {
    "Children": (1, 11),
    "PreTeen/Teen": (11, 20),
    "Young Adults": (20, 30),
    "Adults-1": (30, 40),
    "Adults-2": (40,50),
    "Middle Aged Adults": (50,60),
    "Senior Adults": (60, float('inf'))
}

def categorize_age(age):
    for category, (min_age, max_age) in age_categories.items():
        if min_age <= age < max_age:
            return category
    print(min_age, age, max_age)
    return "Unknown"

users['Category'] = users['age'].apply(categorize_age)

user_ratings = pd.merge(ratings, users)
#display("users", "ratings", "user_ratings.head()")

data = pd.merge(user_ratings, movies)
#display("user_ratings", "movies", "data.head()")








