checking_number = input("Please write a number for checking is it prime or not:")
counter = 0
for i in range(2,int(checking_number)):
    if int(checking_number) % i == 0:
        counter += 1
if counter != 0:
    print(f"{checking_number} is not a prime number.")
else:
    print(f"{checking_number} is a prime number.")


