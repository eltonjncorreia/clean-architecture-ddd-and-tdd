from datetime import datetime
from datetime import timedelta
from unittest import TestCase

from booking.domain.booking.entities import Booking
from booking.domain.booking.exceptions import CheckinDateCannotBeAfterCheckoutDate
from booking.domain.booking.exceptions import CustomerNameRequired
from booking.domain.booking.exceptions import ErrorCodes
from booking.domain.customers.entities import Customer


class BookingEntityTestCase(TestCase):

    def test_raise_exception_when_checkin_date_be_after_checkout_date(self) -> None:
        checkin: datetime = datetime.today()
        checkout: datetime = datetime.today() - timedelta(days=1)
        customer: Customer = Customer(name="Michel Corleone")

        booking: Booking = Booking(checkin, checkout, customer)

        with self.assertRaises(CheckinDateCannotBeAfterCheckoutDate) as e:
            booking.is_valid()

            self.assertEqual(e.exception.message, ErrorCodes.CHECKINAFTERCHECKOUT)

    def test_raise_exception_when_booking_should_not_has_name_of_customer(self) -> None:
        checkin: datetime = datetime.today()
        checkout: datetime = datetime.today() + timedelta(days=5)
        customer: Customer = Customer(name="")

        booking: Booking = Booking(checkin, checkout, customer)

        with self.assertRaises(CustomerNameRequired) as e:
            booking.is_valid()

            self.assertEqual(e.exception.message, ErrorCodes.CUSTOMERISREQUIRED)

    def test_create_new_booking_with_success(self) -> None:
        checkin: datetime = datetime.today()
        checkout: datetime = datetime.today() + timedelta(days=5)
        customer: Customer = Customer(name="Jonh")

        booking: Booking = Booking(checkin, checkout, customer)

        self.assertTrue(booking.is_valid())
