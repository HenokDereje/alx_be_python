size = int(input("Enter the size of the pattern: "))
if size>0:
    row = 0
    while row<size:
        for i in range(size):
            print("*", end="")
        print()
        row+=1
else:
    print("Enter a positive number.")