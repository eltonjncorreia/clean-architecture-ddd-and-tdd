from enum import Enum


class ErrorCodes(Enum):
    CHECKINAFTERCHECKOUT = "checkin cannot be after checkout"
    CUSTOMERISREQUIRED = "customer name is required"


class CheckinDateCannotBeAfterCheckoutDate(Exception):
    def __init__(self, message: str, code: str = ErrorCodes.CHECKINAFTERCHECKOUT) -> None:
        self.message = message
        self.code = code


class CustomerNameRequired(Exception):
    def __init__(self, message: str, code: str = ErrorCodes.CUSTOMERISREQUIRED) -> None:
        self.message = message
        self.code = code
