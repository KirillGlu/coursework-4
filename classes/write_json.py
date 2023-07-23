from classes.vacancy import Vacancy
import json
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def get_vacancies_from_file(self):
        pass


class JSONSaver(Saver):

    def __init__(self):
        self.vacancies_from_file = []

    def write_file(self, vacancies: list):
        """Записывает вакансии в файл"""
        with open('../vacancies.json', 'w', encoding="utf-8") as f:
            json.dump(vacancies, f, indent=2, ensure_ascii=False)

    def get_vacancies_from_file(self):
        """Достает вакансии из файла и создает экземпляры класса Vacancy"""
        with open('../vacancies.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
            for vacancy in data:
                self.vacancies_from_file.append(Vacancy(**vacancy))
            return self.vacancies_from_file

