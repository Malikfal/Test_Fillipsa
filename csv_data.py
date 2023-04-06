import csv
import os

# Создание csv таблицы, если такой нет
def csv_create() -> None:
    if os.path.exists("data.csv"):
        return None

    with open("data.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file,delimiter='|', quoting=csv.QUOTE_MINIMAL)
        text = ["ФИО ученика", "Класс", "Общее число несовпадений", "Несовпадений по 1 фактору", "Несовпадений по 2 фактору", "Несовпадений по 3 фактору", "Несовпадений по 4 фактору", "Несовпадений по 5 фактору", "Несовпадений по 6 фактору", "Несовпадений по 7 фактору", "Несовпадений по 8 фактору", "Результат"]
        writer.writerow(text)

# Добавление данных в csv таблицу
def csv_write(results: dict) -> None:
    with open("data.csv", "a", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file,delimiter='|', quoting=csv.QUOTE_MINIMAL)
        text = [res for _, res in results.items()]
        writer.writerow(text)
        
            