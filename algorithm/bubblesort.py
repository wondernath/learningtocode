def bubble_sort():
    thelist = list(map(int, input('Enter an array:').split(" ")))
    for each1 in range(1, len(thelist)):
        for each2 in range(len(thelist)-1, 0, -1):
            if thelist[each2] < thelist[each2-1]:
                thelist[each2] = thelist[each2]+thelist[each2-1]
                thelist[each2-1] = thelist[each2]-thelist[each2-1]
                thelist[each2] = thelist[each2]-thelist[each2-1]
    return thelist

print (bubble_sort())
