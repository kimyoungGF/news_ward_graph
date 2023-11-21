import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm




# =========================단어 그래프=============================================
def makegraghday(wordx, wordy,month,day):  # 그래프 만들어서 저장  수정필요
    ##font_location = "C:\\Users\\sw-107\\Documents\\김영욱\\malgun.ttf"
    font_location = "D:\\파이썬\\malgun.ttf"
    font_name = fm.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.bar(wordx, wordy)

    for i, v in enumerate(wordx):
        plt.text(v, wordy[i], wordy[i],
                 fontsize=9,
                 color='blue',
                 horizontalalignment='center',
                 verticalalignment='bottom')
        plt.xticks(rotation=30, fontsize=7)
        plt.rc('axes', unicode_minus=False)

    os.makedirs("./뉴스_그래프_하루별/{0}".format(month), exist_ok=True)
    plt.savefig('./뉴스_그래프_하루별/{0}/{0}월{1}일.png'.format(month,day))

    plt.close()

def makegraghclass(wordx, wordy, month, days,news):  # 그래프 만들어서 저장
    ##font_location = "C:\\Users\\sw-107\\Documents\\김영욱\\malgun.ttf"
    try:
        font_location = "D:\\파이썬\\malgun.ttf"
        font_name = fm.FontProperties(fname=font_location).get_name()
        matplotlib.rc('font', family=font_name)

        plt.bar(wordx, wordy)

        for i, v in enumerate(wordx):
            plt.text(v, wordy[i], wordy[i],
                     fontsize=9,
                     color='blue',
                     horizontalalignment='center',
                     verticalalignment='bottom')
            plt.xticks(rotation=30, fontsize=7)
            plt.rc('axes', unicode_minus=False)

        os.makedirs("./뉴스_그래프_분야별/{0}/{1}".format(news, month), exist_ok=True)
        plt.savefig('./뉴스_그래프_분야별/{0}/{1}/{0}_{1}월{2}일.png'.format(news, month, days))

        plt.close()
    except Exception as e:
        return


def makegraghmouth(wordx, wordy, month):  # 그래프 만들어서 저장
    ##font_location = "C:\\Users\\sw-107\\Documents\\김영욱\\malgun.ttf"
    font_location = "D:\\파이썬\\malgun.ttf"
    font_name = fm.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.bar(wordx, wordy)

    for i, v in enumerate(wordx):
        plt.text(v, wordy[i], wordy[i],
                 fontsize=9,
                 color='blue',
                 horizontalalignment='center',
                 verticalalignment='bottom')
        plt.xticks(rotation=30, fontsize=7)
        plt.rc('axes', unicode_minus=False)

    os.makedirs("./뉴스_그래프_한달별".format(month), exist_ok=True)
    plt.savefig('./뉴스_그래프_하루별/{0}월.png'.format(month))

    plt.close()


