import random
try:
    a=int(input("Enter left limit: "))
    b=int(input("Enter right limit: "))
    n=random.randint(a,b)
    print("Range is (",a,",",b,") and randomly picked number is ",n)
    if(n%2==0):
        print(n," is an even number\n")
    else:
        print(n," is an odd number\n")
    if(n>=0):
        print(n," is a positive number\n")
    else:
        print(n," is a negative number\n")
    c=0
    for i in range(2,n):
        if(n%i==0):
            print(n," is a composite number\n")
            c=1
            break
    if(c==0):
        print(n," is a prime number\n")
except:
    print("Please enter an integer!")