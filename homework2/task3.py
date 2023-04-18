Up = 1
def two_numbers(end):
    for i in range(1,end):
        if 2**Up == i :
            Up += 1
            print(i)
            return i

two_numbers(input("Введите число: "))