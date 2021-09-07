# LeetCode 1. two Sum

from typing import List

def twoSum(nums: List[int], target):

    nums.sort() #1,3,4,7,8

    left = 0
    right = len(nums)-1

    while left != right:
        sum = int(nums[left]+nums[right])

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left+1,right+1]

print("answer is : ",twoSum(nums=[1,3,7,4,8], target=7))