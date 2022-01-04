def unique_in_order(iterable):
    l =[]
    prev =None
    for i in iterable:
        if i != prev:
            l.append(i)
        prev =i
    return l
