fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    t=line.rstrip().split()
    for element in t:
     if element not in lst:
      lst.append(element)
    else:
        continue
lst.sort() 
print(lst)
