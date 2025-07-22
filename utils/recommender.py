
import pandas as pd
import pickle

movies = pd.read_csv("data/movies.csv")

class DummySVD:
    def predict(self, user_id, movie_id):
        class Est:
            est = 3.5 + (user_id % 3) * 0.5
        return Est()

svd = DummySVD()

def get_user_recommendations(user_id, top_n=5):
    ratings = pd.read_csv("data/ratings.csv")
    unseen_movies = movies[~movies['movieId'].isin(ratings[ratings['userId'] == user_id]['movieId'])]
    unseen_movies['predicted_rating'] = unseen_movies['movieId'].apply(lambda x: svd.predict(user_id, x).est)
    top_movies = unseen_movies.sort_values('predicted_rating', ascending=False).head(top_n)
    return top_movies[['title', 'predicted_rating']]
