
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    col_val = line.split(',')
    genre = col_val[3]
    rating = col_val[5]

    # key / values to pass to reducer
    print(f'{genre}\t{rating}')

# test
# cat movie_reviews.csv | python mapper2.py | sort

# Genre Based Rating Calculation