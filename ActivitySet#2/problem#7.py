

class Menu:
    """fill in class definition here"""
    def __add__(self,item,price):
        self.item=item
        self.price=price
        return self.item+self.price

    



m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
