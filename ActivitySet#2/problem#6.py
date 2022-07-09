class Menu(dict):
    """fill in class definition  here"""
    def __init__(self) -> None:
        self=dict()

    def add(self,item,price):
        self[item]=price

    def show(self):
        l = ' '
        for i  in self:
            l += i+" "+str(self.get(i))
            x=l[:8]
            y=l[8:]
        print(x)
        print(y)


m = Menu()  # Menu is a class
m.add('idly', 10)
m.add('vada', 20)
m.show()