# Modified author's code:
#   - this heap assumes the keys are integers
#Why O(nlogn) for sorter?--> B/C building the heap itself is O(n)- Sorting the heap is the O(logn) time performance,
#as it needs to iterate throught the heap to find the minimum value. It needs to iterate throught the heap to remove n objects,
#thus resulting in the sorting part being O(logn) time. O(n)+O(logn)== O(nlogn)


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        #make sure all parent keys are <= their child keys
        while (i > 0):
            print(self.heapList, i)
            self.percDown(i)
            i = i - 1
        print(self.heapList,i)

    def percDown(self,i):
        #move key at [i] down heapList to maintain heap order property
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
                
    def minChild(self,i):
        #return index location where smaller child key is located
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percUp(self,i):
        #move key at [i] up heapList to maintain heap order property
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
               tmp = self.heapList[i // 2]
               self.heapList[i // 2] = self.heapList[i]
               self.heapList[i] = tmp
            i = i // 2
 
    def insert(self,k):
        #Add k to end of heapList
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        #Move k up the heapList to maintain heap order property
        self.percUp(self.currentSize)

    def delMin(self):
        #remove and return item at front of heapList
        retval = self.heapList[1]
        #copy item at end of heapList to front of heapList
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        #remove item at end of heapList
        self.heapList.pop()
        #move item at front down heapList to maintain heap order property
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

#Purpose:To sort a heap in O(nlogn) time
#Input: A list of integers
#Output: The newly built heap, as well as the heap sorted
#Assumptions: The list will contain integers
def heapSortyup(alist):
    bh=BinHeap() #Assign the class
    bh.buildHeap(alist) #Build the heap out of the list given
    i=len(alist) #Check the length of the list
    while (i > 0) : #Set the while statement to terminate when the length of the list is empty
        print(bh.delMin()) #Display the minimum value each time the heap is iterated through
        i =i - 1 #Iterate down 1 each time throught the loop


#Purpose:To test our new heap sorter function
#Input: None
#Output: The result of the tests
#Assumptions: None
def testnewsorter():
    alist=[] #Assign the list variable to an empty list
    heapSortyup(alist) #Test the function w/ the empty list
    print("-------------------------------")
    alist=[1] #Re-assign the list variable to a list with one integer only
    heapSortyup(alist) #Test the function w/ the list containing only a single integer
    print("-------------------------------")
    alist=[7,8,3,2,9,10] #Re-assign the list variable to a list with many integers
    heapSortyup(alist) #Test the function w/ the large list
    print("-------------------------------")
    alist=[1,2,3,4,5,6] #Re-assign the list variable to a list which is in order
    heapSortyup(alist) #Run the function w/ the large list which is in order

testnewsorter()




