import datetime as dt
from module.code import findnews1
from module.newsdate import whatnow
from module.codename import *
from module.wordsort import makedata,makenewslist
from module.TFIDF import tfidfScorer
from module.listmake import listmakeclass,listmakeday,listmakemouth
from module.datequ import datewhat,datewhatmouth



def analysis():

    while True:
        print('분야별로 분석하시려면 [class], 날짜별로 분석하시려면 [day], 한달치를 분석하시려면[month] 입력하여 주십시오.하루데이터를 기반으로 LDA는 [LDA]')
        analysis = input()
        if analysis == 'class':
            break
        elif analysis == 'day':
            break
        elif analysis == 'month':
            break
        elif analysis == 'LDA':
            break
        else:
            pass




    # =========실행=============

    if analysis == 'month':

        now,mouthdaycount=datewhatmouth()
        newword_month = []

        for daycount in range(1, mouthdaycount):

            year, month, day = whatnow(now)

            for news in news1.keys():  # 대분류 (숫자:이름) ex)

                kinds1 = findnews1(news)  # 대분류 숫자를 대분류 영어로 변환 ex)100>politic1
                news3 = news1['{0}'.format(news)]  # new3는 한글 대분류

                for kind in kinds1.keys():

                    kinds3 = kinds1['{0}'.format(kind)]

                    corpus = makedata(news3, kinds3, month, day)

                    for id, s in enumerate(tfidfScorer(corpus)):

                        newslist = makenewslist(s)

                        newword_month = newword_month + newslist

            print(day)
            now = now + dt.timedelta(days=1)

        listmakemouth(newword_month, month)






    elif analysis == 'day'or'class':

        now, daytimer = datewhat()

        for day in range(1, daytimer + 2):

            year, month, day = whatnow(now)

            newword_all_day = []

            for news in news1.keys():# 대분류 (숫자:이름) ex)




                newword_all_class = []

                kinds1 = findnews1(news)  # 대분류 숫자를 대분류 영어로 변환 ex)100>politic1
                news3 = news1['{0}'.format(news)]  # new3는 한글 대분류

                for kind in kinds1.keys():


                    kinds3 = kinds1['{0}'.format(kind)]


                    corpus = makedata(news3, kinds3, month, day)


                    for id, s in enumerate(tfidfScorer(corpus)):

                        newslist=makenewslist(s)

                        if analysis == 'day':
                            newword_all_day = newword_all_day + newslist

                        else:
                            newword_all_class = newword_all_class + newslist



                if analysis == 'class':
                    listmakeclass(newword_all_class, month, day,news3)


            if analysis == 'day':
                listmakeday(newword_all_day, month, day)

            now = now + dt.timedelta(days=1)

    else:

        now, mouthdaycount = datewhatmouth()

        newword_month = []


        for daycount in range(1, mouthdaycount):

            newword_day = []

            year, month, day = whatnow(now)

            for news in news1.keys():  # 대분류 (숫자:이름) ex)

                kinds1 = findnews1(news)  # 대분류 숫자를 대분류 영어로 변환 ex)100>politic1
                news3 = news1['{0}'.format(news)]  # new3는 한글 대분류

                for kind in kinds1.keys():

                    kinds3 = kinds1['{0}'.format(kind)]

                    corpus = makedata(news3, kinds3, month, day)

                    for id, s in enumerate(tfidfScorer(corpus)):
                        newslist = makenewslist(s)

                        newword_day = newword_day + newslist

            print(day)
                now = now + dt.timedelta(days=1)






    print('프로그램 끝')