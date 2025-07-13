# 🎥 Movie Recommendation System using Content-Based Filtering

A powerful and interactive **content-based movie recommender system** that suggests movies based on three distinct perspectives: **story**, **cast & crew**, and **scale**. Built with Python and Streamlit using the **TMDb 5000 Movie Dataset**, the system also includes an interactive data analysis dashboard.

---

## 🚀 Features

* 🔍 **Three distinct recommendation strategies**:

  1. **Story-based**: Uses the movie's `title`, `overview`, and `tagline` to recommend movies with similar themes and narratives.
  2. **Cast & Crew-based**: Leverages information about `cast`, `crew`, `production companies`, and `production countries` to suggest movies with similar creators or production styles.
  3. **Scale-based**: Considers numerical attributes like `budget`, `revenue`, `profit`, and `popularity` to suggest movies of similar commercial scale or success.

* 📊 **Exploratory Data Analysis (EDA)** section to interactively explore the TMDb dataset (5,000 movies).

* 🧠 Uses **cosine similarity** from scikit-learn to calculate similarity between movies.

* 🎨 Clean and responsive **Streamlit** UI.

* 🎞️ Shows posters and movie titles in an easy-to-browse layout.

* 🧰 Sidebar customization and filtering options.

---

## 📁 Dataset

* **Source**: [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* Fields used: `title`, `overview`, `tagline`, `cast`, `crew`, `production_companies`, `production_countries`, `budget`, `revenue`, `popularity`, etc.

---

## 🛠️ Technologies Used

* Python
* Pandas & NumPy
* scikit-learn (`cosine_similarity`)
* Streamlit
* Plotly (for interactive visualizations)
* TMDb Dataset

---

## 📦 Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/pankaj-2708/RecommendationSystem
   cd movie-recommendation-system
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

---

## 📱 Live Demo

Check out the live demo here: [Movie Recommender App](https://your-demo-link.com)



## 🙏 Acknowledgements

* [TMDb](https://www.themoviedb.org/) for providing the dataset
* [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* [Streamlit](https://streamlit.io/) for making UI effortless
* scikit-learn for ML utilities
