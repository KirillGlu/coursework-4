import requests
import os
from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def get_api(self):
        pass

    @abstractmethod
    def get_formatted_vacancies(self):
        pass


class HeadHunterAPI(API):

    def __init__(self):
        self.vacancies_lst = []

    def get_api(self, keyword: str):
        """Получает список вакансий"""
        for page in range(10):
            param = {
                'text': keyword,
                'page': page,
                'per_page': 100
            }
            data = requests.get("https://api.hh.ru/vacancies", params=param).json()
            for i in data["items"]:
                self.vacancies_lst.append(i)

        return self.vacancies_lst

    def get_formatted_vacancies(self):
        """Форматирует список вакансий"""
        formatted_vacancies = []
        for i in range(len(self.vacancies_lst)):
            # print(i)
            if self.vacancies_lst[i]['salary'] is None:
                continue
            if self.vacancies_lst[i]['salary']['from'] is None:
                continue
            else:
                name_vacancy = self.vacancies_lst[i]['name']
                city = self.vacancies_lst[i]['area']['name']
                url = self.vacancies_lst[i]['alternate_url']
                requirement = self.vacancies_lst[i]['snippet']['requirement']
                salary_from = self.vacancies_lst[i]['salary']['from']

            format_data = {"name_vacancy": name_vacancy,
                           'city': city,
                           'salary': salary_from,
                           'requirement': requirement,
                           'url': url,
                           'sait': "HH"}
            formatted_vacancies.append(format_data)
        return formatted_vacancies


class SuperJobAPI(API):

    def __init__(self):
        self.vacancies_lst = []

    def get_api(self, keyword: str):
        """Получает список вакансий"""
        for page in range(10):
            sj_api_key = os.getenv('API_KEY_SJ')
            headers = {
                'X-Api-App-Id': sj_api_key,
            }

            param = {
                'keyword': keyword,
                'page': page,
                'count': 100
            }
            data = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=param).json()
            for i in data["objects"]:
                self.vacancies_lst.append(i)

        return self.vacancies_lst

    def get_formatted_vacancies(self):
        """Форматирует список вакансий"""
        formatted_vacancies = []
        for i in range(len(self.vacancies_lst)):
            name_vacancy = self.vacancies_lst[i]['profession']
            city = self.vacancies_lst[i]['town']['title']
            url = self.vacancies_lst[i]['link']
            requirement = self.vacancies_lst[i]['candidat']
            salary = self.vacancies_lst[i]['payment_from']
            if salary == 0:
                continue
            format_data = {"name_vacancy": name_vacancy,
                           'city': city,
                           'salary': salary,
                           'requirement': requirement,
                           'url': url,
                           'sait': "SJ"}
            formatted_vacancies.append(format_data)
        return formatted_vacancies

