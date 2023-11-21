import matplotlib
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
matplotlib.use('Agg')


def wordcloud_day(list,month, day):
    wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
    gen = wc.generate_from_frequencies(list)
    plt.figure()
    plt.imshow(gen)
    os.makedirs("./뉴스_워드클라우드_하루별/{0}".format(month, day), exist_ok=True)
    wc.to_file('./뉴스_워드클라우드_하루별/{0}/{0}월{1}일.png'.format(month, day))

    plt.close()

def wordcloud_class(list, month, days,news):
    wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
    gen = wc.generate_from_frequencies(list)
    plt.figure()
    plt.imshow(gen)
    os.makedirs("./뉴스_워드클라우드_분야별/{0}/{1}".format(news, month), exist_ok=True)
    wc.to_file('./뉴스_워드클라우드_분야별/{0}/{1}/{0}_{1}월{2}일.png'.format(news, month, days))

    plt.close()

def wordcloud_mouth(list,month):
    wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
    gen = wc.generate_from_frequencies(list)
    plt.figure()
    plt.imshow(gen)
    os.makedirs("./뉴스_워드클라우드_한달별",exist_ok=True)
    wc.to_file('./뉴스_워드클라우드_한달별/{0}월.png'.format(month))

    plt.close()