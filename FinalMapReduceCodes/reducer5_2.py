import sys
from operator import itemgetter

current_word = None
word_freq = 0

for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t')
    except ValueError: 
        continue
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        word_freq += 1
    else:
        if current_word:
            print(f'{current_word}\t{word_freq}')
        current_word = word
        word_freq = 1

if current_word == word:
    print(f'{current_word}\t{word_freq}')  

# test
# cat movie_reviews.csv | python mapper5.py | sort | python reducer5.py | sort | python reducer5_2.py
# Review Words Frequency Calculation