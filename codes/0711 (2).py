from nltk.corpus import stopwords
stop_words = stopwords.words('english')

add =['oh','yeah','ah','huh']

stop_words.extend(add)

print(len(stop_words))

print(stop_words.count('yeah'))
