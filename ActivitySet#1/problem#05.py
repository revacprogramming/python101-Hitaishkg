score = input("Enter Score: ")
score=float(score)
if score>1.0 or score<0.1:
    print("Marks entered out of range")
    quit()
elif score>=0.9:
    print("A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("c")
elif score>=0.6:
    print("D")
elif score<0.6:
    print("F")