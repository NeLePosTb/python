n = int(input("Введите количество монеток: "))
coins = input("Введите порядок монеток (Г - герб, Р - решка): ")

heads = coins.count("Р")
tails = coins.count("Г")

if heads == n or tails == n:
    print(0)
elif heads > tails:
    print(tails)
else:
    print(heads)