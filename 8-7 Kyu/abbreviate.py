'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

'''

def abbrev_name(name):
    surname = False
    first_name = name[0]
    for i in name:
        if surname:
            second_name = i
            surname = False
        if i ==" ":
            surname = True
    return f"{first_name.upper()}.{second_name.upper()}"