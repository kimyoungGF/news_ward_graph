import datetime as dt
import json
import requests
import os
from module.code import findnews1
from module.newsdate import whatnow
from module.newsfind import find
from module.codename import news1
from module.datequ import datewhat

def scrape():
    headers = {'User-Agent': 'Mozilla/5.0(Windows NT 6.1; WOW64: Trident/7.0:rv:11.0)like Gecko'}

    now, daytimer = datewhat()

    print('수집 시작')

    for day in range(1, daytimer + 2):  # 날짜에 +2 만큼 반복
        year, month, day = whatnow(now)

        for news in news1.keys():

            newsdic = {}  # 날것 뉴스 담는 딕셔너리 뉴스제목:뉴스내용

            kinds1 = findnews1(news)


            for kind in kinds1.keys():
                news3 = news1['{0}'.format(news)]
                kinds3 = kinds1['{0}'.format(kind)]

                for page in range(1, 4):
                    url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2={0}&sid1={1}&date={2}{3}{4}&page={5}'.format(
                        kind, news, year, month, day, page)

                    site = requests.get(url, headers=headers)
                    source_data = site.text

                    count = source_data.count('<dt class="photo">')

                    for i in range(count):
                        source_data, newsdic = find(source_data, newsdic)

                if not os.path.exists('./뉴스_날것/'):
                    os.mkdir('./뉴스_날것/')

                with open('./뉴스_날것/{0}_{1}_[{2}_{3}].json'.format(news3, kinds3, month, day), 'w',
                          encoding='UTF-8') as f:
                    json.dump(newsdic, f, ensure_ascii=False, indent=4)
                print("대분류 = {0}, 소분류 = {1}, 날짜 = {2}_{3}".format(news3, kinds3, month, day))
        now = now + dt.timedelta(days=1)
