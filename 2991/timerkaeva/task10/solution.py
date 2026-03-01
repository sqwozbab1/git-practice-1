import re

def normalize_ipv6(ip):
    parts = ip.split(':')
    normalized = []
    
    for part in parts:
        if part:
            try:
                if part != '':
                    part = part.lstrip('0')
                    if not part:  # Если после удаления осталась пустая строка
                        part = '0'
            except:
                pass
        normalized.append(part)
    
    return ':'.join(normalized)


def check_ip(ip):
    ip = ip.strip()  # Убираем пробелы в начале и конце
    
    # Проверка на IPv4
    if check_ipv4(ip):
        return "IPv4"
    
    # Проверка на IPv6
    if check_ipv6(ip):
        return "IPv6"
    
    return "INVALID"


def check_ipv4(ip):

    parts = ip.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        if len(part) > 1 and part[0] == '0':
            return False
        
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True


def check_ipv6(ip):
    
    if ip.count('::') > 1:
        return False
    
    if '::' in ip:
        parts = ip.split(':')
        parts = [p for p in parts if p != '']
    else:
        parts = ip.split(':')
        if len(parts) != 8:
            return False
    
    for part in parts:
        if part == '':  # Пустая часть допустима только при ::
            continue
            
        if not re.match(r'^[0-9a-fA-F]{1,4}$', part):
            return False
    
    return True


def main():
   
    test_addresses = [
        # Корректные IPv4
        "192.168.1.1",
        "0.0.0.0",
        "255.255.255.255",
        
        # Некорректные IPv4
        "256.1.2.3",
        "192.168.1",
        "192.168.1.1.1",
        "192.168.01.1",
        "abc.def.ghi.jkl",
        
        # Корректные IPv6
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
        "2001:db8:85a3::8a2e:370:7334",
        "::1",
        "fe80::1",
        
        # Некорректные IPv6
        "2001::85a3::8a2e",  # Два ::
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334:extra",  # Слишком много частей
        "2001:0db8:85a3:0000:0000:8a2e:0370:zzzz",  # Не hex символ
        "2001:0db8:85a3:0000:0000:8a2e:0370:",  # Заканчивается на :
    ]
    
    print("Тестирование проверки IP-адресов:")
    print("-" * 60)
    
    for addr in test_addresses:
        result = check_ip(addr)
        
        if result == "IPv6":
            normalized = normalize_ipv6(addr)
            print(f"Адрес: '{addr}'")
            print(f"Тип: {result}")
            print(f"Нормализованный: {normalized}")
        else:
            print(f"Адрес: '{addr}'")
            print(f"Тип: {result}")
        print()


if __name__ == "__main__":
    user_input = input("Введите IP-адрес для проверки: ")
    result = check_ip(user_input)
    
    if result == "IPv6":
        normalized = normalize_ipv6(user_input)
        print(f"Тип: {result}")
        print(f"Нормализованный: {normalized}")
    else:
        print(f"Тип: {result}")
    
    main()