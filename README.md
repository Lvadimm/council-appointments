# Council Housing Appointment Booking (BDD prototype)

Small Python prototype for SWE6301 Agile Programming, Assignment 1 (Task 2).

Residents of a local authority can book a face-to-face appointment with a
housing officer. The prototype checks the resident's housing reference,
checks that the time slot exists and is free, and then confirms the booking.

The expected behaviour is written first as Gherkin scenarios in
`features/book_appointment.feature` and is run with `behave`.

## User story

As a resident applying for council housing,
I want to book an appointment with a housing officer online,
so that I do not have to phone or queue at the council office.

## Run it

```
python -m pip install -r requirements.txt
behave
```

Optional quick demo:

```
python demo.py
```
