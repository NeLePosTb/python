n = int(input("Введите количество элементов массива: "))
arr = []
for i in range(n):
    arr.append(int(input("Введите элемент массива: ")))

x = int(input("Введите число X: "))

closest_num = arr[0]
for num in arr:
    if abs(num - x) < abs(closest_num - x):
        closest_num = num

print("Самый близкий по величине элемент в массиве к числу", x, "равен", closest_num)