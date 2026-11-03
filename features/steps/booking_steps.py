# Step definitions: each function links one Gherkin line to Python code.
# behave matches the text in the decorator, {name} values are passed in.
from behave import given, when, then

from booking import AppointmentBook


@given("the housing office has these free slots:")
def step_free_slots(context):
    # context.table holds the table from the feature file
    slots = [row["slot"] for row in context.table]
    # context is shared between steps of one scenario
    context.book = AppointmentBook(slots)


@given('the slot "{slot}" has already been booked by "{reference}"')
def step_slot_taken(context, slot, reference):
    # Set up the "slot taken" situation by booking it first
    context.book.book(reference, slot)


@given('a resident with housing reference "{reference}"')
def step_resident(context, reference):
    context.reference = reference


@given('a resident with housing reference ""')
def step_resident_empty(context):
    # Separate step because {reference} does not match an empty string
    context.reference = ""


@when('the resident books the slot "{slot}"')
def step_book(context, slot):
    # Keep the result so the Then steps can check it
    context.result = context.book.book(context.reference, slot)


@then("the booking is confirmed")
def step_confirmed(context):
    # assert fails the scenario if the condition is False
    assert context.result.success, context.result.message


@then('the booking is rejected with the message "{message}"')
def step_rejected(context, message):
    assert not context.result.success, "Booking should have been rejected"
    # Check the exact text the resident would see
    assert context.result.message == message, (
        f'Expected "{message}" but got "{context.result.message}"'
    )


@then('the slot "{slot}" is no longer available')
def step_not_available(context, slot):
    assert not context.book.is_available(slot)


@then('the slot "{slot}" is still available')
def step_still_available(context, slot):
    # A rejected booking must not block the slot
    assert context.book.is_available(slot)
