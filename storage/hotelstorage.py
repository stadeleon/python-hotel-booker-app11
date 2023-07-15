from storage.storage import Storage
from hotel import Hotel


class HotelStorage(Storage):
    DATATYPE = {'id': int, 'capacity': int, 'price': float}
    COLUMNS = 'id,name,city,capacity,price,available'

    def populate(self, data):
        for hotel in [Hotel(row) for row in data]:
            self.add(hotel)

    def add(self, hotel: Hotel):
        self._items[hotel.id] = hotel

    def list(self):
        return self._items

    def get_by_id(self, hotel_id):
        return self._items[hotel_id]

