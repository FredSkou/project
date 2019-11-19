def large_sum():
    n = 2**1000
    list=[]
    ns = str(n)
    total = 0
    for dig in ns:
        list.append(dig)
        total+=int(dig)
    print(list)
    print(total)

large_sum()
