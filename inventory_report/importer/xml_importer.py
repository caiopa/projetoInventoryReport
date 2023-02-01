from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):

    def import_data(path: str):
        with open(path, encoding='utf-8') as file:
            try:
                files = file.read()
                data = xmltodict.parse(files)["dataset"]['record']
            except Exception:
                raise ValueError("Arquivo inválido")

            return list(data)
