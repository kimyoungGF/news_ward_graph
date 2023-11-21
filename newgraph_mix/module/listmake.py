from module.wordgrape import makegragh
from module.wordsort import findbest


def listmakeday(newword_all,month,day,news,analysis,all_category = 1):
    bestlist = findbest(newword_all)
    word1 = []
    word2 = []
    for i in range(0, 10):
        word1.append((bestlist[i])[0])
        word2.append((bestlist[i])[1])

    makegragh(word1, word2, month, day,news,analysis)
    if all_category == 1:
        print("{0}월{1}".format(month, day))
    else:
        print("{0}_{1}월{2}".format(news, month, day))


def listmakeclass(newword_all, month, day, news, kinds,analysis):
    bestlist = findbest(newword_all)
    word1 = []
    word2 = []
    for i in range(0, 10):
        word1.append((bestlist[i])[0])
        word2.append((bestlist[i])[1])
    makegragh(word1, word2, month, day, news,analysis)
    print("{0}_{1}월{2}".format(news, month, day))