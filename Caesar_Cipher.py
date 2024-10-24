def caesar_cipher(text, shift, language, mode):
    shift %= len(language)

    for i in text:
        if mode == "encryption":
            new = (i + shift) % len(language)
        elif mode == "encryption":
            new = (i - shift) % len(language)
        result.append(language[new])

    return ''.join(result)

def main():
    alphabet = input('Enter language (1: english (capital/small), 2: russian (capital/small) ')
    mode = input('Enter mode (encryption/C): ')
    shift = int(input('Enter shift : '))
    text = input('Enter text : ')

    russian_capital = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    russian_small = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    english_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    english_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if alphabet == "russian capital":
        language = russian_capital
    elif alphabet == "russian small":
        language = russian_small
    elif alphabet == "english capital":
        language = english_capital
    elif alphabet == "english small":
        language = english_small
    else:
        print("Language is incorrect")

    result = caesar_cipher(text, shift, language, mode)
    print("Result:", result)