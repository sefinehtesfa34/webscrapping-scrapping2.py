
import requests
from bs4 import BeautifulSoup
import re
URL='https://tzadmission.net/addis-ababa-university-courses-offered/'
page=requests.get(URL)
soup=BeautifulSoup(page.content, 'html.parser')
phdCoursesList=soup.find(id='sidebar-primary')
text=phdCoursesList.get_text().strip()
text=text.split("Regular")
with open('phd.txt','w') as file:
    for  i in text:
        result  = " ".join(i.split())
        index=result.find("(")
        result=result[:index]
        
        file.write(result+"\n")
    