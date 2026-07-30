import os
from collections import Counter
import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "I can't stop, and I won't stop!"
text = text.lower()
token = word_tokenize(text)
# print(token)

stop_words = stopwords.words('english')
clean_token = [w for w in token if w not in stop_words]
# print(clean_token)
clean_token = [w for w in clean_token if w.isalpha()]
print(clean_token)

