import csv  # добавляем библиотеку csv для работы с этими файлами
new_space = []  # создаём пустой список, куда в дальнейшем будем присваивать значение строки csv файла
with open("space.csv", encoding="utf-8") as file:  # открываем файл с помощью конструкции with open,
    # прописываем encoding="utf-8" для правильной работы с кириллицей
    reader = csv.DictReader(file, delimiter="*", quotechar="'")  # считываем файл в reader, разделитель - *, кавычки - '
    for row in reader:
        new_space.append(row)  # переписываем все строки файла в переменную
    while True:
        a = input()# так как без вопроса, то оставляем пустые скобки
        t = False
        if a == "stop":
            break
        else:
            for row in new_space: # построчно пробегаем переменную
                if a == row["ShipName"]:
                    print(f"Корабль {row['ShipName']} был отправлен с планеты: {row['planet']} и его направление движения было: {row['direction']}")
                    t = True
            if t == False:
                    print("error.. er.. ror..")
