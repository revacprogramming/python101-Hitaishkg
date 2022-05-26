import re
hand = input("Enter name of the file:")
fh=open(hand).read()
x=re.findall('[0-9]+',fh)
sum=0
for i in x:
    sum+=int(i)
print(sum)