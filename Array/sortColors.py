# LeetCode 75. Sort Colors

from typing import List

def sortColors(nums: List[int]):

    left = 0
    right = len(nums) - 1
    i = 0

    while i < right :
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1

        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1

        else :
            i += 1

    return nums
    
print("answer is : ",sortColors(nums=[1,0,2,2,0,1,2,1,0]))       