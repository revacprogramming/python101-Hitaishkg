# Variables, Expressions & Statements

def inpuy():
    s = input("Enter values:")
    return s

def compute(hrs,rate_perhr):
    gross_pay= (float(hrs) * float(rate_perhr))
    return gross_pay
    
def main():
    hrs=inpuy()
    rate_perhr=inpuy()
    gross_pay=compute(hrs,rate_perhr)
    print(gross_pay)


if __name__=="__main__":
    main()
    

