from datetime import date
def countdown(date_begin,date_end):
    t = date_begin.year*365-date_end.year*365 + (date_begin.month*30-date_end.month*30) + (date_begin.day-date_end.day)
    return t
print(countdown(date(2022,1,5),date(2008,5,5)))


    
    
    
