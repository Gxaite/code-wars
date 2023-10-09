'''You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
Strings
Fundamentals'''
def likes(names):
    count = 0
    if names==[]:
        return "no one likes this"
    for name in names:
        count +=1 
    
    if count == 1:
        return "{} likes this".format(*names)
    elif count == 2:
        return "{} and {} like this".format(*names)
    elif count == 3:
        return "{}, {} and {} like this".format(*names)
    else:
        count-=2
        return f"{names[0]}, {names[1]} and "+str(count)+" others like this"
    