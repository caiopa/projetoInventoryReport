from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, lista):
        now = str(date.today())

        company = [item["nome_da_empresa"] for item in lista]

        count_company = Counter(company).most_common()[0][0]

        manufacturing_dates = [item["data_de_fabricacao"] for item in lista]

        old_manufacturing_dates = min(manufacturing_dates)

        expired_dates = [
            item["data_de_validade"] for item in lista
            if item["data_de_validade"] >= now
        ]

        next_expired_date = min(expired_dates)

        return (
            f"Data de fabricação mais antiga: {old_manufacturing_dates}\n"
            f"Data de validade mais próxima: {next_expired_date}\n"
            f"Empresa com mais produtos: {count_company}"
        )

    @classmethod
    def get_company(cls, list):
        company = [item["nome_da_empresa"] for item in list]
        return Counter(company)
