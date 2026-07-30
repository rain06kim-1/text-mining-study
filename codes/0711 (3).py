import os
from collections import Counter
import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer 

lemmatizer = WordNetLemmatizer() 

add =['oh','yeah','ah','huh','ca']
stop_words = stopwords.words('english')
stop_words.extend(add)

def analyze_lyrics(text,title):
    text=text.lower()
    
    words = word_tokenize(text)
    clean_words = [w for w in words if w not in stop_words]
    clean_words = [w for w in clean_words if w.isalpha() == True]
    clean_words = [lemmatizer.lemmatize(w) for w in clean_words]
    clean_count = Counter(clean_words).most_common(10)

    print(clean_count)

    words = [pair[0] for pair in clean_count]
    count = [pair[1] for pair in clean_count]

    plt.bar(words,count)
    plt.title(title)
    plt.show()
    


for filename in os.listdir('lyrics'):
    with open('lyrics/'+filename, encoding ='utf-8') as f:
        text = f.read()
    analyze_lyrics(text,filename)

