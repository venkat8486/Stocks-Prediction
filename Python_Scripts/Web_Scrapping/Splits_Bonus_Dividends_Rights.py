import pandas as pd
for year in range(2020, 1999,-1):
    for category in ['bonus', 'dividends_declared']:
        try:
            url = 'https://www.moneycontrol.com/stocks/marketinfo/'+category+'/index.php?sel_year='+str(year)
            df = pd.read_html(url, attrs={'class':'b_12 dvdtbl'})[0]
            df.to_csv(category+'_'+str(year)+'.txt', index=False, sep='|', quoting=1)
        except Exception as e:
            raise#print(year, category, url)

    for category in ['splits', 'rights']:
        try:
            url = 'https://www.moneycontrol.com/stocks/marketinfo/'+category+'/index.php?sel_year='+str(year)
            df = pd.read_html(url, attrs={'class':'b_12 dvdtbl tbldata14'})[0]
            df.to_csv(category+'_'+str(year)+'.txt', index=False, sep='|', quoting=1)
        except Exception as e:
           raise # print(year, category, url)