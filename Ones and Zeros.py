def binary_array_to_number(arr):
    res =0
    l = [ i for i in reversed(arr)]
    for a in range(len(l)):
        if l[a]==1:
            res += 2 **a 
    return res
print(binary_array_to_number([0, 0, 1, 0]))
