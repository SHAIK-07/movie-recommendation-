# 🎬 Movie Recommender System 🍿

## 📜 Description

This is a Movie Recommender System built with Streamlit, Python, and The Movie Database (TMDb) API. It recommends similar movies based on the movie title you select. The app uses content-based filtering to find movies with similar features and display their posters and details.

## ✨ Features

- **🎥 Movie Selection**: Choose a movie from the dropdown list.
- **🔍 Movie Recommendations**: Based on the selected movie, it recommends similar movies.
- **🖼️ Poster Display**: Displays movie posters fetched from the TMDb API.
- **💻 Interactive UI**: Built with **Streamlit**, providing an intuitive and user-friendly interface.

## 🛠️ Technologies Used

- **Streamlit**: Web framework for building the app interface.
- **pandas**: Data manipulation library.
- **requests**: HTTP library to interact with the TMDb API.
- **scikit-learn**: For implementing the content-based recommendation algorithm.
- **TMDb API**: Fetching movie details and posters.

## 📦 Install the Dependencies

Make sure you have Python installed (preferably version 3.7 or above). Then, install the required libraries using "requirements.txt":

```bash
pip install -r requirements.txt
```

## 🔑 API Reference

Create a TMDb account and get your API key from [TMDb API](https://developer.themoviedb.org/docs/getting-started).

Replace the placeholder `your_api_key_here` in the code with your actual TMDb API key.

## 🚀 Run the App

```bash
streamlit run app.py
```

Open the link provided by Streamlit in your browser to view the app.

## 📁 File Structure

Here’s a guide to the essential files and directories in our project:

```bash
movie-recommender-system/
│
├── app.py                  # Main application code
├── movie_list.pkl          # Pickled movie list for recommendations
├── movies.pkl              # Pickled DataFrame containing movie data
├── similarity.pkl          # Pickled similarity matrix for recommendations
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

This map will help you navigate the project and locate key files with ease!

## 📚 Usage

Select a movie from the dropdown list.

The app will recommend 5 similar movies based on the selected movie.

Each recommendation includes the movie title and its poster.

## 📄 License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details on terms and conditions.

Feel free to use and contribute to the project under these terms!

## 🙏 Acknowledgements

- [TMDb API](https://developer.themoviedb.org/docs/getting-started): For providing the movie data and posters.
- [Streamlit](https://docs.streamlit.io/): For making it easy to create and deploy interactive web apps.
- [Scikit-learn](https://scikit-learn.org/stable/index.html): For providing the content-based filtering algorithms.

## 🎥 Demo

For a demo, please visit the following link:

[Movie Recommender System Demo](https://movie-recommendation-m.streamlit.app/)
