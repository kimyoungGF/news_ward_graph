from module.wordgrape import makegraghday,makegraghclass,makegraghmouth
from module.wordsort import findbest
from module.wordcloud import wordcloud_day,wordcloud_class,wordcloud_mouth


def listmakeday(newword_all,month,day):

    bestlist = findbest(newword_all)


    #wordcloud_day(bestlist,month,day)
    word1 = []
    word2 = []
    worddic={}
    for i in range(0, 10):
        word1.append((bestlist[i])[0])
        word2.append((bestlist[i])[1])

    for i in range(0, len(bestlist)):
        worddic[((bestlist[i])[0])] =((bestlist[i])[1])

    wordcloud_day(worddic,month,day)



    makegraghday(word1, word2, month, day)
    print("{0}월{1}".format(month, day))



def listmakeclass(newword_all,month,day,new):
    bestlist = findbest(newword_all)
    word1 = []
    word2 = []
    worddic = {}
    for i in range(0, 10):
        word1.append((bestlist[i])[0])
        word2.append((bestlist[i])[1])

    for i in range(0, len(bestlist)):
        worddic[((bestlist[i])[0])] =((bestlist[i])[1])

    wordcloud_class(worddic, month, day, new)


    makegraghclass(word1,word2,month,day,new)
    print("{0}_{1}월{2}".format(new,month,day))


def listmakemouth(newword_all,month):
    bestlist = findbest(newword_all)
    word1 = []
    word2 = []
    worddic = {}
    for i in range(0, 10):
        word1.append((bestlist[i])[0])
        word2.append((bestlist[i])[1])

    for i in range(0, len(bestlist)):
        worddic[((bestlist[i])[0])] =((bestlist[i])[1])

    wordcloud_mouth(worddic, month)
    makegraghmouth(word1,word2,month)

    print("{0}월".format(month))