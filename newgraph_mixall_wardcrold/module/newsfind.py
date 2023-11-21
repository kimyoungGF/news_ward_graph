from newspaper import Article
import time

#========================뉴스 찾아서 저장=====================
def find(data,dic): #제목 찾아서 링크로 들어가기
    pos1 = data.find('<dt class="photo">')
    data = data[pos1:]

    pos2 = data.find('<a href="')+len('<a href="')
    data = data[pos2:]

    pos3 = data.find('">')
    extract_data = data[: pos3]
    extract_data = extract_data.strip()

    data = data[pos3+4:]
    
    extract_data=extract_data.replace('&#034;', '')
    extract_data=extract_data.replace('&#039;', '')
    extract_data=extract_data.replace('\n\n;', '')
    
    url = extract_data
    
    
    article = Article(url, language='ko')


    while True:
        try:
            article.download()
            article.parse()
            break
            
        except:
            print('errer')
            time.sleep(5)
        
        
    
    
    dic[article.title]=article.text
    
    return data, dic


