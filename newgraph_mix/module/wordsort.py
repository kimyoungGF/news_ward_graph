import json


# =====================================단어 정렬=======================================================


def makedata(news, kinds, month, days):  # 리스트파일 불러오기
    with open('D:\\뉴스_날것\\{0}_{1}_[{2}_{3}].json'.format(news, kinds, month, days), 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data


def makenewslist(s):  # 뉴스 단어 리스트에 추가

    id_list = []
    wordrank = sorted(s, key=lambda x: x[1], reverse=True)

    try:
        for i in range(0, 10):
            a = (wordrank[i])[0]
            id_list.append(a)

        return id_list
    except:
        return id_list


def findbest(wordall):  # 단어 2글자 이상만 찾고 빈도수 리스트 만들어서 정렬
    newswords = []
    vocab = {}
    result = []

    for word in wordall:
        if len(word) >= 2:
            result.append(word)
            if word not in vocab:
                vocab[word] = 0
            vocab[word] += 1
    newswords.append(result)
    a = sorted(vocab.items(), key=lambda x: x[1], reverse=True)

    return a
