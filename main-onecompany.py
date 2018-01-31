import urllib.request
from bs4 import BeautifulSoup
quote_page = 'https://www.bloomberg.com/quote/DWDP:US'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'companyName__99a4824b'})
name = name_box.text.strip()
print(name)
price_box = soup.find('div', attrs={'class':'overviewRow__0956421f'})
price = price_box.text
print(price)
print('data from bloomberg, made by qurt')
# most of code copied from https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#this program uses the GPLv3 license
