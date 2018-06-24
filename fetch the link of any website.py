import bs4 as bs
from pprint import pprint
import urllib.request
sauce=urllib.request.urlopen('http://www.lpu.in').read()
soup = bs.BeautifulSoup(sauce,'lxml')
print(soup.title.text)
for url in soup.find_all('a'):
	print(url.get('href'))
