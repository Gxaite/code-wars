'''
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
'''
def repeat_str(repeat, string):

    string_answ =''
    
    for i in range(0,repeat):
        string_answ += string
    return string_answ