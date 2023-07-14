from user import User
from reservation import Reservation
from hotelstorage import HotelStorage
from paymentprocessor import PaymentProcessor


hotels = HotelStorage()
hotels.import_from_file("hotels.csv")

while True:
    print(hotels)

    hotel_id = int(input('Enter The hotel ID: '))
    hotel = hotels.get_by_id(hotel_id)

    if hotel.is_available():
        print("Hotel is Available")
        user_name = input("Enter your name: ")
        user = User(0, user_name)

        card_number = input("Enter card number for payment process:")
        holder = input("Enter Card Holder Name")
        expiration_date = input("Enter card expiration date:")
        payp = PaymentProcessor(card_number, holder, expiration_date)

        if not payp.is_valid_card():
            print("Invalid card fill your data again")
            continue

        cvc = int(input("Enter Card Secret CVC code: "))

        payment = payp.complete_payment(cvc, hotel.price)

        if payment['status'] != 200:
            print(payment['error'])
            continue

        reservation = Reservation(user, hotel)
        reservation.complete()
        print(reservation.generate_receipt())

        hotels.export_to_file("hotels.csv")
    else:
        print("NO MORE ROOMS!!")
