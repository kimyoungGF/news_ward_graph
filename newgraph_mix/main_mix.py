import datetime as dt
from module.code import findnews1
from module.newsdate import whatnow
from module.codename import *
from module.wordsort import makedata,makenewslist
from module.TFIDF import tfidfScorer
from module.listmake import listmakeclass,listmakeday
from module.datequ import datewhat


#===========날짜 물어보기========

now,daytimer=datewhat()

#=====분석 종류 물어보기==========

while True:
    print('분야별로 분석하시려면 [class], 날짜별로 분석하시려면 [day]를 입력하여 주십시오.')
    analysis=input()
    if analysis=='class':
        break
    elif analysis=='day':
        break
    else:
        pass

#=========실행=============


for day in range(1, daytimer + 2):

    year, month, day = whatnow(now)

    newword_all = []

    for news in news1.keys(): #대분류 (숫자:이름) ex)

        kinds1 = findnews1(news) #대분류 숫자를 대분류 영어로 변환 ex)100>politic1
        news3 = news1['{0}'.format(news)] # new3는 한글 대분류


        for kind in kinds1.keys():


            kinds3 = kinds1['{0}'.format(kind)]

            corpus = makedata(news3, kinds3, month, day)

            for id, s in enumerate(tfidfScorer(corpus)):
                    newword_all = newword_all + makenewslist(s)

        if analysis=='class':
            listmakeclass(newword_all, month, day,news3,kinds3,analysis)

    if analysis=='day':
        listmakeday(newword_all, month, day,news3,analysis)

    now = now + dt.timedelta(days=1)


