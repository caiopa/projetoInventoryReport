from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    def import_data(path: str):
        with open(path) as file:
            try:
                data = json.loads(file.read())
            except Exception:
                raise ValueError("Arquivo inválido")

            return list(data)
