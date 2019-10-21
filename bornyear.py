# Спросить у пользователя год рождения А.С Пушкина

b_year_asp = input("Введите год рождения А.С.Пушкина - ")

if b_year_asp == "1799": # 1799 - в кавычках т.к. Input - вводит строки tupe - str
    print('Верно')
    print(b_year_asp,"====", type(b_year_asp))
else:
    print('Неверно')
    print(b_year_asp,"====",type(b_year_asp))

