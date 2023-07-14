from datetime import datetime


class Card:
    def __init__(self, data: dict):
        self.number = data['number']
        self.expiration = data['expiration']
        self.cvc = int(data['cvc'])
        self.holder = data['holder']
        self.balance = data['balance']

    def is_valid(self) -> bool:
        card_expiration = datetime.strptime(self.expiration, "%M/%y")
        today = datetime.now()

        return card_expiration >= today

    def validate_payment(self, cvc: int, payment_sum: float):
        if not self.is_valid():
            return {'status': 401, 'error': 'Card outdated, use new card'}

        if self.cvc != cvc:
            return {'status': 401,
                    'error': 'Security code is invalid, card will be blocked after three incorrect enter'}

        if self.balance < payment_sum:
            return {'status': 401,
                    'error': 'Not Enough Money, Need more Gold!!'}

        return {'status': 200, 'error': ''}

    def complete_payment(self, payment_sum: float):
        self.balance -= payment_sum

    def __str__(self):
        return f"{self.number},{self.expiration},{self.cvc},{self.holder},{self.balance:.2f}"
