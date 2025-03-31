
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    col_val = line.split(',')
    review_id = col_val[0]
    movie_title = col_val[1]
    review_year = col_val[2]

    # key / values to pass to reducer
    print(f'{review_year}\t1')

# test
# cat movie_reviews.csv | python mapper6.py | sort

# Movie Review Year Trend Calculation