'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
Examples

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.


'''

def high_and_low(numbers):
    new_number = numbers.split()
    higher = int(new_number[0])
    lower = int(new_number[0])
    for i in new_number:
        int_i = int(i)
        if int_i >= higher:
            higher = int_i
        if int_i<= lower:
            lower = int_i 
    return f"{higher} {lower}"  

