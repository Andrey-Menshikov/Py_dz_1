x = int(input("Введите х: "))
y = int(input("Введите у: "))
if x != 0 and y != 0:
    if x > 0:
        if y > 0:
            print("1 четверть")
        else:
            print("4 четверть")
    elif x < 0:
        if y < 0:
            print("2 четверть")
        else:
            print("3 четверть")
else:
    print("Ввели не верные данные ")
