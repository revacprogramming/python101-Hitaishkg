# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
      count=count+1
      l=line.find("0")
      number=float(line[l:])
      total=total+number
avg=total/count
print("Average spam confidence:",avg)