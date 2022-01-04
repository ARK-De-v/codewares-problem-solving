def max_redigit(num): 
    if 100<=num<=999:
        return int(''.join(sorted(str(num),reverse = True)))
    else: return None