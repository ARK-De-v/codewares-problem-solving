def high_and_low(numbers):
    new = list(numbers.split(" "))
    prev =None
    l =[]
    for i in new:
        i = int(i)
        l.append(i)
    return '%i %i'%(max(l),min(l))
    
