# LeetCode 56. Merge Intervals

from typing import List

def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    answer = []
    for ans in sorted(intervals, key = lambda i:i[0]):
        if answer and ans[0] <= answer[-1][1]:
            answer[-1][1] = max(ans[1],answer[-1][1])
        else:
            answer.append(ans)
    return answer

print("answer is :", mergeIntervals(intervals=[[1,3],[2,6],[10,15],[8,16]]))