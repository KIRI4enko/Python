''' Замена в файле
    Replacement in file
На вход программе подается текстовый файл следующего вида:
Символы алфавита …{N}… Символы алфавита
Где N – целое число (таких конструкций может быть несколько)
Необходимо открыть файл, прочитать его содержимое и запросить у пользователя ввести N строк,
на которые необходимо будет заменить соответствующую цифру в новом созданном файле
Например:
Гипотенуза равна корню из {0} квадратов {2}
Гипотенуза равна корню из суммы квадратов катетов'''

with open('input.txt', mode='r', encoding='utf-8') as file_input:
    i = file_input.read()
    print(i)
    numbers = []
    for x in range(len(i)):
        if i[x] == '{':
            y = x + 1
            num = ''
            while i[y] != '}':
                num += i[y]
                y += 1
            numbers.append(int(num)) # Нашли номера
    print(numbers)
    with open('output.txt', mode='w', encoding='utf-8') as file_output:
        for x in numbers:
            N = input('Замените {'f'{x}''}: ')
            i = i.replace('{'f'{x}''}', N, 1)
        print(i + ' (Записано в файл output.txt)')
        file_output.write(i)

