def unique_in_order(iterable):
    first=0
    res=[]
    l=len(iterable)
    print(l)
    while (first<l):
        for i in iterable[first+1:]:
            print(iterable[first])
            print(i)
            if not iterable[first]==i:
                res.append(iterable[first])
                first=iterable.index(i)
                print(first)
    return res
iterable='AAAABBBCCDAABBB'   
print(unique_in_order(iterable))