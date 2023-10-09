'''You get an array of numbers, return the sum of all of the positives ones.'''
def positive_sum(arr):
    soma = 0
    i= 0
    for i in arr:
        if i>=0:
            soma+=i
    
    if soma <= 0:
        return 0
    else:
        return soma