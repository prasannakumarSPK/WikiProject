 
# we scrape 1. content 2. urls 3. tables

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://en.wikipedia.org/wiki/Sachin_Tendulkar").read()
soup = bs.BeautifulSoup(sauce,'lxml')
 
# print(soup.p)

# lst=soup.find_all('p')
# for e in lst:
# 	print(e.string)#if child tags  exist we get none
# 	print(e.text)
# 	print("/////////")

# print(soup.get_text()) #we get all the text in webpage

# for url in soup.find_all('a'):
# 	print(url.text+" "+url.get('href'))

# nav = soup.nav

# for url in nav.find_all('a'):
# 	print(url.get('href'))

# to get text only in body//////
# body = soup.body

# for para in body.find_all('p'):
# 	print(para.text)

# for div in soup.find_all('div',class_='body'):
# 	print(div.text) 





# x = soup.find("div", {"id": "bodyContent"})
# print(x)



# for para in soup.find_all('div',class_='mw-parser-output'):
# 	print(para.text)


for data in soup.find_all('div',class_='mw-parser-output'):
	# print(para.text)
	for p in data.find_all('p'):
		print(p.text)
		for url in p.find_all('a'):
			print(url.text+"     "+"link is:"+"https://en.wikipedia.org"+url.get('href'))
		print("////////////////////////////////////////////")

# for url in soup.find_all('a'):
# 	print(url.text+" "+url.get('href'))
