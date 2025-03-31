import sys
from operator import itemgetter

current_genre = None
genre_freq = 0
genre_rating_sum = 0


for line in sys.stdin:
    line = line.strip()
    genre_title, genre_rating = line.split('\t')
    try:
        genre_rating = int(genre_rating)
    except ValueError:
        continue
    if current_genre == genre_title:
        genre_freq += 1
        genre_rating_sum += genre_rating
    else:
        if current_genre:
            genre_rating_avg = genre_rating_sum / genre_freq
            print(f'{current_genre}\t{genre_rating_avg}')
        current_genre = genre_title
        genre_freq = 1
        genre_rating_sum = genre_rating

if current_genre == genre_title:
    genre_rating_avg = genre_rating_sum / genre_freq
    print(f'{current_genre}\t{genre_rating_avg}')  

# test
# cat movie_reviews.csv | python mapper2.py | sort | python reducer2.py
# Average Genre Rating Calculation