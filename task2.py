# использую файл, созданный в первом задании
def count_of_words(line):  # функция для подсчета количества слов в строке
    words = 0
    for word in line.split():
        words += 1
    return words


try:
    with open('text_1.txt', 'r', encoding='utf-8') as text:
        print(text.read())
        text.seek(0)  # возвращаемся в начало файла после его чтения
        count_lines = 0
        count_words = []
        empty_line = 0
        for line in text.readlines():
            if line != '\n':
                count_lines += 1
                count_words.append(count_of_words(line))
            else: # т.к. программа не считает пустые строки, то предупредим об этом пользователя
                empty_line += 1
        if empty_line > 0:
            print('Пустые строки в файле не учитываются.')
        print(f'Количество строк в файле - {count_lines}')
        for i in range(len(count_words)):
            print(f'Количество слов в строке {i + 1} - {count_words[i]}')
except FileNotFoundError:
    print('Файл не найден.')
