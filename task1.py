with open('text_1.txt', 'w+', encoding='utf-8') as text:
    line = True
    while line:
        line = input('Введите текст. Для завершения ввода нажмите Enter.')
        text.writelines([line, '\n'])
        text.seek(0)
        print(text.read())
    print('Работа программы завершена.')

