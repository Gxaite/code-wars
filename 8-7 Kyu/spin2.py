'''
Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the array counts as a 90° rotation in that direction.
Worked Example

["right", "right", "right", "right", "left", "right"] ➞ 1
# You spun right 4 times (90 * 4 = 360)
# You spun left once (360 - 90 = 270)
# But you spun right once more to make a full rotation (270 + 90 = 360)

My first Code
def spin_around(lst):
    count_right = count_left = 0
    for i in lst:
        if i == "right":
            count_right += 1
        else: 
            count_left += 1
    
    return abs(count_right * 90 -count_left * 90)//360
            
    
    
'''
def spin_around(lst):
    return abs(lst.count("right") - lst.count("left"))//4
            
    
    
        