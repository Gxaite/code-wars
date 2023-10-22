'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
Examples

[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

'''

def find_outlier(integers):
    odd_count = even_count = last_even = last_odd = 0
    
    for i in integers:
        if i%2==0:
            even_count += 1
            last_even = i
        else:
            odd_count += 1
            last_odd = i
    
    if odd_count == 1:
        return last_odd
    
    elif even_count == 1:
        return last_even