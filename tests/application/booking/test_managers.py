from datetime import datetime
from datetime import timedelta
from unittest import TestCase

from booking.application.booking.dtos import BookingDTO
from booking.application.booking.managers import BookingManager
from booking.domain.customers.entities import Customer


class BookingManagerTestCase(TestCase):

    def test_checkin_date_cannot_be_after_checkout_date(self) -> None:
        checkin: datetime = datetime.today()
        checkout: datetime = datetime.today() - timedelta(days=1)
        customer: Customer = Customer(name="Michel Corleone")

        booking_dto: BookingDTO = BookingDTO(checkin, checkout, customer)
        manager: BookingManager = BookingManager()
        response: dict = manager.create_new_booking(booking_dto)

        self.assertEqual(response["message"], 'checkin cannot be after checkout')

    def test_booking_should_has_a_name_of_the_customer(self) -> None:
        checkin: datetime = datetime.today()
        checkout: datetime = datetime.today() + timedelta(days=5)
        customer: Customer = Customer(name="")

        booking_dto: BookingDTO = BookingDTO(checkin, checkout, customer)
        manager: BookingManager = BookingManager()
        response: dict = manager.create_new_booking(booking_dto)

        self.assertEqual(response["message"], 'customer name is required')

    def test_create_new_booking_with_success(self) -> None:
        checkin: datetime = datetime.today()
        checkout: datetime = datetime.today() + timedelta(days=1)
        customer: Customer = Customer(name="Michel Corleone")

        booking_dto: BookingDTO = BookingDTO(checkin, checkout, customer)
        manager: BookingManager = BookingManager()
        response: dict = manager.create_new_booking(booking_dto)

        self.assertEqual(response["message"], "Saved")
