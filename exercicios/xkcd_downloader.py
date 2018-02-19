#baixa tds os quadrinhos do site xkcd
import requests
import bs4
import os

url_base = 'http://xkcd.com'              # starting url
url=url_base+'/1526'
os.makedirs('xkcd', exist_ok=True)   # store comics in xkcd



while not url.endswith('#'):
    #Download the page.
    res = requests.get(url=url)
    xkcd_soup=bs4.BeautifulSoup(res.text,'lxml')

    #Find the URL of the comic image.
    comic_link = xkcd_soup.select('div #comic img')
    if not comic_link:
        print('oops')

    else:

        comic_title = comic_link[0].get('alt')
        comic_link = url+comic_link[0].get('src')
        if not comic_title:
            print('ooops')
            comic_title='erro'
        else:
            comic_title=comic_title.replace('/','')

        #print(comic_link)

        #Download and save the image to xkcd.
        img_path = 'xkcd/'+comic_title
        if os.path.exists(img_path):
            print(comic_title+' já foi baixado')
        else:
            print('baixando:'+comic_title)
            img_raw = requests.get(comic_link)
            f=open(img_path,'wb')
            f.write(img_raw.content)
            print('feito')
            f.close()

    #Get the Prev button's url.
    comicNav=xkcd_soup.select('.comicNav li > a')
    print('faltam:'+comicNav[1].get('href'))
    prev_url=url_base+comicNav[1].get('href')
    url=prev_url



print('Done.')
