import csv  # добавляем библиотеку csv для работы с этими файлами
new_space = []  # создаём пустой список, куда в дальнейшем будем присваивать значение строки csv файла
with open("space.csv", encoding="utf-8") as file:  # открываем файл с помощью конструкции with open,
    # прописываем encoding="utf-8" для правильной работы с кириллицей
    reader = csv.DictReader(file, delimiter="*", quotechar="'")  # считываем файл в reader, разделитель - *, кавычки - '
    for row in reader:  # построчно пробегаем файл
        n = int(row["ShipName"][5])  # присваиваем n по условию
        m = int(row["ShipName"][6])  # присваиваем m по условию
        t = len(row["planet"]) - row["planet"].count(" ")  # присваиваем t по условию
        g = row["direction"].split()  # список координат направления
        xd = int(g[0])  # направление по иксу
        yd = int(g[1])  # направление по игрику
        if "0" in row["coord_place"]:
            _ = row["coord_place"].split()
            if _[0] == "0":
                if n > 5:
                    _[0] = str(n + xd)
                elif n <= 5:
                    _[0] = str(-(n + xd) * 4 + t)
            if _[1] == "0":
                if m > 3:
                    _[1] = str(m + t + yd)
                elif m <= 3:
                    _[1] = str(-(n + yd) * m)
            row["coord_place"] = " ".join(_)  # присваиваем получившиеся координаты
            if row["ShipName"][3] == "V":  # ищем нужные корабли, оканчивающиеся на V
                print(f"{row['ShipName']} - ({row['coord_place'].split()[0]}, {row['coord_place'].split()[1]})")  # выводим
                # их координаты
        new_space.append(row)

with open("space_new.csv", "w", newline="", encoding="utf-8") as file:  #создаём csv файл для последующего преобразования в txt
    w = csv.DictWriter(file, fieldnames=["ShipName", "planet", "coord_place", "direction"])
    w.writeheader()  # прописываем заголовки
    w.writerows(new_space)  # прописываем значения

with open("space_new.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="*", quotechar="'")
    with open("space_new.txt", "w") as f:  #создаём текстовый файл space_new.txt
        f.writelines(file)



    # with open("space_new.txt", "w", newline="", encoding="utf-8") as f:  #создаём csv файл для последующего преобразования в txt
    #     f.writelines(file.readlines())