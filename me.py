import sys
import os.path

import urllib2
import BeautifulSoup
import requests
from urllib2 import urlparse
import shutil

website = sys.argv[1:]
print website
def download(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)

def remove_html_tags(text):
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
                os.makedirs(dir)

request = urllib2.Request(website[0])

o = urlparse.urlsplit(website[0]).path.split('/')[2]

assure_path_exists('./music/' + o + '/')

response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)
for a in soup.findAll('a'):
  if '.mp3' in a['href']:
    newTitle = urllib2.unquote(a['href'])
    Mp3ToDownload = website[0] + a['href']
    print 'Downloading ' + newTitle
    download(Mp3ToDownload, './music/' + o + '/' + newTitle)