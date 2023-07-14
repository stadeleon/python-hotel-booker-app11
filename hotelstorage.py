from storage import Storage
from hotel import Hotel


class HotelStorage(Storage):
    DATATYPE = {'id': int, 'capacity': int, 'price': float}

    def __init__(self):
        self.hotels = {}

    def populate(self, data):
        for hotel in [Hotel(row) for row in data]:
            self.add(hotel)

    def add(self, hotel: Hotel):
        self.hotels[hotel.id] = hotel

    def list(self):
        return self.hotels

    def get_by_id(self, hotel_id):
        return self.hotels[hotel_id]

    def __str__(self):
        result = 'id,name,city,capacity,price,available\n'
        for hotel in self.hotels.values():
            result += str(hotel) + '\n'
        return result
