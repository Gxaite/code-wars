'''The goal of this kata is two-fold:

1.) You must produce a fibonacci sequence in the form of an array, containing a number of items equal to the input provided.

2.) You must replace all numbers in the sequence divisible by 3 with Fizz, those divisible by 5 with Buzz, and those divisible by both 3 and 5 with FizzBuzz.

For the sake of this kata, you can assume all input will be a positive integer.
Use Cases

Return output must be in the form of an array, with the numbers as integers and the replaced numbers (fizzbuzz) as strings.
Examples

Input:

fibs_fizz_buzz(5)

Output:

[ 1, 1, 2, 'Fizz', 'Buzz' ]

Input:

fibs_fizz_buzz(1)

Output:

[1]'''

def fibs_fizz_buzz(n):
    answ_list = []
    first_digit, second_digit = 1,1
    for i in range(n):
        
        if first_digit%3==0 and first_digit%5==0:
            answ_list.append("FizzBuzz")
            
        elif first_digit%3==0:
            answ_list.append("Fizz")
            
        elif first_digit%5==0:
            answ_list.append("Buzz")
            
        else:
            answ_list.append(first_digit)      
            
        first_digit, second_digit = second_digit, first_digit+second_digit   
        
    return answ_list 