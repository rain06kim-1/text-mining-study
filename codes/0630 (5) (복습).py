# 2026-06-30 복습 풀이 (문제 4) — return 으로 3곡 단어 수 한 번에
#   파일 이름을 받아 단어 수를 'return' 으로 돌려주는 함수 + os.listdir 반복문
#   핵심: print 는 화면에 보여줄 뿐, return 은 값을 돌려줘 다른 데서 쓸 수 있다
# 실행 결과: HOPE 851 / The Search 796 / Time 527

import os


def count_words(filename) :
    with open('lyrics/'+filename, encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    text = text.split()

    return (len(text))

for filename in os.listdir('lyrics'):
    print(filename,count_words(filename))