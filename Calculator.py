while True:
    print('💎 Калькулятор от Fru1sik 💎')
    print('Поддержка +, -, :, ×, %')
    a = float(input('Первая цифра: '))
    op = input('Знак решения: ')
    b = float(input('Вторая цифра: '))
    
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '×' or op == '*':
        print(a * b)
    elif op == ':' or op == '/':
        if b == 0:
            print("🚫ОШИБКА🚫 Деление на ноль считается ошибкой!")
        else:    
            print(a / b)
    elif op == '%':
        print((a/100)*b)
    quit = input('Выход?: ')
    
    if quit.lower() == 'да':
        print('Закрываем,Секунду...')
        break
    else:
        print('Хорошо, продолжай писать вопросы')
        
