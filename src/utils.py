def filter_vacancies(vacancies: list, city: str):
    """Получает список вакансий по ключевому слову"""
    filtered_vacancies = []
    for vacancy in vacancies:
        if city.lower() in vacancy["city"].lower():
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def get_top_vacancies(vacancies, top_n):
    """Возвращает топ N вакансий"""
    return vacancies[0:top_n]
