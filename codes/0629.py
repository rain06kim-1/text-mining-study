# =============================================================
#  2026-06-29 공부 기록
#  주제: 노래 가사 텍스트 마이닝 — 기초 파이프라인 (1곡 분석)
#
#  [오늘 만든 것]
#    NF "The Search" 가사에서 많이 쓴 단어 Top 10 막대그래프
#
#  [공부한 개념]
#    1. 변수 / 문자열(string): 여러 줄 글자는 """ ... """ 로 담기
#    2. 전처리(preprocessing) = 분석 전에 데이터 다듬기
#         .lower()   → 모두 소문자로 (Just 와 just 를 같은 단어로)
#         .replace() → 기호( ? , ) 제거
#    3. 토큰화(tokenization): .split() 으로 문장을 '단어 리스트'로 쪼개기
#    4. 빈도 분석: Counter 로 단어별 등장 횟수 세기 / .most_common(n)
#    5. 불용어(stopword): a, you, the 처럼 의미 없는 단어 제거
#         for 반복문 + if (단어 not in stopwords) 로 거르기
#    6. 시각화: matplotlib 의 plt.bar 로 막대그래프 (pip 으로 설치)
#
#  [핵심 깨달음]
#    가장 많이 나온 단어는 보통 의미 없는 문법 단어(불용어)다.
#    그걸 빼야 진짜 핵심 단어(never, great, faith)가 드러난다.
# =============================================================

from collections import Counter

lyric = """Just hang with me, this'll only take a moment, okay?
Just think about it for a second, if you look at your face
Every day when you get up and think you'll never be great
You'll never be great, not because you're not, but the hate
Will always find a way to cut you up and murder your faith"""


lyric_lower = lyric.lower()

f1 = lyric_lower.replace('?','')
final = f1.replace(',','')

words = final.split()


words_count = Counter(words)

stopwords = ["a", "you", "and", "the", "to", "be", "it", "if", "but", "your", "for", "with", "up", "at", "me", "when"]

meaningful = []

for w in words :
    if w not in stopwords :
        meaningful.append(w)

meaningful_count = Counter(meaningful)


import matplotlib.pyplot as plt

top10 = meaningful_count.most_common(10)

labels = [pair[0] for pair in top10]
counts = [pair[1] for pair in top10]

plt.bar(labels, counts)
plt.show()


