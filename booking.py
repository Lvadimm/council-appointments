"""Housing appointment booking for residents (prototype)."""


def validate_reference(reference):
    """Return an error message, or None if the housing reference is valid.

    A valid reference is "HR" followed by exactly 6 digits, e.g. HR123456.
    """
    reference = reference.strip()
    if reference == "":
        return "Please enter your housing reference"
    if len(reference) != 8 or not reference.startswith("HR") or not reference[2:].isdigit():
        return "Housing reference must be HR plus 6 digits"
    return None


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
        error = validate_reference(reference)
        if error:
            return BookingResult(False, error)

        if not self.is_available(slot):
            return BookingResult(False, "This slot is no longer available")

        self.slots[slot] = reference
        return BookingResult(True, f"Booking confirmed for {slot}")
