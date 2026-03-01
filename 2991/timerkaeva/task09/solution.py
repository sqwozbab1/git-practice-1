def encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)


def decode(encoded_text):
    if not encoded_text:
        return ""
    
    result = []
    i = 0
    
    while i < len(encoded_text):
        char = encoded_text[i]
        i += 1
        
        number = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            number += encoded_text[i]
            i += 1
        
        count = int(number) if number else 1
        
        result.append(char * count)
    
    return "".join(result)


def main():
    test_strings = [
        "AAABBBCCDAA",
        "Hello World!!!",
        "ABBBCCCCCCCDD",
        "A",
        "",
        "111222333",
        "  ",
    ]
    
    print("Тестирование RLE сжатия:")
    print("-" * 50)
    
    for original in test_strings:
        encoded = encode(original)
        decoded = decode(encoded)
        
        print(f"Оригинал: '{original}'")
        print(f"Сжато:    '{encoded}'")
        print(f"Распаковано: '{decoded}'")
        print(f"Корректно: {original == decoded}")
        print()


if __name__ == "__main__":
    print("Выберите действие:")
    print("1 - Сжать строку")
    print("2 - Распаковать строку")
    
    choice = input("Ваш выбор (1/2): ")
    
    if choice == "1":
        text = input("Введите строку для сжатия: ")
        result = encode(text)
        print(f"Результат сжатия: {result}")
    
    elif choice == "2":
        text = input("Введите сжатую строку (например, A3B2C1): ")
        result = decode(text)
        print(f"Распакованная строка: {result}")
    
    else:
        print("Неверный выбор")
    
    main()