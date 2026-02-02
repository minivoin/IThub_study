from calculating_norm import calculate
import inputs
import os
from datetime import date
from output_from_file import output
from output_from_file import cahge_file
from output_from_file import search_today

dali_norm = calculate(inputs.weight())


def main_menu():
    os.system('cls')
    print('Введите команду:\n1.Ввести воду\n2.Сколько осталось до дневной нормы\n3.История\n4.Ввести вес\n5.Выход')
    user_input = input()
    if user_input == '1':
        add_water(inputs.water())
    elif user_input == '2':
        show_dali_norm()
    elif user_input == '3':
        os.system('cls')
        print(output())
        input('Чтобы вернуться в гланое меню нажмите Enter...')
        main_menu()
    elif user_input == '4':
        global dali_norm
        dali_norm = calculate(inputs.weight())
    elif user_input == '5':
        print('Выход')
    else:
        input('Команда не распознана\nЧтобы продолжить нажмите Enter...')
        main_menu()
    

def add_water(amount_ml):
    now_water = int(search_today(date.today()))
    now_water += int(amount_ml)
    cahge_file(now_water, date.today())
    main_menu()

def show_dali_norm():
    os.system('cls')
    now_water = search_today(date.today())
    remainder = int(dali_norm) - int(now_water)
    if remainder < 0:
        remainder = remainder * -1
    print(f'Дневная норма - {dali_norm}\nВы выпили - {now_water}\nВам осталось выпить - {remainder}')
    input('Чтобы вернуться в гланое меню нажмите Enter...')
    main_menu()


main_menu()

