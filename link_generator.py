import urllib2
from bs4 import BeautifulSoup
import csv

urls_collection = []
nlr_volumes = 'https://www.lawnet.gov.lk/new-law-reports/'

page_content = urllib2.urlopen(nlr_volumes)

html_content = BeautifulSoup(page_content, 'html.parser')

links = html_content.select('tr > td > a')

for link in links:
    volume_page_content = urllib2.urlopen(link.get('href'))
    volume_page_html_content = BeautifulSoup(volume_page_content, 'html.parser')
    case_links = volume_page_html_content.select('ul[class=lcp_catlist] > li > a')
    for case_link in case_links:
        urls_collection.append(case_link.get('href'))


with open('cases_links.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(urls_collection)
