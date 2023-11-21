ten=[]
for i in range (1,10):
    ten.append(i)

def whatnow(d):
    year = str(d.year)
    if d.month in ten: 
        month ="0{0}".format(str(d.month))   
    else:
        month =str(d.month)

    if d.day in ten: 
        day ="0{0}".format(str(d.day))   
    else:
        day =str(d.day)
  
    return (year,month,day)
