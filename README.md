Use this Jupyter Notebook: use Google Colab or Jupyter run environments (Online or VSCode)

Execute all of the below code snippets to:
  1. Get to know about our implementation of Content, Colaborative and Popularity based filtering
  2. Certain parts of the notebook need to be executed to execute the "Main Functional code for Hybrid Filtered movie recommendation" below.
Executing everything also gives some insight on our progression and data format.

# **If not connected to the internet** then Replace the **Third Cell** of the notebook with the below code:

**start of code**

unames = ['user_id', 'gender', 'age', 'occupation', "zip"]
users = pd.read_table('data/users.dat', sep="::", header=None, names=unames, engine='python')
print(users.shape)

rnames = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("data/ratings.dat", sep="::", header=None, names=rnames, engine="python")
print(ratings.shape)

mnames = ['movie_id', "title", "genres"]
movies = pd.read_table("data/movies.dat", sep="::", header=None, names=mnames, engine="python")
print(movies.shape)

**end of code**

The Dataset is given in the "data" folder of this branch only
