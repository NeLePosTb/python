
def find_numbers(sum, product):
    for i in range(1, sum):
        if product % i == 0:
            j = product // i
            if i + j == sum:
                return i, j
    return None

result = find_numbers(int(input("введите сумму чисел: ")), int(input("введите произведение чисел: ")))
if result:
    print("Найдены числа:", result[0], "и", result[1])
else:
    print("Числа не найдены")