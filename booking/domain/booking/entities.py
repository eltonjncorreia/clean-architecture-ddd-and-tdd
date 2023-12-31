from dataclasses import dataclass
from datetime import datetime
from booking.domain.customers.entities import Customer
from booking.domain.booking.exceptions import CheckinDateCannotBeAfterCheckoutDate
from booking.domain.booking.exceptions import CustomerNameRequired


@dataclass
class Booking:
    checkin: datetime
    checkout: datetime
    customer: Customer

    def is_valid(self) -> bool:
        if self.checkin > self.checkout:
            raise CheckinDateCannotBeAfterCheckoutDate("checkin cannot be after checkout")

        elif not self.customer.name:
            raise CustomerNameRequired("customer name is required")

        return True
