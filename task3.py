password = input("Введите пароль через пробел: ").split()
code = int(input("Введите значение для сдвига элементов: "))
chast1 = password[:code]
chast2 = password[code:]
final = chast2 + chast1
super_final = [int(i) for i in final]
print(super_final)