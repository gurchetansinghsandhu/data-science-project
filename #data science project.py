#data science project

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


#LOAD DATA 
df = pd.read_csv("C:/Users/sande/OneDrive/Desktop/net.csv")

#CLEAN DATA
df = df.dropna(subset=["type" , "release_year" ,"rating" , "country" , "duration"])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index , type_counts.values , color =["skyblue", "green"])
plt.title("Number of Films v/s T.V Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tv_shows.png")

plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8 , 6))
plt.pie(rating_counts, labels = rating_counts , autopct="%1.1f%%", startangle=90)
plt.title("Percentage")
plt.tight_layout()
plt.savefig("content.png")

plt.show()

movie_rating = df["duration"].value_counts()
plt.figure(figsize =(8, 6))
plt.hist(movie_rating , bins = 35 , color = "green" , edgecolor = "blue")
plt.title("Duration of Movies")
plt.xlabel("duration")
plt.ylabel("movies")
plt.tight_layout()
plt.savefig("duration.png")

plt.show()

countries_list = df["country"].value_counts().head(10)
plt.figure(figsize = (8, 6))
plt.bar(countries_list.index , countries_list.values , color = ["green" , "red"])
plt.title("Countries in Netfilx")
plt.xlabel("number of shows ")
plt.ylabel("country")
plt.tight_layout()
plt.savefig("country.png")

plt.show()