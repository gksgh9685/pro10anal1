# 형태소 분석
# 말뭉치(corpus)는 자연어 연구, 언어 분석, 인공지능(ai) 학습을 위해 다양한 분야의 
# 언어 자료를 컴퓨터가 읽고 처리할 수 있도록 모아 놓은 대규모 텍스트-음성-영상 데이터 집합.
# 정의 : 사람이 실제로 쓰고 말한 언어 자료를 수집-정제한 데이터.
# 문접 연구, 번역 시스템, 챗봇 등 다양한 언어 데이터 분석의 기초 자료로 활용.
# 형태소(morpheme)는 의미를 가지는 가장 작은 단위를 말함.

# 영어 토큰(token)이란 컴퓨터가 텍스트를 이해하고 연산할 수 있도록 문장, 단어, 형태소,
# 혹은 글자의 조각처럼 의미를 가진 최소 단위로 쪼갠 결과물을 뜻한다.
# 토큰의 주요 유형 : 단어 토큰(word token), 형태소 토큰(morpheme token), 문자 토큰(char)

# 영어 토큰(token)화
import nltk
from nltk.tokenize import word_tokenize

# 최초 실행 시 필요한 데이터 다운로드
# nltk.download('punkt')
# nltk.download('punkt_tab')

text = 'i am studying python with my friends at room.'

# 1. 토큰화
tokens = word_tokenize(text)
print(tokens)       # ['i', 'am', 'studying',...]
print()
# 품사 태깅
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)     # [('i', 'NN'), ('am', 'VBP'), ('studying', 'VBG'),...]

print('\n\n 한국어 토큰(token)화------')
# 대표적인 한글 형태소 분석 라이브러리
# pip install jpypel <== java 컴파일러가 먼저 설치되어야 함
from konlpy.tag import Okt, Kkma, Komoran
text = '나는 오늘 아침에 학교에 갔다. 가는 길에 국화가 피어 너무 아름다웠다.'

print('okt------')
okt = Okt()
print('형태소 : ', okt.morphs(text))
print('품사 태깅 : ', okt.pos(text))
print('품사 태깅(어감 포함) : ', okt.morphs(text, stem=True))   # 원형 출력 : 그래요 -> 그렇다
print('명사 추출 : ', okt.nouns(text))

print('Kkma------')
Kkma = Kkma()
print('형태소 : ', Kkma.morphs(text))
print('품사 태깅 : ', Kkma.pos(text))
print('명사 추출 : ', Kkma.nouns(text))

print('Komoran------')
Komoran = Komoran()
print('형태소 : ', Komoran.morphs(text))
print('품사 태깅 : ', Komoran.pos(text))
print('명사 추출 : ', Komoran.nouns(text))
