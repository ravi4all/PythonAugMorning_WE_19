import bs4
import urllib.request as url

while True:
    movieName = input("Enter movie name : ")
    movieName = '+'.join(movieName.split())
    req = url.urlopen("https://www.imdb.com/find?ref_=nv_sr_fn&q="+movieName)

    page = bs4.BeautifulSoup(req,'lxml')

    td = page.find('td',class_='result_text')
    a_tag = td.find('a')
    path = "https://www.imdb.com" + a_tag['href']

    req_2 = url.urlopen(path)
    page_2 = bs4.BeautifulSoup(req_2,'lxml')

    title = page_2.find('div',class_='title_wrapper')
    #print(title.text)
    title = ' '.join(title.text.split())
    print(title)
