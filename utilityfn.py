import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats.mstats import winsorize
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import pickle
import warnings

warnings.filterwarnings("ignore")


def grouped_bar_ch(
    values_A,
    values_B,
    groups,
    tle="",
    v1="hit",
    v2="flop",
    title_x="",
    title_y="Amount in USD ($)",
):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=groups, y=values_A, name=v1, marker_color="blue", textposition="outside"
        )
    )

    fig.add_trace(
        go.Bar(
            x=groups, y=values_B, name=v2, marker_color="orange", textposition="outside"
        )
    )

    # Group bars side-by-side
    fig.update_layout(
        barmode="group",
        title=tle,
        xaxis_title=title_x,
        yaxis_title=title_y,
        xaxis=dict(categoryorder="array", categoryarray=groups),
    )

    return fig


df1 = pd.read_csv("./datasets/sol.csv")


def draw_graph(name, lst):
    revenues_hit = []
    revenues_flop = []
    count_hit = []
    count_flop = []
    budget_hit = []
    budget_flop = []
    total_rev = []
    total_bug = []
    for comp in lst:
        total_rev.append(df1[df1[comp] == 1]["revenue"].sum())
        total_bug.append(df1[df1[comp] == 1]["budget"].sum())
        revenues_hit.append(
            df1[(df1[comp] == 1) & (df1["hit/flop"] == "hit")]["revenue"].sum()
        )
        revenues_flop.append(
            df1[(df1[comp] == 1) & (df1["hit/flop"] == "flop")]["revenue"].sum()
        )
        budget_hit.append(
            df1[(df1[comp] == 1) & (df1["hit/flop"] == "hit")]["budget"].sum()
        )
        budget_flop.append(
            df1[(df1[comp] == 1) & (df1["hit/flop"] == "flop")]["budget"].sum()
        )
        count_hit.append(df1[(df1[comp] == 1) & (df1["hit/flop"] == "hit")].shape[0])
        count_flop.append(df1[(df1[comp] == 1) & (df1["hit/flop"] == "flop")].shape[0])
    fig1 = grouped_bar_ch(
        revenues_hit, revenues_flop, lst, "Revenue comparison", title_x=name
    )
    fig2 = grouped_bar_ch(
        count_hit,
        count_flop,
        lst,
        "Total no of movies",
        title_x=name,
        title_y="Total No of Movies",
    )
    fig3 = grouped_bar_ch(
        budget_hit, budget_flop, lst, "Budget of all movies", title_x=name
    )
    fig4 = grouped_bar_ch(
        total_rev, total_bug, lst, "Revenue and Budget", "Reveue", "Budget", name
    )
    return fig1, fig2, fig3, fig4


def movieDetails(movie_name):
    return df[df["original_title"] == movie_name]

df = pd.read_csv("./datasets/new_movies_full.csv")

def allmovies():
    release_years=df["release_date"].apply(lambda x:x[:4]if len(str(x))>4 else " ").values
    titles=df["title"].values
    final=[f"{titles[i]} ({release_years[i]})" for i in range(len(titles))]
    return final




def RecommendStory(movie):
    similarity1 = None
    with open("./models/story.pkl", "rb") as f:
        similarity1 = pickle.load(f)
    index = df[df["title"] == movie.split("(")[0][:-1]].index
    curr = similarity1[index]
    top5 = np.argsort(curr)[0, :][::-1][1:6]
    similar_rows = df[df.index.isin(top5)]
    similar_movies = similar_rows["title"].values
    posters = similar_rows["poster_path"].values
    date = similar_rows["release_date"].apply(lambda x:x[:4]if len(str(x))>4 else " ").values
    return similar_movies, posters,date


similarity2 = None
with open("./models/cast.pkl", "rb") as f:
    similarity2 = pickle.load(f)


def Recommendcast(movie):
    index = df[df["title"] == movie.split("(")[0][:-1]].index
    curr = similarity2[index]
    top5 = np.argsort(curr)[0, :][::-1][1:6]
    similar_rows = df[df.index.isin(top5)]
    similar_movies = similar_rows["title"].values
    posters = similar_rows["poster_path"].values
    date = similar_rows["release_date"].apply(lambda x:x[:4]if len(str(x))>4 else ' ').values
    return similar_movies, posters ,date


similarity3 = None
with open("./models/scale.pkl", "rb") as f:
    similarity3 = pickle.load(f)


def Recommendscale(movie):
    index = df[df["title"] == movie.split("(")[0][:-1]].index
    curr = similarity3[index]
    top5 = np.argsort(curr)[0, :][::-1][1:6]
    similar_rows = df[df.index.isin(top5)]
    similar_movies = similar_rows["title"].values                              
    posters = similar_rows["poster_path"].values
    date = similar_rows["release_date"].apply(lambda x:x[:4]if len(str(x))>4 else '').values
    return similar_movies, posters,date