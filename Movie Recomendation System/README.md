# 🎬 Movie Recommendation System

## 🎯 Objective

This project aims to recommend movies similar to a user-selected movie using a **Content-Based Filtering** approach. It analyzes metadata like cast, director, genres, and title to generate relevant suggestions.

## 🧠 How It Works

- Combines key features of each movie (e.g., cast, director, genres, title)
- Applies **TF-IDF Vectorization** to convert text to numeric form
- Computes **Cosine Similarity** between movie vectors
- Finds the closest match to the input movie title
- Recommends the top similar movies

## 🛠️ Tools & Technologies Used

- **Python**
- **Pandas, NumPy** – Data handling
- **Scikit-learn** – TF-IDF Vectorizer, Cosine Similarity
- **Difflib** – Fuzzy matching for movie titles

## 📈 Dataset Features

- `movie_title`
- `genres`
- `director_name`
- `actor_1_name`, `actor_2_name`, `actor_3_name`

## 💡 Example Flow

1. User inputs a movie title.
2. The system finds a close match from the database.
3. It returns top recommended movies based on content similarity.

