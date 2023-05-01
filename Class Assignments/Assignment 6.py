#Purpose:To create a recursive palindrome checker function
#Input: A string
#Output: True or False, based on the string entered
#Assumptions: A string will be inputted
def palchecker(astring):
    if len(astring)<2: #tests if length of string is 1 or is 0(empty)- b/c that means it is a palindrome
        return True
    if astring[0] !=astring[-1]: #checking if the first letter(the position of it) is equal to the last letter-of it not-not a palindrome
        return False
    else:
        return palchecker(astring[1:-1]) #slices first and last letters of the string until the string is sufficiently small enough to trigger first if statement

#Purpose:To test the recursive palindrome checker function w/ no values inside
#Input: None
#Output: The result of each test case given
#Assumptions: None
def testpalcheckerempty():
    print(palchecker("")) #test an empty string-should return true
    print(palchecker(" ")) #test an empty string with a space-should return true

#Purpose:To test the recursive palindrome checker function w/ 1 value only
#Input: None
#Output: The result of each test case
#Assumptions: None    
def testpalcheckerone():
    print(palchecker("a")) # test a single letter word- should return true
    print(palchecker("1")) # test a single number word-should return true
    print(palchecker("-")) #tests a single symbol character- should return true

#Purpose: To test the recursive palindrome checker function w/ many values inside
#Input: None
#Output: The result of each test case
#Assumptions: None
def testpalcheckermany():
    print(palchecker("yeet")) # tests a non palindrome- should return false
    print(palchecker("kayak"))# tests a multi-letter palindrome-should return true
    print(palchecker("a b a")) #tests a multi-letter w/ spaces palindrome-should return true
    print(palchecker("race car")) #tests a multi-word palindrome w/ space in between- should not work-should return false
    print(palchecker("racecar")) #tests multi-word palindrome w/out space- should work- should return true
    print(palchecker(";;--")) #tests a many symbol string- should return false
    print(palchecker(";-;")) #tests a many symbol palindrome- should return true
    print(palchecker("keek")) # tests an even numbered palindrome- should return true

#Purpose: To test all tester functions in a single function
#Input: None
#Output: the result of all the tester functions 
#Assumptions: None
def maintester():
    testpalcheckerempty()
    print("------------------------------------------")
    testpalcheckerone()
    print("------------------------------------------")
    testpalcheckermany()

maintester()


