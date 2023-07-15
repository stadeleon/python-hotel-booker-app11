from reservation import Reservation


class SpaReservation(Reservation):
    def generate_receipt(self) -> str:
        return f"""
Thank you for your SPA reservation!
Here are your SPA booking data:
Name: {self.user.get_name()}
Hotel name: {self.hotel.name}
"""
