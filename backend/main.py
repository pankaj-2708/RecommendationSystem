from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from datetime import date
from huggingface_hub import hf_hub_download

app = FastAPI()


def load_models():
    model_path = hf_hub_download(
        repo_id="Pankaj121212/my-model1", filename="models/story.pkl"
    )
    with open(model_path, "rb") as f:
        similarity1 = pickle.load(f)
    model_path = hf_hub_download(
        repo_id="Pankaj121212/my-model1", filename="models/cast.pkl"
    )
    with open(model_path, "rb") as f:
        similarity2 = pickle.load(f)
    model_path = hf_hub_download(
        repo_id="Pankaj121212/my-model1", filename="models/scale.pkl"
    )
    with open(model_path, "rb") as f:
        similarity3 = pickle.load(f)

    return similarity1, similarity2, similarity3


similarity1, similarity2, similarity3 = load_models()


df = pd.read_csv("../datasets/new_movies_full.csv")


@app.get("/allmovies")
def allmovies():
    release_years = (
        df["release_date"].apply(lambda x: x[:4] if len(str(x)) > 4 else " ").values
    )
    titles = df["title"].values
    final = [f"{titles[i]} ({release_years[i]})" for i in range(len(titles))]
    return final


@app.get("/story")
def RecommendStory(movie):
    index = df[df["title"] == movie.split("(")[0][:-1]].index
    curr = similarity1[index]
    top5 = np.argsort(curr)[0, :][::-1][1:6]
    similar_rows = df[df.index.isin(top5)]

    similar_movies = list(similar_rows["title"].values)
    posters = list(similar_rows["poster_path"].values)
    date1 = list(
        similar_rows["release_date"]
        .apply(lambda x: x[:4] if len(str(x)) > 4 else " ")
        .values
    )

    return {"similar_movies": similar_movies, "posters": posters, "date": date1}


@app.get("/cast")
def Recommendcast(movie):
    index = df[df["title"] == movie.split("(")[0][:-1]].index
    curr = similarity2[index]
    top5 = np.argsort(curr)[0, :][::-1][1:6]
    similar_rows = df[df.index.isin(top5)]
    similar_movies = list(similar_rows["title"].values)
    posters = list(similar_rows["poster_path"].values)
    date = list(
        similar_rows["release_date"]
        .apply(lambda x: x[:4] if len(str(x)) > 4 else " ")
        .values
    )
    return {"similar_movies": similar_movies, "posters": posters, "date": date}


@app.get("/scale")
def Recommendscale(movie):
    index = df[df["title"] == movie.split("(")[0][:-1]].index
    curr = similarity3[index]
    top5 = np.argsort(curr)[0, :][::-1][1:6]
    similar_rows = df[df.index.isin(top5)]
    similar_movies = list(similar_rows["title"].values)
    posters = list(similar_rows["poster_path"].values)
    date = list(
        similar_rows["release_date"]
        .apply(lambda x: x[:4] if len(str(x)) > 4 else "")
        .values
    )
    return {"similar_movies": similar_movies, "posters": posters, "date": date}
