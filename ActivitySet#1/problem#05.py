def inpuy():
    s=float(input('Enter values'))
    return s 

def compute(score):
    if score>1.0 or score<0.1:
     print("Marks entered out of range")
     quit()
    elif score>=0.9:
     grade="A"
    elif score>=0.8:
        grade="B"
    elif score>=0.7:
     grade="C"
    elif score>=0.6:
     grade="D"
    elif score<0.6:
     grade ="F"
    return grade

def output(grade):
    print(grade)

def main():
    score=inpuy()
    grade=compute(score)
    output(grade)

if __name__=="__main__":
    main()
