import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    if 'poster_path' in data and data['poster_path']:
        full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        return full_path
    else:
        return "https://via.placeholder.com/500x750.png?text=No+Image"  # Placeholder if no poster available

# Load movie data
movies = pickle.load(open('movies.pkl', 'rb'))  # Load full dataset
movies_list = movies['title'].values  # Extract only movie titles

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))
if isinstance(similarity, pd.DataFrame):  # Convert to NumPy if needed
    similarity = similarity.values

# Movie recommendation function
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]  # Get movie index
        distances = similarity[movie_index]  # Fetch similarity scores
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id  # Get movie ID
            recommended_movies.append(movies.iloc[i[0]].title)  # Get movie title
            recommended_posters.append(fetch_poster(movie_id))  # Fetch poster URL

        return recommended_movies, recommended_posters

    except IndexError:
        return ["Movie not found!"], ["https://via.placeholder.com/500x750.png?text=No+Image"]

# Streamlit UI
st.title('Movie Recommender System')

# Select movie
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies_list
)

# Show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)  # ✅ FIXED

    col1, col2, col3, col4, col5 = st.columns(5)  # ✅ FIXED

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
