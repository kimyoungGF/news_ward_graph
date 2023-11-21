import matplotlib
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm


# =========================단어 그래프=============================================

def makegragh(wordx, wordy,stork):  # 그래프 만들어서 저장
    ##font_location = "C:\\Users\\sw-107\\Documents\\김영욱\\malgun.ttf"
    font_location = "D:\\malgun.ttf"
    font_name = fm.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.bar(wordx, wordy)

    for i, v in enumerate(wordx):
        plt.text(v, wordy[i], wordy[i],
                 fontsize=9,
                 color='blue',
                 horizontalalignment='center',
                 verticalalignment='bottom')


    os.makedirs(".\\{0}\\{1}".format(news,stork), exist_ok=True)
    plt.savefig('.\\{0}\\{1}\\.png'.format(news,stork))

    plt.close()


