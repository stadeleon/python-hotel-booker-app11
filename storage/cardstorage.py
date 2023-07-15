from storage.storage import Storage
from card import Card


class CardStorage(Storage):
    DATATYPE = {'number': str, 'cvc': int, 'balance': float}
    COLUMNS = 'number,expiration,cvc,holder,balance'

    def add(self, card: Card):
        self._items[card.number] = card

    def populate(self, data):
        for card in [Card(row) for row in data]:
            self.add(card)

    def is_card_exist(self, card_number: str, card_holder: str, expiration_date: str) -> bool:
        if card_number not in self._items:
            return False

        card = self._items[card_number]

        return card.holder == card_holder.upper() and card.expiration == expiration_date

    def pay(self, card_number, expiration_date, card_holder, cvc, payment_sum):
        if not self.is_card_exist(card_number, card_holder, expiration_date):
            return {'status': 401, 'error': 'Card is invalid'}

        card = self._items[card_number]
        validation = card.validate_payment(cvc, payment_sum)

        if validation['status'] != 200:
            return validation

        card.complete_payment(payment_sum)
        self._items[card_number] = card

        return {'status': 200, 'message': 'Payment complete'}



