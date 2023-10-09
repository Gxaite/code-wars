'''
Complete the function which converts a binary number (given as a string) to a decimal number.
'''

def bin_to_decimal(inp):
    expoent = number_result = 0
    
    for i in inp[::-1]:
        number_result += int(i)*(2**expoent)
        expoent+=1
    return number_result
