import sys
from operator import itemgetter
import string

current_word = None
word_freq = 0

net_review_text = ''


for line in sys.stdin:
    line = line.strip()
    # print(line)
    try:
        movie_review_text, review_id = line.split('\t') 
    except ValueError:
        continue
    net_review_text += movie_review_text + ' '

net_review_text = net_review_text.lower()
net_review_text = net_review_text.translate(net_review_text.maketrans('', '', string.punctuation))

for word in net_review_text.split(' '):
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
# cat movie_reviews.csv | python mapper5.py | sort | python reducer5.py
# Review Words Frequency Calculation