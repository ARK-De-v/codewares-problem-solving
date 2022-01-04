def narcissistic( value ):
    val = [ int(i) for i in str(value)]
    x =sum( a ** len(val) for a in val)
    if x == value:
        return True
    else :
        return False
