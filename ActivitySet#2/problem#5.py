

def get_cs():
    """get string input"""
    s = input("Enter string: ")
    return s



def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    dic={}
    cs=cs.split(";")
    for i in cs:
        i = i.split("=")
        dic[i[0]]=i[1]
    return dic


def dict_to_cs(d):
    """convert a dictionary to connect string"""
    l=' '
    for i in d:
        l+= i+"="+d.get(i)+";"

    return l


def main():
    cs = get_cs()

    d =  cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
