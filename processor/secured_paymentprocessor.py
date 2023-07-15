from processor.paymentprocessor import PaymentProcessor
from storage.passwordstorage import PasswordStorage


class SecuredPaymentProcessor(PaymentProcessor):
    def __init__(self, card_number: str, card_holder: str, expiration_date: str):
        self.passtorage = PasswordStorage()
        self.passtorage.import_from_file('storage/data/card_security.csv')

        super().__init__(card_number, card_holder, expiration_date)

    def check_password(self, number: str, password: str):
        return self.passtorage.validate(number, password)

    def is_secured(self, number: str):
        return self.passtorage.is_card_secured(number)
