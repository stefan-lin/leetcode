#!/usr/bin/python

"""
Given a string, find the length of the longest substring 
without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, 
             "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str)-> int:
        longest_ = 0
        idx = 0

        while idx < len(s):
            mset = set(s[idx])
            
            for c in s[idx+1:]:
                if c not in mset:
                    print(len(mset))
                    mset.add(c)
                else:
                    print('------')
                    print(len(mset))
                    print('------')
                    longest_ = max(longest_, len(mset))
            idx += 1
        return longest_



