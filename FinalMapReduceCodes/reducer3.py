import sys
from operator import itemgetter

current_movie = None
movie_freq = 0

for line in sys.stdin:
    line = line.strip()
    movie_title, movie_rating = line.split('\t')
    try:
        movie_rating = int(movie_rating)
    except ValueError:
        continue
    if current_movie == movie_title:
        movie_freq += 1
    else:
        if current_movie:
            print(f'{current_movie}\t{movie_freq}')
        current_movie = movie_title
        movie_freq = 1

if current_movie == movie_title:
    print(f'{current_movie}\t{movie_freq}')  

# test
# cat movie_reviews.csv | python mapper3.py | sort | python reducer3.py
# Movie Popularity Calculation