def binary_search(alist, low, high, item):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if alist[mid] == item:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif alist[mid] > item:
            return binary_search(alist, low, mid - 1, item)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(alist, mid + 1, high, item)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
alist = [ 2, 3, 4, 10, 40 ]
item = 10
# Function call
result = binary_search(alist, 0, len(alist)-1, item)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
