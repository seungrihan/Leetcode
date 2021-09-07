# LeetCode 724. Find Pivot Index

from typing import List

def pivotIndex(nums: List[int]) -> int:
    total_sum = 0
    
    for num in nums:total_sum += num
    
    right_sum = total_sum
    left_sum = 0
    tmp_num = 0
    
    for idx,num in enumerate(nums):
        
        left_sum += tmp_num
        tmp_num = num
        right_sum -= num

        if left_sum == right_sum:
            return idx         
      
    return -1

print("[1,8,2,9,2,3,6] , pivot idx : ", pivotIndex([1,8,2,9,2,3,6]))