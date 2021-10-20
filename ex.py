def count_rotations_linear(nums):
    
    position = 0                 # What is the intial value of position?
    
    while True:                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and position<position-1:   # How to perform the check?
            return position
    
        
        # Move to the next position
        position += 1
        print(position)
    return 0 
count_rotations_linear([19,25,29,3,5,6,7,9,11,14])                    # What if none of the positions passed the check               4
