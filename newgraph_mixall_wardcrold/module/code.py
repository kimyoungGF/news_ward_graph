from module.codename import*

#===============================뉴스 분류=====================

def findnews1(news):
    if news == '100':
        return politic1

    elif news == '101':
        return economy1

    elif news == '102':
        return society1

    elif news == '103':
        return culture1

    elif news == '104':
        return world1

    else:
        return science1

    

