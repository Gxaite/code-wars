'''
Your task is to make a function that can take any non-negative integer as an argument and return it
 with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

'''
def descending_order(num):
    str_num = str(num)
    answ_sorted_str = ''.join(sorted(str_num, reverse=True))
    return int(answ_sorted_str)
