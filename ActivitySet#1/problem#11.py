fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

count = 0
fh = open(fname)
for k in fh:
    if k.startswith('From:'):
            continue
    if  k.startswith('From'):               
     	word=k.split()
     	print(word[1])
     	count=count+1
            

print("There were ", count, "lines in the file with From as the first word ")
