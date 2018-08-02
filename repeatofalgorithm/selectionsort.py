from timeit import timeit

@timeit
def selectionsort():
    alist = list(map(int, input().split()))
    for each in range(len(alist)):
        minm = min(alist[each:])
        minm_ind = alist.index(minm, each)
        if alist[each] > minm:
            alist[each], alist[minm_ind] = alist[minm_ind], alist[each]
    return alist
    
print (selectionsort())
