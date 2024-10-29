def caesar_cipher(text, shift, alphabet, mode):
    shift %= len(alphabet[0])
    result = []

    for char in text:
        if char in alphabet[0]:
            i = alphabet[0].index(char)
            if mode == "encryption":
                new = (i + shift) % len(alphabet[0])
            elif mode == "decryption":
                new = (i - shift) % len(alphabet[0])
            result.append(alphabet[0][new])
        elif char in alphabet[1]:
            i = alphabet[1].index(char)
            if mode == "encryption":
                new = (i + shift) % len(alphabet[1])
            elif mode == "decryption":
                new = (i - shift) % len(alphabet[1])
            result.append(alphabet[1][new])
        else: result.append(char)

    return ''.join(result)

if __name__ == '__main__':

    language = input('Enter language (english/russian) ')
    mode = input('Enter mode (encryption/decryption): ')
    shift = int(input('Enter shift : '))
    text = input('Enter text : ')

    russian_capital = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    russian_small = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    english_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    english_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if language == "russian":
        alphabet = [russian_capital, russian_small]
    elif language == "english":
        alphabet = [english_capital, english_small]
    else:
        print("Language is incorrect")

    result = caesar_cipher(text, shift, alphabet, mode)
    print("Result:", result)
