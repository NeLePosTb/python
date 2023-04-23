
n = int(input("Введите количество элементов массива: "))
arr = []
for i in range(n):
    arr.append(int(input("Введите элемент массива: ")))
x = int(input("Введите число X: "))
count = 0
for i in arr:
    if i == x:
        count += 1
print("Число X встречается в массиве", count, "раз")