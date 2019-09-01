import json
import urllib.request as url

data = json.load(url.urlopen('https://newsapi.org/v2/everything?q=apple&from=2019-08-31&to=2019-08-31&sortBy=popularity&apiKey=695e07af402f4b119f0703e9b19f4683'))

articles = data['articles']
for i in range(len(articles)):
    title = articles[i]['title']
    print(title)
