# Databases
# https://www.py4e.com/lessons/database
from itertools import count
import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET


url = input("Enter location: ")
print ("Retrieving " + url)

xml=urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('comments/comment')
print( "Count: " + str(len(counts)))

sum=0
coun=0

for item  in counts:
    x =item.find('count').text
    sum=sum+int(x)
    coun+=1      

print ("Sum:" + str(sum))
print('count', coun)

    