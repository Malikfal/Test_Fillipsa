from help_data import *
from csv_data import *
import os

class Test_Fil:
    def __init__(self, name, Class) -> None:
        self.student_results = []

        self.end_res_description = ["0) Общее число несовпадений",
        "1) Общая тревожность в школе",
        "2) Переживания социального стресса",
        "3) Фрустрация потребности в достижении успеха",
        "4) Страх самовыражения",
        "5) Страх ситуации проверки знаний",
        "6) Cтрах не соответствовать ожиданиям окружающих",
        "7) Низкая физиологическая сопротивляемость стрессу",
        "8) Проблемы и страхи в отношениях с учителями"]

        self.end_res = {"name": name,
        "Class": Class,
        "total_mismatches": 0,
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        "result": 0}

        # Прохождение тестирования
        self.testirovanie()
        self.koef_func()
        self.print_results()

        # Сохранение результатов в таблицу
        csv_write(self.end_res)

        print(f"\n{name.upper()}, спасибо за прохождение тестирования.\n")
        

    # Начало тестирования
    def testirovanie(self):
        print("Вводите только '+' - если считаете правдой, и '-' - если ложью.\n")
        answer = ""
        for q in questions:
            while True:
                answer = input(f"{q}\n")
                if answer in ["-", "+"]:
                    self.student_results.append(answer)
                    break
                print('\033[1m' + "Вводите только + или -" + '\033[0m')


    # Вычисление всех коэффициентов тревожности 
    def koef_func(self):
        count_trev = 0
        for ind in range(len(self.student_results)):
            if self.student_results[ind] != right_results[ind]:
                count_trev+=1

        def other_koefs(listik: list) -> int:
            count_trev = 0
            for ind in listik:
                if self.student_results[ind-1] != right_results[ind-1]:
                    count_trev+=1
            #return f"{format((count_trev / len(listik)) * 100, '.1f')}%"
            return count_trev

        #self.end_res["total_mismatches"] = f"{format((count_trev / len(right_results)) * 100, '.1f')}%"
        self.end_res["total_mismatches"] = count_trev
        self.end_res[1] = other_koefs(l1)
        self.end_res[2] = other_koefs(l2)
        self.end_res[3] = other_koefs(l3)
        self.end_res[4] = other_koefs(l4)
        self.end_res[5] = other_koefs(l5)
        self.end_res[6] = other_koefs(l6)
        self.end_res[7] = other_koefs(l7)
        self.end_res[8] = other_koefs(l8)  


    # Вывод результатов
    def print_results(self):
        print()


        print('\033[1m' + 'Результаты тестирования:' + '\033[0m',"\n")

        tot_mis = self.end_res["total_mismatches"] / len(right_results) * 100
        if tot_mis < 50:
            print("   Низкий уровень тревожности")
            self.end_res["result"] = "Низкий уровень тревожности"

        elif 75 > tot_mis >= 50:
            print("   Повышенный уровень тревожности")
            self.end_res["result"] = "Повышенный уровень тревожности"

        elif tot_mis >= 75:
            print("   Высокий уровень тревожности")
            self.end_res["result"] = "Высокий уровень тревожности"
            

        for ind in range(len(self.end_res_description)-1):
            print(f'   {self.end_res_description[ind+1]}: {self.end_res[ind+1]}')




if __name__ == "__main__":
    platform = os.name
    if platform == "posix":
        os.system("clear")
    elif platform == "nt":
        os.system("cls")
    a  = """ _____             _      _____  _  _  _  _                    
|_   _|  ___  ___ | |_   |  ___|(_)| || |(_) _ __   ___   __ _ 
  | |   / _ \/ __|| __|  | |_   | || || || || '_ \ / __| / _` |
  | |  |  __/\__ \| |_   |  _|  | || || || || |_) |\__ \| (_| |
  |_|   \___||___/ \__|  |_|    |_||_||_||_|| .__/ |___/ \__,_|
                                            |_|                """
    print(a)
    print('\033[1m' + "Тревожность ребёнка в школе" + '\033[0m')
    print("\nСейчас тебе будет предложен опросник, который состоит из вопросов о том,как ты себя чувствуешь в школе.\nСтарайся отвечать искренне и правдиво, здесь нет верных или неверных, хороших или плохих ответов.\nНад вопросами долго не задумывайся.\n")
    csv_create(platform)
    #Проведение теста нужное кол-во раз
    while True:
        try:
            input("Нажмите Enter для начала тестирования | ctrl+c для выхода из программы\n")
            name = input("Введите своё ФИО: ").title()
            Class = input("Введите номер и букву своего класса: ").upper().replace(" ","")
            test = Test_Fil(name, Class)
        except KeyboardInterrupt:
            print("\nРабота программы завершена!")
            break
