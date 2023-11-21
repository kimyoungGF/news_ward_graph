from module.analysis import analysis
from module.scrape import scrape


#============수집인지 분석인지 물어보기============
while True:
    print('뉴스를 수집하시려면 [수집], 분석하시려면 [분석]을 입력하여 주십시오')
    SnA=input()
    if SnA == '수집':
        scrape()
        break
    elif SnA == '분석':
        analysis()
        break
    else:
        print('잘못입력하셨습니다.')
        pass



