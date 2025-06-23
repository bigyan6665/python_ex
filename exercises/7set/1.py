released_2025 = set()
for i in range(1,3):
    movie_name = input(f"Enter movie_name{i} released in 2025 = ")
    released_2025.add(movie_name)
print(released_2025)
watched_2025 = set()
for i in range(1,3):
    movie_name = input(f"Enter watched movie_name{i} = ")
    watched_2025.add(movie_name)
print(watched_2025)

print(f"2025 movies watched by users are = {released_2025.intersection(watched_2025)}")
print(f"2025 movies yet to be watched by users are = {released_2025.difference(watched_2025)}")
print(f"All movies = {released_2025.union(watched_2025)}")