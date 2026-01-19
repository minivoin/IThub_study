stroka = input('введите строку')

znaki = [",", "." , " ", ":", ";"]
stroka = stroka.lower()
i = 0
while i <  len(znaki):
    stroka = stroka.replace(znaki[i], "")
    i += 1
i = 0
#A man, A plan, a canal: Panama
chek = True
while i < int(len(stroka))//2:
    if stroka[i] == stroka[(len(stroka) - 1) - i]:
        pass
    else:
        chek = False
        break
    i += 1

if chek:
    print("PALINDROME")
else:
    print("NE PALINDROME")

