
row = int(input("enter the number of row: "))
colum=int(input("enter the number of colum: "))
symobol=input("enter the symbol to print: ")
for i in range(row):
    for j in range(colum):
        print(symobol,end="3")
    print()

print("solving pattern in python:")
print("incressing pattern")
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()

print("dcresing pattern")
n=5
for i in range(n):
    for j in range(i,n):
        print('*',end="")
    print()

print("Right side triangle")
n= 5
for i in range(n):
    for j in range(i,n):
        print(' ',end="")
    for j in range(i+1):
        print('*',end="")
    print()
print("left side triangle")
n= 5
for i in range(n):
    for j in range(i+1):
        print(' ',end="")
    for j in range(i,n):
        print('*',end="")
    print()

print("hill pattern")
n=int(input("enter your number: "))
symbol=input("enter your symbol: ")
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(symbol,end="")
    for j in range(i+1):
        print(symbol,end="")
    print()

n=int(input("enter your number: "))
symbol=input("enter your symbol: ")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(symbol,end="")
    for j in range(i,n):
        print(symbol,end="")
    print()


print("diamond pattern")
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end="")
    for j in range(i):
        print('*',end="")
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print('*',end="")
    for j in range(i,n):
        print('*',end="")
    print()