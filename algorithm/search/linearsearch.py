def binarysearch():
    cookie = list(map(int, input("Enter a list:").split()))
    crumb = int(input("Enter a number to search:"))
    for sweet in cookie :
        if sweet - crumb ==0 : return "Number found"
    return "Number not found"

print (binarysearch())
