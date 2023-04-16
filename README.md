3_course_work

Project of the third course work on the topic 
"basics of backend development".

The project implements the Code for the "Account Transactions" widget

## Task

Implements a function that displays a list of the last 5 operations performed by the client in the format:

#<transfer date> <transfer description>
#<from> -> <where>
#<transfer amount> <currency>

# Sample output for one operation:

10/14/2018 Organization transfer
Visa Platinum 7000 79** **** 6361 -> Account **9638
82771.72 rub


### Requirements

- The last 5 EXECUTED operations are displayed.
- Operations are separated by an empty line.
- The transfer date is presented in the format DD.MM.YYYY (example: 10/14/2018).
- At the top of the list are the most recent transactions (by date).
- The card number is masked and not displayed in full in the XXXX XX** **** XXXX format (the first 6 digits and the last 4 are visible, divided into blocks of 4 digits separated by a space).
- Account number is masked and not displayed in full in **XXXX format
(only the last 4 digits of the account number are visible).