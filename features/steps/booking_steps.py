from behave import given, when, then

from booking import AppointmentBook


@given("the housing office has these free slots:")
def step_free_slots(context):
    slots = [row["slot"] for row in context.table]
    context.book = AppointmentBook(slots)


@given('the slot "{slot}" has already been booked by "{reference}"')
def step_slot_taken(context, slot, reference):
    context.book.book(reference, slot)


@given('a resident with housing reference "{reference}"')
def step_resident(context, reference):
    context.reference = reference


@given('a resident with housing reference ""')
def step_resident_empty(context):
    context.reference = ""


@when('the resident books the slot "{slot}"')
def step_book(context, slot):
    context.result = context.book.book(context.reference, slot)


@then("the booking is confirmed")
def step_confirmed(context):
    assert context.result.success, context.result.message


@then('the booking is rejected with the message "{message}"')
def step_rejected(context, message):
    assert not context.result.success, "Booking should have been rejected"
    assert context.result.message == message, (
        f'Expected "{message}" but got "{context.result.message}"'
    )


@then('the slot "{slot}" is no longer available')
def step_not_available(context, slot):
    assert not context.book.is_available(slot)


@then('the slot "{slot}" is still available')
def step_still_available(context, slot):
    assert context.book.is_available(slot)
