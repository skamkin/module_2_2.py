first = int(input('Введите число:  '))
second = int(input('Введите число:  '))
third = int(input('Введите число:  '))

if first == second and first == third and second == third:  # 3
    print(3)
elif first == second or first == third or second == third:  # 2
    print(2)
else:
    print(0)
