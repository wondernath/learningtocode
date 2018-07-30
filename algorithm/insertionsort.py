def ist():
    thelst = list(map(int, input().split()))
    for each1 in range(1, len(thelst)):
        for each2 in range(each1-1, -1, -1):
            if thelst[each1] < thelst[each2]:
                thelst[each1] = thelst[each1] + thelst[each2]
                thelst[each2] = thelst[each1] - thelst[each2]
                thelst[each1] = thelst[each1] - thelst[each2]
    return thelst

print (ist())
