def insertionsort():
    brownie = list(map(int, input().split()))
    for first in range(len(brownie)):
        ind = first
        for second in range(first-1, -1 , -1):
            if brownie[first]< brownie[second]: 
                ind = second
            else:
                break
        brownie.insert(ind, brownie.pop(first))
    return brownie

print (insertionsort())
