

class Vacancy:

    def __init__(self, name_vacancy: str, city: str, salary: int, requirement: str, url: str, sait: str):
        self.name_vacancy = name_vacancy
        self.__city = city
        self.salary = salary
        self.requirement = requirement
        self.url = url
        self.sait = sait

    @property
    def city(self):
        return self.__city

    def __str__(self):
        return f"""
Название вакансии: {self.name_vacancy}
Город: {self.__city}
ЗП: {self.salary}
Требования: {self.requirement}
Ссылка: {self.url}
Сайт: {self.sait}
=========================================
"""

    def __gt__(self, other):
        return self.salary > other.salary

