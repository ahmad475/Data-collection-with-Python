from pytrends.request import TrendReq
from datetime import date, timedelta
import pandas as pd

start_date = date(2015, 1, 5) 
end_date = date(2015, 6, 14)    # perhaps date.now()
df = pd.DataFrame()
df2 = pd.DataFrame()
week = 1
c='2015-01-01 2015-01-04'
pytrends = TrendReq(hl='en-US')
keyword = ['bitcoin']
pytrends.build_payload(keyword, timeframe=c)
df = pd.concat([df,pytrends.interest_over_time()])
df["Week"] = "week " + str(week)
df2 = df



delta = end_date - start_date   # returns timedelta
print("Made it")
p = 0
for i in range(0,(delta.days + 1),7):
    week+=1
    
    day1 = start_date + timedelta(days=i)
    day2 = day1 + timedelta(6)
    print(str(day1)+" "+str(day2))
    c = str(day1)+" "+str(day2)
    pytrends = TrendReq(hl='en-US')
    keyword = ['bitcoin']
    pytrends.build_payload(keyword, timeframe=c)
    df = pytrends.interest_over_time()
    df["Week"] = "week" + str(week)
    df2 = pd.concat([df2,df])
    
    

df2.to_csv('weekly_info.csv',header=True)