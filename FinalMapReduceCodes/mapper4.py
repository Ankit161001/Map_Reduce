
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    col_val = line.split(',')
    review_id = col_val[0]
    rating = col_val[5]

    # key / values to pass to reducer
    print(f'{rating}\t1')

# test
# cat movie_reviews.csv | python mapper4.py | sort

# Rating Frequency Calculation