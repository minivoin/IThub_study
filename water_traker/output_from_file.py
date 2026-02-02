
def output():
    file = open("diary.txt")
    final_output = file.read()
    file.close()
    return final_output

def cahge_file(input_string, data_of_record):
    file = open("diary.txt", "r")
    strings = file.read().split('\n')
    file.close()
    check = True
    for i in strings:
        data = i.split(' ')
        if data[0] == str(data_of_record):
            check = False
            break
    if check:
        file = open("diary.txt", "a")
        file.write(f'{data_of_record} {input_string}\n')
        file.close()
    else:
        file = open("diary.txt", "r")
        new_data = file.read().replace(f'{data[0]} {data[1]}', f'{data[0]} {input_string}')
        file.close()
        file = open("diary.txt", "w")
        file.write(new_data)
        file.close()
        
def search_today(data_of_record):
    file = open("diary.txt", "r")
    strings = file.read().split('\n')
    file.close()
    check = True
    for i in strings:
        data = i.split(' ')
        if data[0] == str(data_of_record):
            check = False
            return data[1]
    if check:
        cahge_file('0', data_of_record)
        return '0'

if __name__ == '__main__':
   print(search_today('2026-02-02'))