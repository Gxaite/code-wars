'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

'''
def to_camel_case(text):
    symbols = "_-"
    answ_string = ""
    next_word = False
    for i in text:
        if next_word == True:
            answ_string += i.upper()
            next_word = False
            continue
        if i in symbols:
            next_word = True
        else:
            answ_string += i
    
    return answ_string