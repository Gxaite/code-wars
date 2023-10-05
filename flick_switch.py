'''Create a function that always returns True for every item in a given list. However, if an element is the word 'flick', switch to always returning the opposite boolean value.
Examples

['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]'''


def flick_switch(lst):
    resp_list = []
    switch = True
    
    for item in lst:
        if item == 'flick':
            switch = not switch 
        resp_list.append(switch)   
    
    return resp_list