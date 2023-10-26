'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false


'''
def xo(s):
    count_x = count_o = 0
    if 'x' not in s and 'o' not in s:
        return True
    for i in s:
        if i.lower() == 'x':
            count_x += 1
        elif i.lower()== 'o':
            count_o += 1
    
    if count_x == count_o:
        return True
    else:
        return False