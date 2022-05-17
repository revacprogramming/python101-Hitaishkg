name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d=dict()
big=int(0)
for line in handle:
    words=line.split()
    if len(words) < 3 or words[0] != "From" : continue
    words=words[1]
    if words not in d:
        d[words]=1
    else :
        d[words]+=1
    d[words]=int(d[words])
    
maxx=0
value=""
for i in d:
    if (d[i])>maxx:
        maxx=d[i]
        value=i
print(value,maxx)