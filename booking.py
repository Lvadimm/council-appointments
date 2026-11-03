"""Housing appointment booking for residents (prototype)."""


def validate_reference(reference):
    """Return an error message, or None if the housing reference is valid.

    A valid reference is "HR" followed by exactly 6 digits, e.g. HR123456.
    """
    # strip() removes spaces a user may type by accident
    reference = reference.strip()

    # Empty input gets its own message so the resident knows what to fix
    if reference == "":
        return "Please enter your housing reference"

    # Check length, prefix and digits in one rule (HR + 6 digits = 8 chars)
    if len(reference) != 8 or not reference.startswith("HR") or not reference[2:].isdigit():
        return "Housing reference must be HR plus 6 digits"

    return None


class BookingResult:
    # Small object so callers get both the outcome and a message to show
    def __init__(self, success, message):
        self.success = success
        self.message = message


class AppointmentBook:
    def __init__(self, slots):
        # Dictionary: slot -> housing reference, None means the slot is free.
        # A dict gives fast lookup by slot time.
        self.slots = {slot: None for slot in slots}

    def is_available(self, slot):
        # A slot must exist and not be booked yet
        return slot in self.slots and self.slots[slot] is None

    def book(self, reference, slot):
        # Validate input first, before changing any data
        error = validate_reference(reference)
        if error:
            return BookingResult(False, error)

        # Save the cleaned reference, not the raw user input
        reference = reference.strip()

        # Stops double booking of the same slot
        if not self.is_available(slot):
            return BookingResult(False, "This slot is no longer available")

        self.slots[slot] = reference
        return BookingResult(True, f"Booking confirmed for {slot}")
