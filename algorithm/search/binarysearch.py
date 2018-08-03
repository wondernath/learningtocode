import math

def binarysearch():
    router = list(map(int, input("Enter a list of int:").split()))
    router.sort()
    print (router)
    packet = int(input("Enter a number to search:"))
    found = True
    while found:
        mid = math.floor(len(router)/2)
        if router[mid]==packet :
            return "Number found"
        elif router[mid] > packet :
            router = router[:mid]
        #elif router[mid] < packet :
        else :
            router = router[mid:]
        # else:
        #    found = False
        if len(router)==0 : found = False
    return "Number not found"

print (binarysearch())
