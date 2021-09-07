# LeetCode 283. Move Zeroes

from typing import List

def moveZereos(nums: List[int]) -> List:
    wIdx = 0
    idx = 0

    for idx in range(len(nums)):
        if nums[idx] != 0:
            nums[wIdx], nums[idx] = nums[idx], nums[wIdx]
            wIdx += 1

    return nums

print("answer is : ", moveZereos(nums=[0,5,0,7,6,3]))