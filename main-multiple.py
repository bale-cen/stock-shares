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
quote_page1 ='https://www.bloomberg.com/quote/NUGYO:TI'
page1 = urllib.request.urlopen(quote_page1)
soup1 = BeautifulSoup(page1, 'html.parser')
name_box1 = soup1.find('h1', attrs={'class': 'companyName__99a4824b'})
name1 = name_box1.text.strip()
print(name1)
price_box1 = soup1.find('div', attrs={'class':'overviewRow__0956421f'})
price1 = price_box1.text
print(price1)
quote_page2 ='https://www.bloomberg.com/quote/AAPL:US'
page2 = urllib.request.urlopen(quote_page2)
soup2 = BeautifulSoup(page2, 'html.parser')
name_box2 = soup2.find('h1', attrs={'class': 'companyName__99a4824b'})
name2 = name_box2.text.strip()
print(name2)
price_box2 = soup2.find('div', attrs={'class':'overviewRow__0956421f'})
price2 = price_box2.text
print(price2)
quote_page3 ='https://www.bloomberg.com/quote/THYAO:TI'
page3 = urllib.request.urlopen(quote_page3)
soup3 = BeautifulSoup(page3, 'html.parser')
name_box3 = soup3.find('h1', attrs={'class': 'companyName__99a4824b'})
name3 = name_box3.text.strip()
print(name3)
price_box3 = soup3.find('div', attrs={'class':'overviewRow__0956421f'})
price3 = price_box3.text
print(price3)
quote_page4 ='https://www.bloomberg.com/quote/INTC:US'
page4 = urllib.request.urlopen(quote_page4)
soup4 = BeautifulSoup(page4, 'html.parser')
name_box4 = soup4.find('h1', attrs={'class': 'companyName__99a4824b'})
name4 = name_box4.text.strip()
print(name4)
price_box4 = soup4.find('div', attrs={'class':'overviewRow__0956421f'})
price4 = price_box4.text
print(price4)
quote_page5 ='https://www.bloomberg.com/quote/AMD:US'
page5 = urllib.request.urlopen(quote_page5)
soup5 = BeautifulSoup(page5, 'html.parser')
name_box5 = soup5.find('h1', attrs={'class': 'companyName__99a4824b'})
name5 = name_box5.text.strip()
print(name5)
price_box5 = soup5.find('div', attrs={'class':'overviewRow__0956421f'})
price5 = price_box5.text
print(price5)
quote_page6 ='https://www.bloomberg.com/quote/NVDA:US'
page6 = urllib.request.urlopen(quote_page6)
soup6 = BeautifulSoup(page6, 'html.parser')
name_box6 = soup6.find('h1', attrs={'class': 'companyName__99a4824b'})
name6 = name_box6.text.strip()
print(name6)
price_box6 = soup6.find('div', attrs={'class':'overviewRow__0956421f'})
price6 = price_box6.text
print(price6)
quote_page7 ='https://www.bloomberg.com/quote/QCOM:US'
page7 = urllib.request.urlopen(quote_page7)
soup7 = BeautifulSoup(page7, 'html.parser')
name_box7 = soup7.find('h1', attrs={'class': 'companyName__99a4824b'})
name7 = name_box7.text.strip()
print(name7)
price_box7 = soup7.find('div', attrs={'class':'overviewRow__0956421f'})
price7 = price_box7.text
print(price7)
quote_page8 ='https://www.bloomberg.com/quote/RHT:US'
page8 = urllib.request.urlopen(quote_page8)
soup8 = BeautifulSoup(page8, 'html.parser')
name_box8 = soup8.find('h1', attrs={'class': 'companyName__99a4824b'})
name8 = name_box8.text.strip()
print(name8)
price_box8 = soup8.find('div', attrs={'class':'overviewRow__0956421f'})
price8 = price_box8.text
print(price8)
print('data from bloomberg, made by qurt')
# most of code copied from https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#this program uses the GPLv3 license
