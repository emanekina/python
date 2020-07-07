def int_func(text):
    for letter in text:
            if ord(letter) < ord('a') or ord(letter) > ord('z'):
                return print('Ошибка ввода')
    return text.title()

words = input('Маленькими латинскими буквами введите строку, состоящую из слов, разделенных пробелом: ').split()
for num_let, word in enumerate(words):
    words[num_let] = int_func(word)
if words.count(None) ==0:
    print(' '.join(words))
else:
    print(f'Что-то пошло не так. Вы точно ввели только латинские буквы в нижнем регистре?\nПерезапустите программу и повторите ввод.')
