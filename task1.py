import math

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

p=1/2*(a+b+c)

s=math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Результат: ", s)

