def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Введите номер числа Фиббоначи: "))
print("Число Фибоначчи под номером ", n, " равно ", fibonacci(n))