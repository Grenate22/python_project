import requests
from bs4 import BeautifulSoup
response=requests.get('https://en.wikipedia.org/wiki/List_of_capitals_of_states_of_Nigeria')
print(response.status_code)
if response.status_code==200:
    soup=BeautifulSoup(response.content,'html.parser')
    dict={}
    for tr in soup.find_all('tr'):
        print((tr.text))