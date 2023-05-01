import random
#import math
import time

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    
    return -1

#print(naive_search([1,5,18,5,12,29], 12))


def bin_search(list, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(list)-1

    if high < low:
        return -1

    midpoint = (low+high)//2
    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return bin_search(list, target, low, midpoint-1)
    else:
        return bin_search(list, target, midpoint+1, high)

if __name__ == "__main__":
    # list = [2,5,6,90,45,3]
    # target_list = 45
    # print(naive_search(list, target_list))
    # print(bin_search(list, target_list))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search took: " ,(end-start)/length,  " seconds")

    start2 = time.time()
    for target in sorted_list:
        bin_search(sorted_list,target)
    end2 = time.time()
    print("Binary search took: " ,(end2-start2)/length, " seconds")
    
    
    