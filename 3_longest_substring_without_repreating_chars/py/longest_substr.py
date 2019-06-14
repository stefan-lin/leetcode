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
                #print('current iteration = {}'.format(c))
                if c not in mset:
                    #print('size of set = ', end='')
                    #print(len(mset))
                    mset.add(c)
                else:
                    #print('{} is fount in set; b4 longest_ = {:d}'.format(c, longest_))
                    longest_ = max(longest_, len(mset))
                    #print('after longest_ = {:d}'.format(longest_))
                    break
                #print('---another for iteration---')
            idx += 1
            #print()
        return longest_


    def test(self):
        inputs = ['abcabcbb', 'bbbbb', 'pwwkew']
        
        # run tests
        for i in inputs:
            print(self.lengthOfLongestSubstring(i))


if __name__ == '__main__':
    s = Solution()
    s.test()
