from Node import Node

#This class implements the following methods:
#   add(item)
#   search(item)
#   remove(item)
#   isEmpty()
#   size()
#The other methods in this class must be implemented.

class UnorderedList:
    def __init__(self):
        self.head = None

    #Purpose: add item to front of list
    #Assumptions: none
    #Inputs: self: the UnorderedList object
    #        item: object to be added to list
    #Outputs: updates self.head
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    #Purpose: search for item in list
    #Assumptions: none
    #Inputs: self: the UnorderedList object
    #        item: object being searched for
    #Outputs: returns True when item found;
    #         otherwise returns False.
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
        
    #Purpose: To find the index position of a given object
    #Assumptions: None
    #Input: self: the UnorderedList object
    #       item: object being searched for
    #Output: The index position of the object in question; if object being searched for is not found-will return -1
    def index(self,item):
        current=self.head
        count=0
        found=self.search(item)
        if found== False:
            return -1
        else:
            while current != None:
                if current.getData()==item:
                
                    return count
                else:
                    current=current.getNext()
                count=count+1
    
            
         
    #Purpose: remove item from list
    #Assumptions: None
    #Inputs: self: the UnorderedList object
    #        item: object to be removed
    #Outputs: updates self.head when necessary
    def remove(self,item):
        current = self.head
        found = self.search(item)        
        if current != None and current.getData() == item:
            self.head=current.getNext() # setting head to next node
            current=None #setting current to Null so that it will be deleted
            return found #end and return True

        previous=None        
        while current != None and current.getData() != item:
            previous= current  # moves the head pointer throughout the list if it does not match
            current= current.getNext() # assigns new current node
        if current is None:
            return found  # if the item is not found 
        previous.next=current.getNext() # sets the previous pointer to new next
        current=None
        return found   
    #Purpose: To insert a new node at beginning of list
    #Assumption: None
    #Input: self: the UnorderedList object
    #       item: object being added
    #      
    #Outputs: Updated list of nodes w/ new node added at front of list
    def addFirst(self, item):
        new_node = Node(item)
        new_node.next = self.head #draw line to the current head
        self.head = new_node #assigns the head to the new node and the next node is the previous head    

    #Purpose: To insert a new node at end of list
    #Assumption: None
    #Input: self: the UnorderedList object
    #       item: object being added
    #      
    #Outputs: Updated list of nodes w/ new node added at end of list
    def addLast(self, item):
        new_node = Node(item) #create new node equal to the data entered
        if self.head is None: #there is nothing there
            self.head = new_node #set head to the new node
            return #end
        last_node = self.head
        while last_node.next!= None: #wants the last node in the list
            last_node = last_node.next

        last_node.next = new_node #adds node to the end of the list 



    #Purpose: To insert a new node at a specific position
    #Assumption: None
    #Input: self: the UnorderedList object
    #       item: object being added/inserted
    #       pos: the specific location to place new node
    #Outputs: Updated list of nodes w/ new node added at correct position; if input not valid will return false
    def insert(self,item,pos):
        if pos > self.size() or pos < 0: #input validation
            return False
        
        elif pos ==0: # if pos is first(index 0) use add first method
            self.addFirst(item)
            
        elif pos==self.size(): #if pos is last(index size) use add last method
            self.addLast(item)

        else:
            currnode=self.head #assigning current node to head
            current=0 # creating counter
            while current!= pos: # while condition is not satisfied(pos!= current)
                previous=currnode # saves head position(from above) as previous
                currnode=currnode.getNext() # updates current node to next node
                current=current+1 # updates counter 
                
            NewNode=Node(item) # creates new node to be added
            NewNode.next=previous.next # New Nodes next pointer points to previous Node's next
            previous.next=NewNode # set the "next" of the previous node to the new Node


    def isEmpty(self):
        return self.head == None

    #Purpose: determine size of list
    #Assumptions: none
    #Inputs: self: the UnorderedList object
    #Outputs: returns integer representing size of list
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def __str__(self):
        result = ""
        current = self.head
        while current != None:
            if len(result) > 0:
                result = result + ","
            result = result + str(current.getData())
            current = current.getNext()

        return "UnorderedList:" + result


#Purpose: To test the remove method with all relevant scenarios
#Assumptions:None
#Input:None
#Output: The result of each test along with numerous print statements to affirm the success of the tests
def testremove():
    u=UnorderedList()#test list to see if empty
    print(u.isEmpty())
    print(u.remove("cheese"))#try and remove something from an empty list(should result in a "False')
    u.add("cat")
    print(u)
    u.remove("cat") #remove an item from list w/ one object
    print(u)
    u.add("cat")
    u.add("dog")
    u.add("yeet")
    u.add("hello")
    u.add("world")
    print(u)
    u.remove("world")#remove something from beginning,middle,and end of list
    u.remove("cat")
    u.remove("yeet")
    print(u)
    u.remove("hello") #remove something from a list w/ only 2 values
    print(u)


#Purpose: To test the index method with all relevant scenarios
#Assumptions:None
#Input:None
#Output:The result of each test along with numerous print statements to affirm the success of the tests
def testindex():
    w=UnorderedList()#test list to see if empty
    print(w.isEmpty())
    w.add("cat")
    w.add("dog")
    w.add("monkey")
    w.add("YUP")
    w.add("nope")
    print(w.index("HIYA"))#test index something not in list
    print(w.index("nope")) #test index of first value
    print(w.index("cat")) #test index of last value
    print(w.index("monkey")) #test index of middle value
    w.add("monkey")#adding duplicate for test
    print(w.index("monkey"))#test index for duplicate value
    print(w)

#Purpose:To test the insert function witn all relevant scenarios
#Assumptions:None
#Input:None
#Output:The result of each test along with numerous print statements to affirm the success of the tests
def testinsert():
    q=UnorderedList()
    print(q.isEmpty())#test list to see if empty
    q.add("one")
    q.add("two")
    q.add("three")
    q.add("four")
    q.add("five")
    print(q.insert("six",-1))#test for inserting a too low an index position
    print(q.insert("six",7))#test for inserting a too high an index position
    q.insert("six",0) #test for inserting an object right at beginning of list
    print(q)
    q.insert("seven",3) #test for inserting an object in middle of list
    print(q)
    q.insert("eight",7) #test for inserting an object at the very end of the list
    print(q)
    q.insert("eight",7) #test for inserting a duplicate
    print(q)

    
#Purpose:To test all the tester functions in a single function for cleanliness of code etc
#Assumptions:None
#Input:None
#Output:The results of all the tester functions put together, separated by dashes for cleanliness
def maintester():
    testremove()
    print("-------------------------------------------------------------------------")
    testindex()
    print("-------------------------------------------------------------------------")
    testinsert()
