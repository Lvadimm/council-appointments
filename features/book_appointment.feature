Feature: Book a housing appointment
  As a resident applying for council housing
  I want to book an appointment with a housing officer online
  So that I do not have to phone or queue at the council office

  # Background runs before every scenario, so each starts with the same free slots
  Background:
    Given the housing office has these free slots:
      | slot             |
      | 2026-11-10 09:00 |
      | 2026-11-10 09:30 |

  Scenario: Resident books a free slot
    Given a resident with housing reference "HR123456"
    When the resident books the slot "2026-11-10 09:00"
    Then the booking is confirmed
    And the slot "2026-11-10 09:00" is no longer available

  Scenario: Resident tries to book a slot that is already taken
    Given the slot "2026-11-10 09:30" has already been booked by "HR654321"
    And a resident with housing reference "HR123456"
    When the resident books the slot "2026-11-10 09:30"
    Then the booking is rejected with the message "This slot is no longer available"

  # Scenario Outline runs once per row in Examples (empty, too short, too long, wrong prefix)
  Scenario Outline: Resident enters an invalid housing reference
    Given a resident with housing reference "<reference>"
    When the resident books the slot "2026-11-10 09:00"
    Then the booking is rejected with the message "<message>"
    And the slot "2026-11-10 09:00" is still available

    Examples:
      | reference | message                                    |
      |           | Please enter your housing reference        |
      | HR12345   | Housing reference must be HR plus 6 digits |
      | HR1234567 | Housing reference must be HR plus 6 digits |
      | AB123456  | Housing reference must be HR plus 6 digits |
