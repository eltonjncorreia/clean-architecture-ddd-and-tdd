from dataclasses import dataclass
from datetime import datetime

from booking.domain.booking.entities import Booking
from booking.domain.customers.entities import Customer

"""
DTO data transfer object
serve apenas para transportar dados de uma camanda para outra
"""


@dataclass
class BookingDTO:
    checkin: datetime
    checkout: datetime
    customer: Customer

    def to_domain(self) -> Booking:
        return Booking(self.checkin, self.checkout, self.customer)