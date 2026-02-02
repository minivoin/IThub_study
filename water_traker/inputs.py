def weight():
    user_input = int(input("Введите свой вес\n"))
    if user_input <= 0:
        print("Вы не можете весить меньше или равно 0")
        weight()
    else:
        return user_input
    
def water():
    user_input = int(input("Введите объём выпитой воды\n"))
    if user_input <= 0:
        print("Вы не можете весить меньше или равно 0")
        water()
    else:
        return user_input

if __name__ == '__main__':
    print(water())