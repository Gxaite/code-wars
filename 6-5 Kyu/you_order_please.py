'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""


'''
def order(sentence):
    #return "" if sentence == ""
    if sentence == "": return ""

    #Split string in a list
    sentence_split = sentence.split()
    
    #Create a sorted list, with the size of words in sentence
    sentence_sorted = [None] * len(sentence_split)
    
    #Use a for to pass in words and chars
    for word in sentence_split:
        for char in word:
            if char.isdigit():
                position = int(char)-1 #save char index in sorted list
                sentence_sorted[position] = word #saving word in the correct index
    
    #Transform list in string and return the result
    result = " ".join(sentence_sorted)
    return result

