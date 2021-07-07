import time
def myFunction(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return myFunction(n-1) + myFunction(n-2)
        
n=int(input("Enter the nth position: "))
print(myFunction(n))
time.sleep(10)
