'''
Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
Example(Input => Output):

35231 => [1,3,2,5,3]
0 => [0]


'''

def digitize(n):
    n_answ =[]
    for i in str(n):
        n_answ.append(int(i))
    n_answ.reverse()
    return n_answ