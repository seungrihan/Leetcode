# LeetCode 162. Find Peak Element

from typing import List

def findPeakElem(nums: List[int]) -> int:

    left = 0
    right = len(nums) - 1

    if len(nums) <= 1:
        return
    
    while left < right:
        pivot = int((left+right)/2)
        num = nums[pivot]
        nextNum =nums[pivot+1]

        if num < nextNum:
            left = pivot+1
        else:
            right = pivot
    
    return left

print("answer is : ", findPeakElem(nums=[1,3,2,4,5,6,7,8]))