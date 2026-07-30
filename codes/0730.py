# =============================================================
#  2026-07-30 공부 기록 (세션 2)
#  주제: NLTK — 전문 전처리 도구로 교체
#
#  [오늘 만든 것]
#    손으로 하던 전처리(replace 9줄 + 손 불용어 23개)를 NLTK로 교체.
#    토큰화 → 표준 불용어 → 기호 제거 → 표제어 추출 → Top 10 그래프
#
#  [공부한 개념]
#    1. NLTK 설치는 2단계: pip install nltk(도구) + nltk.download(데이터)
#         - 받은 데이터: punkt_tab(토큰화 규칙), stopwords(불용어), wordnet(사전)
#    2. word_tokenize(text): 언어를 아는 가위.
#         - 기호를 따로 뗌: 'stop!' → 'stop', '!'  (replace 불필요, ahead 안 다침)
#         - 축약형을 가름: don't → do + n't,  can't → ca + n't
#    3. stopwords.words('english'): 표준 불용어 198개 리스트를 꺼내옴
#         - 가사용 감탄사(oh, yeah, ah, huh)는 없어서 extend 로 직접 추가
#         - 'english'는 파일 이름이라 소문자로! (대문자는 윈도우에서만 우연히 됨)
#    4. w.isalpha(): 문자열 하나에게 "알파벳으로만 됐니?" 묻기 → True/False
#         - 컴프리헨션 if 자리에 바로 사용 (== True 는 군더더기)
#    5. 컴프리헨션의 두 능력:
#         [w for w in 리스트 if 조건]   ← 거르기 (불용어·기호 2단 여과)
#         [변환(w) for w in 리스트]     ← 바꾸기 (표제어 추출에 사용)
#    6. 클래스와 물건: WordNetLemmatizer(설계도) → lemmatizer(기계 제작)
#         - lemmatizer = WordNetLemmatizer() 로 만들고 .lemmatize(w) 버튼 사용
#         - years → year (복수→기본형). 단, 기본은 명사 가정이라 went→go 는 못 함
#    7. 메서드 vs 함수: 대상.버튼() = 그 자료형에 딸린 기능 / 도구(대상) = 독립 도구
#         - 리스트에 isalpha 없음, 문자열에 extend 없음 → 버튼의 주인 확인!
#    8. 함수의 안/바깥 이름: 바깥의 filename 을 건네면 안에서는 title 이름표가 붙음
#         - plt.title(title) 로 수정 (전역변수 filename 몰래 쓰기 졸업)
#
#  [오늘 직접 잡은 것]
#    (1) print 없이 count 만 씀 → 스크립트에선 print 해야 화면에 보임
#    (2) nltk.tokenization → tokenize (import 는 실제 이름을 정확히)
#    (3) stopwords.extend(add) → stopwords 는 도구, 리스트는 stop_words
#    (4) stop_words = 리스트.extend(add) → extend 는 돌려주는 값이 None, 등호 없이!
#    (5) words('english') 따옴표 빼먹음 → NameError
#    (6) clean_words.isalpha() → isalpha 는 단어(w) 하나의 버튼
#    (7) w.lemmatize() → lemmatize 는 lemmatizer 기계의 버튼, w 는 재료
#    (8) The Search 에 수상한 'ca' 4회 발견 → can't 가 ca+n't 로 갈라진 것.
#        n't 는 isalpha 가 걸렀지만 ca 는 통과 → 가사용 불용어에 추가로 해결
#
#  [복습 때 다시 볼 점]
#    - lemmatize 는 pos(품사) 옵션을 주면 동사도 처리 가능 (나중 세션에서)
#    - gonna → gon+na, wanna → wan+na 도 나타나면 불용어 추가 (YAGNI: 미리 안 함)
# =============================================================

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
