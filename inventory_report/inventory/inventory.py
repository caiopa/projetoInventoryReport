from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:

    @classmethod
    def import_data(cls, path: str, type: str):
        if "csv" in path:
            data = CsvImporter.import_data(path)
        if "json" in path:
            data = JsonImporter.import_data(path)
        if "xml" in path:
            data = XmlImporter.import_data(path)

        return (
            SimpleReport.generate(data) if type == "simples"
            else CompleteReport.generate(data)
        )
