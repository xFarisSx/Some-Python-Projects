import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
import lxml

job_titles = []
company_names = []
locations_names = []
links = []


result = requests.get('https://wuzzuf.net/search/jobs/?q=python&a=hpb')

src = result.content

soup = BeautifulSoup(src, 'lxml')

job_title = soup.find_all('h2',{"class":"css-m604qf"})
company_name = soup.find_all('a', {'class':'css-17s97q8'})
locations_name = soup.find_all('span', {'class':'css-5wys0k'})



for i in range(len(job_title)):
    job_titles.append(job_title[i].text)
    links.append(job_title[i].find('a').attrs['href'])
    company_names.append(company_name[i].text)
    locations_names.append(locations_name[i].text)

file_list = [job_titles,company_names,locations_names,links]
exported = zip_longest(*file_list)
with open('jobtest.csv', 'w') as file:
    wr = csv.writer(file)
    wr.writerow(['job title','company name','location','links'])
    wr.writerows(exported)