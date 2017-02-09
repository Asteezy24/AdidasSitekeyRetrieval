from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen
import urllib2

def getSitekey():
    url = "http://www.adidas.com/us/men-shoes?sz=120&start=0"
    shoeLinks = []
    keyword_for_sitekey = 'data-sitekey'
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib2.urlopen(req)
    soup = BeautifulSoup(con, "html.parser")
    data = soup.findAll('div', {'class':'image plp-image-bg'})

    for item in data:
        link = item.find('a')['href']
        shoeLinks.append(link)

    for link in shoeLinks:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            'Accept': 'text/html, application/xhtml+xml, application/xml',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
            'DNT': '1'
        })
        response = session.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        sitekeyDiv = soup.findAll(attrs={"class": "g-recaptcha"})
        print "Currently checking for sitekey on " + link
        if sitekeyDiv:
            print "\nFound Sitekey on " + link + "\n\n\n"
            print "Current Sitekey = " + sitekeyDiv[0]['data-sitekey']
            break
            
        else:
            continue
    print "Sitekey not found."

if __name__ == "__main__":
    getSitekey()
