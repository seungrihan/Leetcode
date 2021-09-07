# LeetCode 287 Find the Duplicate Number

from typing import List

def findDuplicate(nums: List[int]):
    hare = nums[0]
    tortoise =nums[0]

    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        if hare == tortoise:
            break
        
    ptr = nums[0]
    
    while ptr != tortoise:
        ptr = nums[ptr]
        tortoise = nums[tortoise]
    
    return ptr

print("answer is : ",findDuplicate([3,1,3,4,2]))