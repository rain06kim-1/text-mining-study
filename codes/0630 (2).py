with open ('lyrics/The Search - NF.txt', encoding='utf-8') as f:
    text=f.read()

from collections import Counter 
import matplotlib.pyplot as plt

stopwords = ["that","in","a",'not',"on","you", "and", "the", "to", "be", "it", "if", "but", "your", "for", "with", "up", "at", "me", "when"]

def analyze_lyrics(text):
    text=text.lower()
    text=text.replace('?','')
    text=text.replace(',','')
    text=text.replace('.','')
    text=text.replace('(','')
    text=text.replace(')','')
    text=text.replace('yeah','')
    text=text.replace('ah','')
    text=text.replace('huh','')
    text=text.replace('"','')

    words = text.split()
    clean_words = [w for w in words if w not in stopwords]
    clean_count = Counter(clean_words).most_common(10)

    print(clean_count)

    words = [pair[0] for pair in clean_count]
    count = [pair[1] for pair in clean_count]

    plt.bar(words,count)
    plt.show()

analyze_lyrics(text)
