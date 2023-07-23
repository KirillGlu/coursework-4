from classes.get_api import HeadHunterAPI, SuperJobAPI
from classes.write_json import JSONSaver
from src.utils import filter_vacancies, get_top_vacancies

get_api = ""
# Ввод ключевого слова для поиска вакансий
user_input = input("Введите ключевое слово для поиска вакансий")

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_api(user_input)
sj_vacancies = sj_api.get_api(user_input)

# Получение вакансий в требуемом формате
formatted_hh = hh_api.get_formatted_vacancies()
formatted_sj = sj_api.get_formatted_vacancies()

# Ввод выбора сайта для поиска вакансий
choice_api = input("Выберите вакансии с сайта\n1 - Вакансии с HeadHunter\n2 - Вакансии с SuperJob\n3 - Вакансии с "
                   "HeadHunter и SuperJob\n")

if choice_api == "1":
    get_api = formatted_hh
elif choice_api == "2":
    get_api = formatted_sj
elif choice_api == "3":
    get_api = formatted_hh + formatted_sj
else:
    print("Не верный ввод")

# Ввод пользователя города, в котором интересует вакансия
user_keyword = input("Введите интересующий город(Пропустить - Enter)")
if len(user_keyword) > 1:
    filtered_vac = filter_vacancies(get_api, user_keyword)
else:
    filtered_vac = get_api

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
save_in_file = json_saver.write_file(filtered_vac)

# Бесконечный цикл для работы с пользователем
while True:

    command = input("Выберите критерии вакансий\n1 - Показать все вакансии\n2 - Показать вакансии сортированные по "
                    "ЗП\nexit - Завершение программы\n")

    if command.lower() == "exit":
        break
    elif command == "1":
        vacancies = json_saver.get_vacancies_from_file()
    elif command == "2":
        top_n = int(input("Выберете количество интересующих вакансий"))
        vacancies = get_top_vacancies(sorted(json_saver.get_vacancies_from_file(), reverse=True), top_n)
    else:
        print("Не верный ввод")
        break

    for vacancy in vacancies:
        print(vacancy)
