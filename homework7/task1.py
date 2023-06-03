
vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и'] # список гласных букв
phrases = input("Введите фразы через пробел: ").split() # ввод фраз и разделение их по пробелам
vowels_count = [] # список количества гласных в каждой фразе

for phrase in phrases:
    phrase_vowels = 0 # количество гласных в текущей фразе
    for letter in phrase:
        if letter.lower() in vowels:
            phrase_vowels += 1
    vowels_count.append(phrase_vowels) # добавление количества гласных в список

if len(set(vowels_count)) == 1: # если количество гласных в каждой фразе одинаковое
    print("парам пам-пам")
else:
    print("пам парам")