from cardstorage import CardStorage


class PaymentProcessor:
    def __init__(self, card_number: str, card_holder: str, expiration_date: str):
        self.card_storage = CardStorage()
        self.card_storage.import_from_file("cards.csv")

        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date

    def is_valid_card(self) -> bool:
        return self.card_storage.is_card_exist(self.card_number, self.card_holder, self.expiration_date)

    def complete_payment(self, cvc: int, payment_sum: float):
        payment_result = self.card_storage.pay(
            self.card_number,
            self.expiration_date,
            self.card_holder,
            cvc,
            payment_sum
        )

        self.card_storage.export_to_file("cards.csv")

        return payment_result
