# Network Programming
# https://www.py4e.com/lessons/network
import urllib.request, urllib.parse, urllib.error

 img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
 fhand = open('cover3.jpg', 'wb')
 fhand.write(img)
 fhand.close()

 import socket

 mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 mysock.connect(('data.pr4e.org', 80))
 cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
 mysock.send(cmd)

 while True:    data = mysock.recv(512)
     if len(data) < 1:
         break
     print(data.decode(),end='')

 mysock.close()