num = int(input())
factorial = 1

if num%1==0 and num>=0:
    for i in range(1, num+1):
        factorial = i*factorial
    print(factorial)

else:
    print("Факториал можно вычислить только для положительного числа")

