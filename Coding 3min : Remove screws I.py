def sc(s):
    sum =0
    prev =None
    for i in s:
        if prev !=None and i!= prev:
            sum += 5
        sum+=2
        prev =i
    return sum-1
