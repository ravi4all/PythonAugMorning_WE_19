import bs4
import urllib.request as url

# Step 1 - hit the url from where you want to fetch data
req = url.urlopen('https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0&otracker1=AS_Query_TrendingAutoSuggest_1_0&as-pos=1&as-type=HISTORY&suggestionId=tv&requestId=23e8c5bd-2e75-43c9-bd13-6e187376dea4&as-backfill=on')
#print(req)

# Step 2 - pass the req to beautiful soup and it will return full page source
pageSource = bs4.BeautifulSoup(req,'lxml')

# Step 3 - now from page Source find the required tag and it will return html
# code of that tag
titleDiv = pageSource.find('div',class_='_3wU53n')
#print(titleDiv)

# Step 4 - last step is to fetch text part from the tag
text = titleDiv.text
print(text)
