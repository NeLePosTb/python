def sum(a,b):
    if b == 0:
        return a
    else:
        return sum(a ^ b, (a & b) << 1)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Сумма чисел ", a, " и ", b, " равно = ", sum(a,b))