import requests
from bs4 import BeautifulSpoup
from csv import writer
url=('https://icog-makers.com/my-projects/')
page=requests.get(url)
soup=BeautifulSpoup(page.content,'html.parser').text
lists=soup.find_all('section',class_='listing-search-item').text
with open("scrapping.csv","w") as f:
	thewriter=writer(f)
	header=['Title','Price','Location','Area']
	thewriter.writerow(header)
	for list in lists:
		title=list.find('a',class_='listing-search-item_link--title').text
		location=list.find('div',class_='listing-search-item_location').text
		price=list.find('span',class_='listing-search-item_price').text
		area=list.find('span',class_='listing-search-item_description').text
		info=[title, location, price, area]
		thewriter.writerow(header)
	

