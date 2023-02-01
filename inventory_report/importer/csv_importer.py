from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    def import_data(path: str):
        with open(path, encoding='utf-8') as file:
            if "csv" not in path:
                raise ValueError('Arquivo inválido')
            else:
                data = csv.DictReader(file, delimiter=",", quotechar='"')

            return list(data)
