import requests
import csv
from bs4 import BeautifulSoup

url_vienna = 'https://twincityliner.com/en/content/vienna-bratislava'
url_brat = 'https://twincityliner.com/en/content/bratislava-vienna'

r = requests.get(url_vienna)
s = requests.get(url_brat)
soup = BeautifulSoup(r.content, 'html.parser')
soup2 = BeautifulSoup(s.content, 'html.parser')
parser = soup.find('div', attrs = {'id':'mobil-preise'})
parser2 = soup2.find('div', attrs = {'id': 'mobil-preise'})

print (parser.text)
print('BRATISLAVA to VIENNA')
print(parser2.text)

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([parser.text, parser2.text])
    