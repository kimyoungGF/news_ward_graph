from konlpy.tag import Okt
from math import log10


# =======================================
# -- TF-IDF function
# =======================================
def f(t, d): #문서의 개수
    # d is document == tokens
    return d.count(t)

def tf(t, d): #문서 내에 나타나는 해당 단어의 총 빈도수
    # d is document == tokens
    return 0.5 + 0.5*f(t,d)/max([f(w,d) for w in d])

def idf(t, D): #한 단어가 문서 집합 전체에서 얼마나 공통적으로 나타나는지
    # D is documents == document list
    numerator = len(D)
    denominator = 1 + len([ True for d in D if t in d])
    return log10(numerator/denominator)

def tfidf(t, d, D): #곱한 결과
    return tf(t,d)*idf(t, D)

def tokenizer(d):
    twit = Okt()
    def keyword_extractor(text): #키워드 추출기로 키워드만 결과
        tokens = twit.phrases(text)#형태소 분석1

        tokens = [token for token in tokens if len(token) > 1]  # 한 글자인 단어는 제외

        count_dict = [(token, text.count(token)) for token in tokens] #단어 하나하나에 토큰 추가

        ranked_words = sorted(count_dict, key=lambda x: x[1], reverse=True)[:20] #내림차순으로 20개 뽑기

        return [keyword for keyword, freq in ranked_words]

    return keyword_extractor(d)

def tfidfScorer(D): #토큰화
    tokenized_D = [tokenizer(d) for d in D]
    result = []
    for d in tokenized_D:
        result.append([(t, tfidf(t, d, tokenized_D)) for t in d])
    return result