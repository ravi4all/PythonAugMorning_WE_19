import bs4
import urllib.request as url

req = url.urlopen('https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0&otracker1=AS_Query_TrendingAutoSuggest_1_0&as-pos=1&as-type=HISTORY&suggestionId=tv&requestId=23e8c5bd-2e75-43c9-bd13-6e187376dea4&as-backfill=on')

pageSource = bs4.BeautifulSoup(req,'lxml')

titleDiv = pageSource.find_all('div',class_='_3wU53n')
priceDiv = pageSource.find_all('div',class_='_1vC4OE _2rQ-NK')

for i in range(len(titleDiv)):
    print(titleDiv[i].text)
    print(priceDiv[i].text)
    print("-------------------------")
