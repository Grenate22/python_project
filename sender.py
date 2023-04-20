from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.zoominfo.com/c/deloitte-touche-tohmatsu-ltd/14812699').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace('  ', '')
    when_posted = job.find('span', class_='sim-posted').text

    print(f'''
    company_name : {company_name}
    skills : {skills}
    when_posted : {when_posted}

    ''')