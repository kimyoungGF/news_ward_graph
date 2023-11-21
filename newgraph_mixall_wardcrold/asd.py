import datetime as dt
from module.code import findnews1
from module.newsdate import whatnow
from module.codename import *
from module.wordsort import makedata,makenewslist
from module.TFIDF import tfidfScorer
from module.listmake import listmakeclass,listmakeday,listmakemouth
from module.datequ import datewhat,datewhatmouth
import json
from konlpy.tag import Okt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

newall = []

daycount=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
daycount1=['15']


for day in daycount1:

    year=2022
    month=10

    for news in news1.keys():  # 대분류 (숫자:이름) ex)

        kinds1 = findnews1(news)  # 대분류 숫자를 대분류 영어로 변환 ex)100>politic1
        news3 = news1['{0}'.format(news)]  # new3는 한글 대분류

        for kind in kinds1.keys():

            kinds3 = kinds1['{0}'.format(kind)]

            with open('./뉴스_날것/{0}_{1}_[{2}_{3}].json'.format(news3, kinds3, month, day), 'r', encoding='UTF-8') as f:
                data = json.load(f)

            newall = newall+list(data.values())

newall2=[]

print('형태소 시작')



okt = Okt()

for i in newall:
    tokens = okt.phrases(i)
    tokens = [token for token in tokens if len(token) > 1]

    newall2.append(tokens)
    print(len(newall2))

newallSe = pd.Series(newall2)

print("tfidf시작")

vectorizer = TfidfVectorizer(max_features= 1000)
X = vectorizer.fit_transform(newallSe)

print('TF-IDF 행렬의 크기 :',X.shape)

lda_model = LatentDirichletAllocation(n_components=48,learning_method='online',random_state=777,max_iter=1)
lda_top = lda_model.fit_transform(X)

terms = vectorizer.get_feature_names()

def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
        print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n - 1:-1]])

get_topics(lda_model.components_,terms)



