import requests
from tabulate import tabulate

class CountryInfo:
    API_URL = 'https://restcountries.com/v3.1/all'

    def fetch_data(self):
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error fetching data from API")
            return None

    def get_country_info(self):
        data = self.fetch_data()
        if data is None:
            return

        country_info_list = []
        for country in data:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]  # для тих країн що не мають столиць
            flag_url = country.get('flags', {}).get('png', 'N/A')

            country_info_list.append([name, capital, flag_url])

        self.print_table(country_info_list)

    def print_table(self, data):
        headers = ["Country", "Capital", "Flag URL"]
        table = tabulate(data, headers, tablefmt="grid")
        print(table)

# Використання класу
country_info = CountryInfo()
country_info.get_country_info()
