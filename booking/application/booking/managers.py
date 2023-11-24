"""Use cases
Orquestrador entre os controllers e entidades")
Onde é implementado os casos de uso")
Esse modulo 'managers' também as vezes é nomeado de 'services'")
"""
from typing import Dict

from booking.application.booking.dtos import BookingDTO
from booking.domain.booking.exceptions import CheckinDateCannotBeAfterCheckoutDate, CustomerNotFound


class BookingManager(object):

    def create_new_booking(self, bookingDTO: BookingDTO) -> Dict:
        domain = bookingDTO.to_domain()

        try:
            if domain.is_valid():
                return {"message": "Saved"}
            else:
                return {"message": "not save"}

        except (CheckinDateCannotBeAfterCheckoutDate, CustomerNotFound) as e:
            return {"message": e.message, "code": e.code}
