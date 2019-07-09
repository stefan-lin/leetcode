#!/usr/bin/python

from typing import List

"""
The definition of median is:
    1) when the size of a list is odd, the (size/2 + 1)th element is median
    2) when the size of a list is even, the average of the (size/2)th and
       the (size/2 + 1)th elements is median

Assume the size of the two sorted array are m and n.
The median should be ((m+n)/2 + 1)th element when m + n is odd; if the 
length of combined two arrays is even, which means m + n is even, the median 
would be the average of ((m+n)/ 2)th and ((m+n)/2 + 1)th elements

e.g.
    nums1 = [1, 2] and nums2 = [3, 4] => median is (2+3) / 2 = 2.5
    nums1 = [1, 3] and nums2 = [2]    => median is 2

In this question, we are looking for K = (m+n)/2 or both K and K+1 depending 
on odd size or even size of combined array. The purpose of K is that we are
partitioning BOTH arrays into two groups which the first half has less than
or equal to the number of elements in the second half (usually one off or 
the same)

e.g. 
    A = [2, 3, 5, 8]         # len(A) = 4
    B = [1, 4, 6, 9, 11]     # len(B) = 5
    K = (4 + 5) / 2 = 4
    partition_a = K / 2 = 2
    partition_b = K - partition_a = 4 - 2 = 2
    Thus, the two groups would look like:
        group_1 = [2, 3, 1, 4] = [1, 2, 3, 4]
        group_2 = [5, 8, 6, 9, 11] = [5, 6, 8, 9, 11]
        # note: all elements in group_1 is less than smallest element(5) in group_2
"""

class Solution(object):
    def findMedianSortedArrays(self,
                               nums1: List[int],
                               nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if (len1 + len2) % 2:
            # odd case
            return self._find_median(nums1, nums2, (len1 + len2) // 2 + 1) 
        else:
            # even case
            return (self._find_median(nums1, nums2, (len1 + len2) // 2) +
                    self._find_median(nums1, nums2, (len1 + len2) // 2 + 1)
                    ) / 2

    def _find_median(self, 
                     nums1_: List[int], 
                     nums2_: List[int], 
                     k: int) -> float:
        len1_ = len(nums1_)
        len2_ = len(nums2_)

        if len1_ > len2_:
            return self._find_median(nums2_, nums1_, k)
        else:
            if not len1_:
                return nums2_[k-1]
            if k == 1:
                return min(nums1_[0], nums2_[0])

            pivot1 = min(k // 2, len1_)
            pivot2 = k - pivot1

            if nums1_[pivot1 - 1] <= nums2_[pivot2 - 1]:
                return self._find_median(nums1_[pivot1:], nums2_, k-pivot1)
            else:
                return self._find_median(nums1_, nums2_[pivot2:], k-pivot2)

if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 8, 10, 12, 14, 16, 18]
    c = [1, 2]
    d = [3, 4]
    e = [1, 3]
    f = [2]

    s = Solution()

    print(s.findMedianSortedArrays(b, a))
    print(s.findMedianSortedArrays(c, d))
    print(s.findMedianSortedArrays(e, f))

