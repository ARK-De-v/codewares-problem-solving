def descending_order(num):
    if num== 0:
        return 0
    if num> 0:
        return int("".join(sorted([i for i in str(num)],reverse = True)))
