
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def triangle_number(n):
    if n == 1:
        return 1
    else:
        return n + triangle_number(n-1)

n = int(input("Введите число: "))
print("Факториал числа", n, "равен", factorial(n))
print("Треугольное число для числа", n, "равно", triangle_number(n))