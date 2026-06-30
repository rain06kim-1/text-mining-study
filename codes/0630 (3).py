# =============================================================
#  2026-06-30 공부 기록 (세션 1)
#  주제: 파일로 데이터 관리 + 여러 곡 한 번에 분석
#
#  [오늘 만든 것]
#    lyrics 폴더 안의 모든 가사 .txt 를 자동으로 읽어,
#    곡마다 단어 빈도 Top 10 막대그래프(+곡 제목)를 그리는 프로그램
#
#  [공부한 개념]
#    1. 파일 읽기:  with open('경로', encoding='utf-8') as f:  /  text = f.read()
#         - with     : 파일을 열고 작업 끝나면 '자동으로 닫아주는' 안전한 방법
#         - encoding='utf-8' : 글자가 깨지지 않게 하는 약속
#    2. 경로(path): 폴더 안 파일은 '폴더이름/파일이름' 으로 적는다 (lyrics/노래.txt)
#         - FileNotFoundError = 그 위치에 파일이 없다는 에러
#    3. os.listdir('폴더'): 폴더 안 파일 '이름들'의 리스트를 돌려줌
#         - 이름만 주므로, open 할 땐 'lyrics/' + filename 으로 폴더를 다시 붙인다
#    4. for 반복문 + 들여쓰기: 들여쓰기가 '반복문 안/밖'을 결정한다
#         - 분석 함수를 for 안에 넣어야 곡마다 실행된다
#    5. 매개변수 2개 함수:  def analyze_lyrics(text, title)  (재료 2개 받기)
#
#  [오늘 직접 잡은 것]
#    (1) FileNotFoundError → 경로 앞에 'lyrics/' 폴더를 붙여 해결
#    (2) 그래프가 1개만 뜸 → analyze_lyrics(text) 가 for 밖에 있어서.
#        for 안쪽으로 들여쓰니 곡마다(3번) 그래프가 떴다.
#
#  [복습 때 다시 볼 점]
#    - .replace('ah','') 는 단어가 아니라 '글자 조각'을 지운다 (ahead→ead 위험)
#      → 세션 2(NLTK)에서 제대로 된 토큰화로 해결 예정
#    - 그래프 제목에 매개변수 title 대신 바깥 변수 filename 을 썼는데도 동작함:
#      filename 이 for 문의 전역변수라 '우연히' 된 것. 다음엔 받은 title 을 쓰면 더 안전.
# =============================================================

import os
from collections import Counter
import matplotlib.pyplot as plt
stopwords = ['i','of',"that",'oh',"in","a",'not',"on","you", "and", "the", "to", "be", "it", "if", "but", "your", "for", "with", "up", "at", "me", "when"]

def analyze_lyrics(text,title):
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
    plt.title(filename)
    plt.show()
    


for filename in os.listdir('lyrics'):
    with open('lyrics/'+filename, encoding ='utf-8') as f:
        text = f.read()
    analyze_lyrics(text,filename)

