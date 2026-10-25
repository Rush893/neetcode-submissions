import math
from collections import Counter, defaultdict
class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        indicator = False
        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet:
                indicator = True
            else:
                numSet.add(nums[i])
        return indicator
        
        