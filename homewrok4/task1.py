def intersection(first_set, second_set):
    return sorted(list(set(first_set) & set(second_set)))


n = int(input("Количество элементов в первом наборе: "))
first_set = [int(input()) for i in range(n)]
m = int(input("Количество элементов во втором наборе: "))
second_set = [int(input()) for i in range(m)]

result_set = intersection(first_set, second_set)
print( result_set)