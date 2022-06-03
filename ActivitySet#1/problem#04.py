# Conditional Execution

def inpuy():
    h=float(input('Enters Hours:'))
    return h
def compute(h,r):
    if h<40:
        g=h*r
    else:
        g=40*r
        g=g+((h-40)*(1.5*r))
    return g
def output(g):
    print('gross pay:'+str(g))
    
def main():
    h=inpuy()
    r=inpuy()
    g=compute(h,r)
    output(g)

if __name__=="__main__":
    main()