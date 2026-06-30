# =============================================================
#  2026-06-30 공부 기록
#  주제: 코드를 함수(function)로 정리하기 — 재사용 가능한 분석 도구
#
#  [오늘 만든 것]
#    analyze_lyrics(text) : 가사를 넣으면 단어 빈도를 분석·그래프까지 해주는 함수
#
#  [공부한 개념]
#    1. 함수(function):  def 이름(매개변수):  ...  (작업을 묶어 재사용)
#         - 매개변수(parameter): 함수가 받는 '빈 자리' (여기선 text)
#         - 재료(가사)만 바꿔 부르면, 코드 복붙 없이 어떤 노래든 분석
#    2. 리스트 컴프리헨션: [pair[0] for pair in ...] (한 줄로 거르고 뽑기)
#    3. 튜플(tuple): (단어, 숫자) 짝. pair[0]=단어, pair[1]=숫자
#
#  [오늘 직접 잡은 버그 2개]
#    (1) text = lyrics.lower()  →  text = text.lower()
#          바깥 변수(lyrics) 말고, 함수가 받은 재료(text)를 써야 재사용 가능
#    (2) for pair in clean_count               → Counter 를 그냥 돌면 '단어'만 나옴
#        for pair in clean_count.most_common(10) → (단어, 숫자) 짝이 나옴  ← 이게 맞음
# =============================================================

from collections import Counter
import matplotlib.pyplot as plt

stopwords = ["a", "you", "and", "the", "to", "be", "it", "if", "but", "your", "for", "with", "up", "at", "me", "when"]

def analyze_lyrics(text):
    text = text.lower()
    text = text.replace('?', '')
    text = text.replace(',', '')
    words = text.split()
    clean = [w for w in words if w not in stopwords]

    clean_count = Counter(clean)
    print(clean_count)
    
    letter = [pair[0] for pair in clean_count.most_common(10)]
    count = [pair[1] for pair in clean_count.most_common(10)]
    
    print(letter)
    print(count)

    plt.bar(letter,count)
    plt.show()

    
lyrics = '''Just think about it for a second, if you look at your face
Every day when you get up and think you'll never be great
You'll never be great, not because you're not, but the hate
Will always find a way to cut you up and murder your faith'''
analyze_lyrics(lyrics)
