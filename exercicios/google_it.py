import webbrowser
import bs4
import requests
import sys

base_url='https://www.google.com.br/search?q='

def normalize_querry(keywords):
    keywords.replace(' ','+')
    return keywords


def main():
    if len(sys.argv)>2:
        res = requests.get(base_url+normalize_querry(str(sys.argv[2:])))
        if res.status_code==200:
            soup=bs4.BeautifulSoup(res.text,'lxml')
            linkElems = soup.select('.r a')
            numOpen=min(int(sys.argv[1]),len(linkElems))
            for i in range (numOpen):
                webbrowser.open('http://google.com' + linkElems[i].get('href'))
        else:
            print('erro ao pesquisar')
    else:
        print('usage python google_it.py number_results keywords')

if __name__=='__main__':
    main()
