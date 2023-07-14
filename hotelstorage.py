import pandas as pd
from hotel import Hotel


class HotelStorage:
    def __init__(self):
        self.hotels_list = {}

    def populate(self, data):
        for hotel in [Hotel(row) for row in data]:
            self.add(hotel)

    def import_from_file(self, filename):
        df = pd.read_csv(filename, dtype={'id': int, 'capacity': int})
        data = pd.DataFrame(df).to_dict('index')
        self.populate(data.values())

    def export_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

    def add(self, hotel: Hotel):
        self.hotels_list[hotel.id] = hotel

    def list(self):
        return self.hotels_list

    def get_by_id(self, hotel_id):
        return self.hotels_list[hotel_id]

    def __str__(self):
        result = 'id,name,city,capacity,available\n'
        for hotel in self.hotels_list.values():
            result += str(hotel) + '\n'
        return result
