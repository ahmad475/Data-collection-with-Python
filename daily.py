from pytrends.request import TrendReq
from datetime import date, timedelta
import pandas as pd

x=2015
df = pd.DataFrame()
c3=str(x)+'-06-01 '+ str(x)+'-09-18'

while(x<=2022):
    c=str(x)+'-01-01 '+ str(x)+'-05-31'
    c1=str(x)+'-06-01 '+ str(x)+'-12-31'
    c3=str(x)+'-06-01 '+ str(x)+'-09-18'
    pytrends = TrendReq(hl='en-US')
    keyword = ['bitcoin']
    if x==2015:
        pytrends.build_payload(keyword, timeframe=c)
        df = pytrends.interest_over_time()
    else:
        pytrends.build_payload(keyword, timeframe=c)
        df = pd.concat([df,pytrends.interest_over_time()])
    if x==2022:
        pytrends.build_payload(keyword, timeframe=c3)
        df = pd.concat([df,pytrends.interest_over_time()])
    else:
        pytrends.build_payload(keyword, timeframe=c1)
        df = pd.concat([df,pytrends.interest_over_time()])
    x+=1
df.to_csv('daily_info.csv',header=True)
