movies = [ 
    ("The Matrix", 1999),
    ("Avatar", 2009), 
    ("Jurassic Park", 1993), 
    ("Avengers: Endgame", 2019), 
    ("Inception", 2010), 
    ("Titanic", 1997) 
]
# Sort it by year
sorted_movies = sorted(movies, key=lambda x: x[1])
print("Movies (Newest to Oldest):")
for item in sorted_movies:
    print(item)