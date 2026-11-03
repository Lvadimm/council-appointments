"""Housing appointment booking for residents (prototype)."""


class BookingResult:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class AppointmentBook:
    def __init__(self, slots):
        # Each slot maps to the housing reference that booked it,
        # or None while the slot is still free.
        self.slots = {slot: None for slot in slots}

    def is_available(self, slot):
        return slot in self.slots and self.slots[slot] is None

    def book(self, reference, slot):
        if not self.is_available(slot):
            return BookingResult(False, "This slot is no longer available")

        self.slots[slot] = reference
        return BookingResult(True, f"Booking confirmed for {slot}")
