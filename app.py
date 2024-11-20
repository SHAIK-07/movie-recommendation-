import streamlit as st
import pandas as pd
import pickle
import requests



# Load data
movie_list = pickle.load(open('movie_list.pkl', 'rb'))
df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = pd.DataFrame(movie_list)

# Title of the app
st.title("🎥 Movie Recommender System")

# TMDb API key
# TMDb API key
TMDB_API_KEY = "4142bd9f69dc53d39b4f3661066099ef"


# Fetch poster path
def get_poster_path(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    )
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500/{data.get('poster_path', '')}"

# Fetch trailer link
def get_trailer(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=en-US"
    )
    data = response.json()
    for video in data.get("results", []):
        if video["type"] == "Trailer":
            return f"https://www.youtube.com/watch?v={video['key']}"
    return None

# Recommendation logic
def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movie_posters = []
    recommend_movie_trailers = []

    for i in movies_list:
        movie_id = df.iloc[i[0]]['id']
        recommend_movies.append(df.iloc[i[0]]['title'])
        recommend_movie_posters.append(get_poster_path(movie_id))
        recommend_movie_trailers.append(get_trailer(movie_id))

    return recommend_movies, recommend_movie_posters, recommend_movie_trailers

# Search for a movie
selected_movie = st.selectbox("🔎 Search for a movie you watched:",movie_list['title'].values)
if selected_movie not in movie_list['title'].values:
    st.warning("Movie not found. Please select a valid movie.")
else:
    st.success(f"You selected: {selected_movie}")

# Recommend button
if st.button("Recommend"):
    if selected_movie in movie_list['title'].values:
        names, posters, trailers = recommend(selected_movie)

        # Create a dynamic grid for recommendations
        st.markdown("## Recommended Movies:")
        cols = st.columns(5)  # Create 5 columns
        for idx, (name, poster, trailer) in enumerate(zip(names, posters, trailers)):
            with cols[idx % 5]:  # Use modulus to cycle columns
                st.image(poster, use_container_width=True)

                st.caption(name)
                if trailer:
                    st.markdown(f"[🎥 Watch Trailer]({trailer})")




# Footer
st.markdown("---")
st.markdown("Powered by [TMDb API](https://www.themoviedb.org/) | Developed with ❤️ by [Shaik](https://www.linkedin.com/in/shaik-hidaythulla/)")
