# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from msilib import sequence
from turtle import position
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=input('Enter Repeat no of times: ')
position=int(input('Enter position:'))-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
Sequence = []
# Retrieve all of the anchor tags
href=soup('a')

for i in range(count):
    link=href[position].get('href',None)
    print ("retriving:",link)
    Sequence.append(href[position].contents[0])
    html=urllib.urlopen(link).read()
    soup=BeautifulSoup(html,"html.parser")
    href=soup('a')
    link=href[position].get('href',None)
print(Sequence[-1])