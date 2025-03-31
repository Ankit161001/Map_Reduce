
import sys
import string

# input comes from STDIN (standard input)
for line in sys.stdin:

    col_val = line.split(',')
    review_id = col_val[0]
    review_text = col_val[6]
    review_text = review_text.lower()
    review_text = review_text.translate(review_text.maketrans('', '', string.punctuation))
    for word in review_text.split(' '):
        # key / values to pass to reducer
        print(f'{word}\t1')

# test
# cat movie_reviews.csv | python mapper5.py | sort

# Review Words Frequency Calculation