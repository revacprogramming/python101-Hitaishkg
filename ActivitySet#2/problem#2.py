

def add(a, b):
    pass  # ...


def output(a, b, sum):
    pass  # ...

def main():
    a,b = map(int,input('Enter the values: ').split())
    sum = (a+b)

    output(a, b, sum)
    print(a,"+ ", b, 'is ', sum)

if __name__ == '__main__':
    main()
