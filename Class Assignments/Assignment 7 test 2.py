#Purpose: To search in a binary matter without slicing
#Input: a list, the lowest position of a list, the highest position of the list, and the item being searched for
#Output: A confirmation of whether or not the item was found in the list
#Assumptions: A list will be inputted
def binary_searchrecursionnoslice(alist, low, high, item):
 
    if len(alist)==0: # Check base case
        return False
    elif high >= low:
        mid = (high + low) // 2
 
        if alist[mid] == item:  # If element is present at the middle itself
            return True
 
        
        elif alist[mid] > item: # If element is smaller than mid, then it can only be present on the left
            return binary_searchrecursionnoslice(alist, low, mid - 1, item)
 
        
        else: # Else the element can only be present on the right
            return binary_searchrecursionnoslice(alist, mid + 1, high, item)
 
    else: # Element is not present in the array
        return False
 
#Purpose:To test the adapted binary search method with an empty list
#Input: None
#Output: The result of the tests
#Assumptions: None
def testrecursivebinaryempty():
    alist = [ ]
    print(binary_searchrecursionnoslice(alist, 0, len(alist)-1, 2)) #test for item not in the list (b/c it's empty...): Should return False
 
#Purpose:To test the adapted binary search method with a list containing 1 item
#Input: None
#Output: The result of the tests
#Assumptions: None
def testrecursivebinaryone():
    alist = [1]
    print(binary_searchrecursionnoslice(alist, 0, len(alist)-1, 2)) #test for item not in list: Should return False
    print(binary_searchrecursionnoslice(alist, 0, len(alist)-1, 1)) #test for an item which is in the single item'd list: Should return True

#Purpose:To test the adapted binary search method with a list of many items
#Input: None
#Output: The result of the tests
#Assumptions: None
def testrecursivebinarymany():
    alist = [1,3,5,4,8,56,7]
    print(binary_searchrecursionnoslice(alist, 0, len(alist)-1, 3)) #test for item in large list which does exist: Should return True
    print(binary_searchrecursionnoslice(alist, 0, len(alist)-1, 56))#test for item in large list which does exist: Should return True
    print(binary_searchrecursionnoslice(alist, 0, len(alist)-1, 0)) #test for item in large list which is not there: Should return False

#Purpose:To test all of the testers for the adapted binary search method
#Input: None
#Output: The result of the tests
#Assumptions: None
def testallrecursivebinary():
    testrecursivebinaryempty()
    print("---------------------------------")
    testrecursivebinaryone()
    print("---------------------------------")
    testrecursivebinarymany()
    
    
    
    

