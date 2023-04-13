num = int(input("Введите трехзначное число: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
sum = a + b + c
print("Сумма цифр числа", num, "равна", sum)
