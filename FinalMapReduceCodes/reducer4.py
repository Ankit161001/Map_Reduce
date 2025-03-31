import sys
from operator import itemgetter

current_rating = None
rating_freq = 0

for line in sys.stdin:
    line = line.strip()
    movie_rating, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    if current_rating == movie_rating:
        rating_freq += count
    else:
        if current_rating:
            print(f'{current_rating}\t{rating_freq}')
        current_rating = movie_rating
        rating_freq = count

if current_rating == movie_rating:
    print(f'{current_rating}\t{rating_freq}')  

# test
# cat movie_reviews.csv | python mapper4.py | sort | python reducer4.py
# Rating Frequency Calculation