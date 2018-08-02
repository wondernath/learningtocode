from timeit import timeit

@timeit
def bubblesort():
    alist = list(map(int, input().split()))
    swapped = True
    while swapped:
        swapped = False
        for each in range(len(alist)-1, 0, -1):
            if alist[each] < alist[each-1]:
                swapped=True
                alist[each], alist[each-1] = alist[each-1], alist[each]
    return alist

print (bubblesort())
