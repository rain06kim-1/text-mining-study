# 2026-06-30 복습 풀이 (문제 1~3) — 한 곡(Time - NF) 분석
#   문제1: 총 단어 수            -> len(words)
#   문제2: 'time' 등장 횟수      -> words.count('time')  (대소문자 버그 직접 수정: 15->20)
#   문제3: 서로 다른 단어 종류    -> len(set(words))  ← 어휘 다양성(TTR)의 출발점
# 실행 결과: 527 / 20 / 192

with open ('lyrics/Time - NF.txt', encoding='utf-8') as f:
    text = f.read()

def count_clean_words(text):
    text = text.lower()
    text = text.replace('?','')
    text = text.replace(',','')
    text = text.replace('(','')
    text = text.replace(')','')

    words = text.split()
    count = len(words)
    time_count = words.count('time')

    print(count)
    print(time_count)
    print(len(set(words)))

count_clean_words(text)