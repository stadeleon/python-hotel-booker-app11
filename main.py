from user import User
from reservation import Reservation
from spareservation import SpaReservation
from storage.hotelstorage import HotelStorage
from processor.secured_paymentprocessor import SecuredPaymentProcessor


hotels = HotelStorage()
hotels.import_from_file("storage/data/hotels.csv")

while True:
    print(hotels)

    hotel_id = int(input('Enter The hotel ID: '))
    hotel = hotels.get_by_id(hotel_id)

    if hotel.is_available():
        print("Hotel is Available")
        user_name = input("Enter your name: ") or 'Leo'
        user = User(0, user_name)

        card_number = input("Enter card number for payment process:") or '1234'

        holder = input("Enter Card Holder Name") or 'John Smith'
        expiration_date = input("Enter card expiration date:") or '12/26'
        payp = SecuredPaymentProcessor(card_number, holder, expiration_date)

        if payp.is_secured(card_number):
            password = input("Enter Your card security password") or 'mypass'
            if not payp.check_password(card_number, password):
                print("Invalid security password, operation cancelled")
                continue

            print("Secure Payment granted")

        if not payp.is_valid_card():
            print("Invalid card fill your data again")
            continue

        cvc = int(input("Enter Card Secret CVC code: ") or '123')

        payment = payp.complete_payment(cvc, hotel.price)
        if payment['status'] != 200:
            print(payment['error'])
            continue

        reservation = Reservation(user, hotel)
        reservation.complete()
        print(reservation.generate_receipt())

        spa = input('Do you want to book a SPA package? (yes/no)')
        if 'yes' == spa.lower():
            spa_reservation = SpaReservation(user, hotel)
            print(spa_reservation.generate_receipt())

        hotels.export_to_file("storage/data/hotels.csv")
    else:
        print("NO MORE ROOMS!!")
