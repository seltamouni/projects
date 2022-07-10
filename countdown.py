from datetime import date
def countdown(date_begin,date_end):
    t = date_begin.year*365-date_end.year*365 + (date_begin.month*30-date_end.month*30) + (date_begin.day-date_end.day)
    year = t//365
    month = (t%365)//30
    days= (t%365)%30
     
    return (f"date({year,month,days}")
print(countdown(date(2022,1,5),date(2008,5,5)))


    
    
    
