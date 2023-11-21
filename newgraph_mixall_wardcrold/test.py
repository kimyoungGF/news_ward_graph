import json
import pandas as pd
import nltk

# =====================================단어 정렬=======================================================



with open('./뉴스_날것/IT_과학_IT 일반_[10_01].json', 'r', encoding='UTF-8') as f:
    data = json.load(f)


data=list(data.values())



print(data[0])
