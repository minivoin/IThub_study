def search_vowels():
    string = input("Введите строку")
    vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "a", "e", "i", "o", "u", "y"]
    i = 0
    vowel_ring = 0
    for i in range(len(string)):
        j = 0
        for j in vowels:
            if string[i] == j:
                vowel_ring += 1
    return f'количевство гласных = {vowel_ring}'

print(search_vowels())
