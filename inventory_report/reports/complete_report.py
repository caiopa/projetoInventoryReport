from inventory_report.reports.simple_report import SimpleReport


# https://pencilprogrammer.com/python-self-vs-cls/#:~:text=cls%20in%20Python%20holds%20the,classmethod%20decorator)%20by%20Python%20itself.&text=It%20is%20important%20to%20note,just%20naming%20conventions%20in%20Python.


class CompleteReport(SimpleReport):
    pass

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)

        companies = cls.get_company(list)
        # print(companies.items())
        simple_report += "\nProdutos estocados por empresa:\n"
        for company, qnty in companies.items():
            simple_report += f"- {company}: {qnty}\n"
        return simple_report
