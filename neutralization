'''Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

    When positives and positives interact, they remain positive.
    When negatives and negatives interact, they remain negative.
    But when negatives and positives interact, they become neutral, and are shown as the number 0.

Worked Example

("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.'''

def neutralise(s1, s2):
    result_list = ""
    i=0
    while i< len(s1):
        
        if s1[i]!=s2[i]:
            result_list += "0"
        else:
            result_list+= str(s1[i])
        i +=1
        
    return result_list

