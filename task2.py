def info_func(surname, name, year, city, email, tel_num):
    return print(f'Данные клиента {surname} {name}: '\
                 f'год рождения - {year}; '\
                 f'город проживания - {city}; '\
                 f'email - {email}; '\
                 f'телефон - {tel_num}.')


#--------------решила поэкспериментировать с запросом ввода параметров---------------
client_info = {'имя': None,
               'фамилию': None,
               'год рождения': None,
               'город проживания': None,
               'адрес электронной почты': None,
               'телефон': None}
for el in client_info.keys():
    client_info[el] = input(f'Введите {el} клиента:')
info_func(name=client_info.get('имя'),
          surname=client_info.get('фамилию'),
          year=client_info.get('год рождения'),
          city=client_info.get('город проживания'),
          email=client_info.get('адрес электронной почты'),
          tel_num=client_info.get('телефон'))

"""Без запроса ввода параметров:

    info_func(name='Елена',
          surname='Манекина',
          year='1985',
          city='Москва',
          email='emanekina@mail.ru',
          tel_num='89000000000')

 """
