

# def get_cs():
#     """get string input"""
  


# def cs_to_lot(cs):
#     """convert connected string to list of strings"""


# def lot_to_cs(lot):
#     """convert list of strings to connected string"""


# def main():
#     cs=get_cs()

#     lot=cs_to_lot(cs)  # convert connect string to list of tuples
#     print(lot)

#     cs=lot_to_cs(lot)  # convert list of strings to connect string
#     print(cs)


# if __name__ == '__main__':
#     main()

def get_cs():
    s = input("Enter string: ")
    return s


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    l = []
    cs = cs.split(";")
    for i in cs:
        i = tuple(i.split("="))
        l.append(i)
    return l


def lot_to_cs(lot):
    """convert list of strings to connected string"""

    l = ' '
    for i in lot[:3]:
        l += i[0] + "=" + i[1] + "; "
    for i  in lot[3:]:
        l += i[0] + "=" + i[1]

    return (l)


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs = lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
