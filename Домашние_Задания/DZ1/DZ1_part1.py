# Вводим слово с клавиатуры
word = input()

#Если четное число выводим 2 средние буквы, если несетное 1
if len(word)%2==0:
    simvol = len(word)//2
    print(f"{word[simvol-1]}{word[simvol]}")
else:
    simvol = len(word)//2
    print(f"{word[simvol]}")