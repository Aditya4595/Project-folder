import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'title': [
        'The Matrix', 'John Wick', 'Interstellar',
        'Inception', 'The Prestige', 'The Dark Knight',
        'Pulp Fiction', 'The Godfather'
    ],
    'description': [
        'A computer hacker learns about the true nature of his reality.',
        'An ex-hitman comes out of retirement for revenge.',
        'A team travels through a wormhole in space.',
        'A thief enters dreams to steal secrets.',
        'Two magicians battle with science and illusions.',
        'Batman faces a chaotic villain named Joker.',
        'Two hitmen face moral dilemmas in crime life.',
        'The aging patriarch of an organized crime dynasty transfers control.'
    ]
}

df = pd.DataFrame(data)
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(title, df=df, sim_matrix=cosine_sim):
    if title not in df['title'].values:
        return f"Movie '{title}' not found in the dataset."

    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    movie = input("Enter a movie title: ")
    print("\nRecommended movies:")
    print(recommend(movie))
