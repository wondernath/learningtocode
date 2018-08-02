def insertionsort():
    brownie = list(map(int, input().split()))
    for first in range(len(brownie)):
        least_ind  = first
        for second in range(first-1, -1 , -1):
            if brownie[first] < brownie[second]:
                least_ind = second
            else :
                break
        brownie.insert(least_ind, brownie.pop(first))
    return brownie

print (insertionsort())
            
