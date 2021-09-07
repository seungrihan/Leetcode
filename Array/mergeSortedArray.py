# LeetCode 88. Merge Sorted Array

from typing import List

def merge(nums1: List[int], m, nums2: List[int], n):
    num1Idx = m-1
    num2Idx = n-1
    wIdx = len(nums1)-1

    if num2Idx < 0:
        return 

    while 0 <= num1Idx and 0 <= num2Idx:
        num1 = nums1[num1Idx]
        num2 = nums2[num2Idx]
        if num2 <= num1:
            num = num1
            nums1[wIdx] = num
            num1Idx -= 1
            wIdx -= 1
        
        else:
            num = num2
            nums1[wIdx] = num
            num2Idx -= 1
            wIdx -= 1
    
    while 0 <= num2Idx:
        nums1[wIdx] = nums2[num2Idx]
        num2Idx -= 1
        wIdx -= 1
    
    return nums1

print("answer is :",merge(nums1=[1,2,3,0,0,0], m=3 , nums2=[2,5,6], n=3))