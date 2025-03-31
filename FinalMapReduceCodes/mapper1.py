
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    col_val = line.split(',')
    movie_title = col_val[1]
    rating = col_val[5]

    # key / values to pass to reducer
    print(f'{movie_title}\t{rating}')

# test
# cat movie_reviews.csv | python mapper1.py | sort

# Average Movie Rating Calculation