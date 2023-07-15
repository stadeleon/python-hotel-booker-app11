from storage.storage import Storage


class PasswordStorage(Storage):
    def populate(self, data):
        for password in data:
            self._items[password['number']] = password
            # self.add(data)

    DATATYPE = {'number': str, 'password': str}
    COLUMNS = 'number,password'

    def is_card_secured(self, card_number: str) -> bool:
        return card_number in self._items

    def validate(self, card_number: str, password: str) -> bool:
        return self._items[card_number]['password'] == password
