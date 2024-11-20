Movie Recommender System
Description
This is a Movie Recommender System built with Streamlit, Python, and The Movie Database (TMDb) API. It recommends similar movies based on the movie title you select. The app uses content-based filtering to find movies with similar features and display their posters and details.

Features
Movie Selection: Choose a movie from the dropdown list.
Movie Recommendations: Based on the selected movie, it recommends similar movies.
Poster Display: Displays movie posters fetched from the TMDb API.
Interactive UI: Built with Streamlit, providing an intuitive and user-friendly interface.
Technologies Used
Streamlit: Web framework for building the app interface.
pandas: Data manipulation library.
requests: HTTP library to interact with the TMDb API.
scikit-learn: For implementing the content-based recommendation algorithm.
TMDb API: Fetching movie details and posters.
Installation
1. Clone this Repository
bash
Copy code
git clone https://github.com/SHAIK-07/movie-recommender-system.git
2. Install the Dependencies
Make sure you have Python installed (preferably version 3.7 or above). Then, install the required libraries using requirements.txt:

bash
Copy code
pip install -r requirements.txt
3. API Key for TMDb
Create a TMDb account and get your API key from here.
Replace the placeholder your_api_key_here in the code with your actual TMDb API key.
4. Run the App
bash
Copy code
streamlit run app.py
Open the link provided by Streamlit in your browser to view the app.

File Structure
bash
Copy code
movie-recommender-system/
│
├── app.py                  # Main application code
├── movie_list.pkl          # Pickled movie list for recommendations
├── movies.pkl              # Pickled DataFrame containing movie data
├── similarity.pkl          # Pickled similarity matrix for recommendations
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
Usage
Select a movie from the dropdown list.
The app will recommend 5 similar movies based on the selected movie.
Each recommendation includes the movie title and its poster.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
TMDb API: For providing the movie data and posters.
Streamlit: For making it easy to create and deploy interactive web apps.
Scikit-learn: For providing the content-based filtering algorithms.
