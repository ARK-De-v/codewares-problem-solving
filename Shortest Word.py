def find_short(s):
    a =s.split(" ")
    d = [len(i) for i in a[0:]]
    l =min(d)
    return l
