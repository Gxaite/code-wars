'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

'''
def move_zeros(lst):
    result_list = []
    count=0
    for i in lst:
        if i != 0:
            result_list.append(i)
        else:
            count+=1
    for j in range(0,count):
        result_list.append(0)
    return result_list