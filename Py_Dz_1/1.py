day = int(input(" Введите номер дня недели от 1 до 7:  "))
if day <= 5:
    print("Это рабочий день ")
elif day <= 7:
    print(" Это выходной день ")
else:
    print(" Нет такого номера дня недели")
