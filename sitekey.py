from bs4 import BeautifulSoup
import requests, time

def getSitekey():
    url = "http://www.adidas.com/us/men-shoes?sz=120&start=0"
    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Accept': 'text/html, application/xhtml+xml, application/xml',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
        'DNT': '1'
    })
    shoeLinks = []
    keyword_for_sitekey = 'data-sitekey'
    r = session.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.findAll('div', {'class':'image plp-image-bg'})

    for item in data:
        link = item.find('a')['href']
        shoeLinks.append(link)

    for link in shoeLinks:
        response = session.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        sitekeyDiv = soup.findAll(attrs={"class": "g-recaptcha"})
        print("Currently checking for sitekey on {}".format(link))

        if sitekeyDiv:
            print("\nFound Sitekey on {} \n\n\n".format(link))
            print("Current Sitekey = {}".format(sitekeyDiv[0]['data-sitekey']))
            break

        else:
            time.sleep(2)
            continue
    print("Sitekey not found.")

if __name__ == "__main__":
    getSitekey()
