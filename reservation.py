from user import User
from hotel import Hotel


class Reservation:
    def __init__(self, user: User, hotel: Hotel):
        self.user = user
        self.hotel = hotel

    def complete(self):
        self.hotel.book()

    def generate_receipt(self) -> str:
        return f"""
Thank you for your reservation!
Here are your booking data:
Name: {self.user.get_name()}
Hotel name: {self.hotel.name}
"""
