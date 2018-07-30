def selectionsort():
    thelst = list(map(int, input().split()))
    for each in range(len(thelst)):
        lst = thelst[each:]
        lst_min = min(lst)
        min_ind = thelst.index(lst_min, each)
        if thelst[each] > thelst[min_ind]:
            thelst[each], thelst[min_ind] = thelst[min_ind], thelst[each]
    return thelst

print (selectionsort())
        
