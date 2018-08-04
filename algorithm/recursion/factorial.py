def factorial(i):
    if i==0: return 1
    return i * factorial(i-1)
fact = int(input("Enter an integer to find factorial:"))
print (factorial(fact))
