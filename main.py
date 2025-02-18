"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb
    

def longest_run(mylist, key):
    """Returns the longest continuous sequence of 'key' in 'mylist'."""
    longest_run = 0
    current_run = 0
    for i in mylist:
        if i == key:
            current_run += 1
        else:
            current_run = 0
        if current_run > longest_run:
            longest_run = current_run
    return longest_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    """Returns the longest continuous sequence of 'key' in 'mylist'"""
#base cases: empty list and one item
    if len(mylist) == 0: 
        return Result(0, 0, 0, True)
        
    elif len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    #>1 item in array - recursive cases     
    else:
        #split list into two halves
        halfWay = len(mylist)//2 
        left_result = longest_run_recursive(mylist[:halfWay], key)
        right_result = longest_run_recursive(mylist[halfWay:], key)
        
        #compute left size for Result
        left_size = left_result.left_size
        #if the left result is the entire range, add the left size of the right result bc it may continue there
        if left_result.is_entire_range: 
            left_size += right_result.left_size
        #compute right size for Result
        right_size = right_result.right_size
        #if the right result is the entire range, add the right size of the left result bc it may continue there
        if right_result.is_entire_range:
            right_size += left_result.right_size

        #compute the crossover of the left and right results 
        crossover = left_result.right_size + right_result.left_size
        #compute longest size (for Result) which is the max of the left result, right result, and crossover of the two
        longest_size = max(left_result.longest_size, right_result.longest_size, crossover)
        
        #compute is_entire_range (for Result) which is true when the left result is the entire range and the right result is the entire range
        is_entire_range = left_result.is_entire_range and right_result.is_entire_range


    #return the result - values come from the Result class 
    return Result(left_size, right_size, longest_size, is_entire_range)
    
