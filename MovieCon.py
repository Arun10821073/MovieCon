import pandas
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


movies_dict = pickle.load(open('MovieCon_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# For Title and Header
st.title(':blue[Movie]:red[Con]:registered:')
st.header('A Recommendation System')
selected_movie_name = st.selectbox('Search for movies:film_projector:',
movies['title'].values)

# For Button
if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

