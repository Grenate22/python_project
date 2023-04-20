import requests
from bs4 import BeautifulSoup

url='https://www.coindesk.com/price/bitcoin/'
res=requests.get(url)
soup=BeautifulSoup(res.content,'html.parser')
html_element=soup.find('span',{'class':'currency-pricestyles__Price-sc-1rux8hj-0 jIzQOt'})
print(html_element.text)