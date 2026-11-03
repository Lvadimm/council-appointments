"""Housing appointment booking for residents (prototype)."""


class BookingResult:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class AppointmentBook:
    def __init__(self, slots):
        self.slots = {}

    def book(self, reference, slot):
        raise NotImplementedError("Booking not written yet")

    def is_available(self, slot):
        raise NotImplementedError("Availability check not written yet")
