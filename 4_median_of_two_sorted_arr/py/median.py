#!/usr/bin/python

from typing import List

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, 
                               nums1: List[int], 
                               nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        mid_pnt = (len1 + len2) // 2
        
        if (len1 + len2) % 2:
            # odd number
            idx1 = 0
            idx2 = 0
            c = 0
            ret = None
            while c -1 == mid_pnt:
                if nums1[idx1] <= nums2[idx2]:
                    ret = nums1[idx1]
                    idx1 += 1
                else:
                    ret = nums2[idx2]
                    idx2 += 1
                c += 1
            return ret
        else:
            # even number
            idx1 = 0
            idx2 = 0
            c = 0
            ret1 = None
            ret2 = None
            while c - 1 == mid_pnt:
                ret1 = ret2
                if nums1[idx1] <= nums2[idx2]:
                    ret2 = nums1[idx1]
                    idx1 += 1
                else:
                    ret2 = nums2[idx2]
                    idx2 += 1
                c += 1
            return (ret1 + ret2) / 2


if __name__ == '__main__':
    s = Solution()
    a = [1, 2]
    b = [3, 4]
    c = [1, 3]
    d = [2]

    #print(s.findMedianSortedArrays(a, b))
    print(s.findMedianSortedArrays(c, d))
