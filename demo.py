"""Small console demo of the booking prototype."""

from booking import AppointmentBook

book = AppointmentBook(["2026-11-10 09:00", "2026-11-10 09:30"])

for reference, slot in [
    ("HR123456", "2026-11-10 09:00"),  # normal booking
    ("HR654321", "2026-11-10 09:00"),  # slot already taken
    ("HR12", "2026-11-10 09:30"),      # invalid reference
]:
    result = book.book(reference, slot)
    status = "OK " if result.success else "NO "
    print(f"{status}{reference:<10} {slot}  ->  {result.message}")
