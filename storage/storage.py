import pandas as pd
from abc import ABC, abstractmethod


class Storage(ABC):

    DATATYPE = {}
    COLUMNS = ''

    def __init__(self):
        self._items = {}

    def import_from_file(self, filename):
        df = pd.read_csv(filename, dtype=self.DATATYPE)
        data = pd.DataFrame(df).to_dict('index')
        self.populate(data.values())

    def export_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

    def __str__(self):
        result = self.COLUMNS + '\n'
        for item in self._items.values():
            result += str(item) + '\n'
        return result

    @abstractmethod
    def populate(self, data):
        pass
