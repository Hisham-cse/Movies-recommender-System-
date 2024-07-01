import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=7bcf19d40f5023064dd5fc4ee9b6b277&language=en-US')
    data = response.json()
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{movie_id}?api_key=7bcf19d40f5023064dd5fc4ee9b6b277&language=en-US')
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1]) [1:6]

    recommended_movies = []
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('How would you like to be contacted?',movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    if names and posters:
        cols = st.columns(5)
        for i, col in enumerate(cols[:len(names)]):
            with col:
                st.text(names[i])
                if posters[i]:
                    st.image(posters[i])
                else:
                    st.write("No poster available")
    else:
        st.write("No recommendations found.")