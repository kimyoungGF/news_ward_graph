import datetime as dt

def datewhat():
    print("시작 날짜를 입력 하십시오 ex)2000-1-1")
    now=input()
    now=now.split('-')
    now=list(map(int, now))

    print("끝나는 날짜를 입력 하십시오 ex)2000-1-1")
    end=input()
    end=end.split('-')
    end=list(map(int, end))

    now = dt.datetime(now[0],now[1],now[2])
    end = dt.datetime(end[0],end[1],end[2])

    daytimer = end - now
    daytimer = daytimer.days

    return now,daytimer
