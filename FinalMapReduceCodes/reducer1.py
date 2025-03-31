import sys
from operator import itemgetter

current_movie = None
movie_freq = 0
movie_rating_sum = 0


for line in sys.stdin:
    line = line.strip()
    movie_title, movie_rating = line.split('\t')
    try:
        movie_rating = int(movie_rating)
    except ValueError:
        continue
    if current_movie == movie_title:
        movie_freq += 1
        movie_rating_sum += movie_rating
    else:
        if current_movie:
            movie_rating_avg = movie_rating_sum / movie_freq
            print(f'{current_movie}\t{movie_rating_avg}')
        current_movie = movie_title
        movie_freq = 1
        movie_rating_sum = movie_rating

if current_movie == movie_title:
    movie_rating_avg = movie_rating_sum / movie_freq
    print(f'{current_movie}\t{movie_rating_avg}')  

# test
# cat movie_reviews.csv | python mapper1.py | sort | python reducer1.py
# Average Movie Rating Calculation