a = input("Please enter a positive integer number:")
b = 0
if a.isnumeric():
    for i in a :
        b += int(i) ** len(a)
    print(b)
    if b == int(a) :
        print(f"{a} is an Armstrong number") 
    else:
        print(f"{a} is not an Armstrong number")

else:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

