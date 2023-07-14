import pandas as pd
from abc import ABC, abstractmethod


class Storage(ABC):

    DATATYPE = {}

    def import_from_file(self, filename):
        df = pd.read_csv(filename, dtype=self.DATATYPE)
        data = pd.DataFrame(df).to_dict('index')
        self.populate(data.values())

    def export_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

    @abstractmethod
    def populate(self, data):
        pass
