# Conditional Execution
hrs = input("Enter Hours:")
h = float(hrs)
perhr=input("Enter rate per hour")
p=float(perhr)
if h<=40:
    gross=h*p

else:
    gross=40*p
    gross=gross +((h-40)*(1.5*p))
    
