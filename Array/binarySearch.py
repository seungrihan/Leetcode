# LeetCode 704. Binary Search

from typing import List

def binarySearch(nums: List[int], target):

    left = 0
    right = len(nums)-1

    while left <= right:
        pivot = int((left+right)/2)
        
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            left = pivot+1
        else:
            right = pivot-1
            
    return -1

print("answer is : ",binarySearch(nums=[1,0,3,5,9,12], target=9))