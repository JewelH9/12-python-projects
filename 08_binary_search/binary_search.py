# implementation of binary search algorithm

#we will prove that binary search is faster than linear search by comparing the number of comparisons made by both algorithms

#naive linear search algorithm
#if yes, return the index of the element
#if no, return -1
from random import random
import time


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
  

#binary search algorithm uses divide and conquer approach
#we will leverage the fact that the array is sorted to eliminate half of the search space at each step
def binary_search(arr, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    midpoint = low + (high - low) // 2

    if arr[midpoint] == target:
        return midpoint
    elif target < arr[midpoint]:
        return binary_search(arr, target, low, midpoint - 1)
    else:
        return binary_search(arr, target, midpoint + 1, high)
      
if __name__ == "__main__":  #__name__ is a special variable in Python that is set to "__main__" when the script is run directly, and to the name of the module when it is imported. This allows us to write code that will only be executed when the script is run directly, and not when it is imported as a module.
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # target = 5

    # print("Linear Search:")
    # index = linear_search(arr, target)
    # if index != -1:
    #     print(f"Element {target} found at index {index}")
    # else:
    #     print(f"Element {target} not found in the array")

    # print("\nBinary Search:")
    # index = binary_search(arr, target)
    # if index != -1:
    #     print(f"Element {target} found at index {index}")
    # else:
    #     print(f"Element {target} not found in the array")
    
    #now we will vompare time taken by both algorithms for a large array
    length = 10000
    sorted_arr = set(range(length))  #create a sorted array of length 10000
    while len(sorted_arr) < length:
        sorted_arr.add(random.randint(0, length * 2))  #add random elements to the set until it reaches the desired length
    
    sorted_arr = sorted(list(sorted_arr))  #convert the set to a list and sort it
    
    start_time = time.time()
    for target in sorted_arr:
        linear_search(sorted_arr, target)
        
    end_time = time.time()
    print("Time taken by linear search:", (end_time - start_time)/length ,"seconds")
    
    start_time = time.time()
    for target in sorted_arr:
        binary_search(sorted_arr, target)
    end_time = time.time()
    print("Time taken by binary search:", (end_time - start_time)/length ,"seconds")