def check_brackets(text):
       brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    open_brackets = set(brackets.keys())
    close_brackets = set(brackets.values())
    
    stack = []
    
    for char in text:
        if char in open_brackets:
            stack.append(char)
        
        elif char in close_brackets:
            if not stack:
                return "NO"
            
            last_open = stack.pop()
            
            if brackets[last_open] != char:
                return "NO"
        
    
    return "YES" if not stack else "NO"


def main():
    test_strings = [
        "(a + b) * [c + d] / {e + f}",  # Правильно
        "([{}])",                         # Правильно
        "((()))",                          # Правильно
        "([)]",                             # Неправильно
        "((())",                             # Неправильно (не закрыта)
        "())(",                               # Неправильно
        "hello world",                        # Нет скобок - правильно
        "({[}])",                              # Неправильно
    ]
    
    print("Тестирование проверки скобок:")
    print("-" * 40)
    
    for test in test_strings:
        result = check_brackets(test)
        print(f"Строка: '{test}'")
        print(f"Результат: {result}")
        print()


if __name__ == "__main__":
    user_input = input("Введите строку для проверки скобок: ")
    result = check_brackets(user_input)
    print(f"Результат: {result}")
    
    main()