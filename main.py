from user import User
from reservation import Reservation
from hotelstorage import HotelStorage


hotels = HotelStorage()
hotels.import_from_file("hotels.csv")

while True:
    print(hotels)

    hotel_id = int(input('Enter The hotel ID: '))
    hotel = hotels.get_by_id(hotel_id)

    if hotel.is_available():
        print("Hotel is Available")
        user_name = input("Enter your name for reservation: ")
        user = User(0, user_name)
        reservation = Reservation(user, hotel)
        reservation.complete()

        print(reservation.generate_receipt())
        hotels.export_to_file("hotels2.csv")
    else:
        print("NO MORE ROOMS!!")
