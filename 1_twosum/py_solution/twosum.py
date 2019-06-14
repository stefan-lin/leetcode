#!/usr/bin/python

from typing import List

"""
Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, and you 
may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            O(n) solution
        """
        map_     = {}
        idx      = 0
        
        for v in nums:
            if target - v in map_.keys():
                return [map_[target -v], idx]
            map_[v] = idx
            idx += 1
        return [-1, -1]
    # End twoSum
