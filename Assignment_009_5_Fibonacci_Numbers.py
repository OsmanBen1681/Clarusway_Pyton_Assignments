num1 = 1
num2 = 1
sum1 = 0
Fibonaccci_list = [1,1]
while sum1 != 55:
    sum1 = num1 + num2
    num1 = num2
    num2 = sum1
    Fibonaccci_list.append(sum1)
print(Fibonaccci_list)
    
    
