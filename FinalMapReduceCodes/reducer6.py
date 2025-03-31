import sys
from operator import itemgetter

current_year = None
year_freq = 0

for line in sys.stdin:
    line = line.strip()
    review_year, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    if current_year == review_year:
        year_freq += count
    else:
        if current_year:
            print(f'{current_year}\t{year_freq}')
        current_year = review_year
        year_freq = count

if current_year == review_year:
    print(f'{current_year}\t{year_freq}')  

# test
# cat movie_reviews.csv | python mapper6.py | sort | python reducer6.py
# Movie Review Year Trend Calculation