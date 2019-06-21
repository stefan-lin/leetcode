from typing import List

class Solution(object):
    def find_median(self, nums1: List[int], nums2: List[int]) -> float:
        # first find the length of both list inputs
        len1 = len(nums1)
        len2 = len(nums2)
        mp = (len1 + len2) // 2

        idx1 = 0
        idx2 = 0
        ret1 = 0
        ret2 = 0

        if (len1 + len2) % 2:
            # odd
            while mp != -1:
                if nums1[idx1] <= nums2[idx2]:
                    ret2 = nums1[idx1]
                    idx1 += 1
                else:
                    ret2 = nums2[idx2]
                    idx2 += 1
                mp -= 1
            return ret2
        else:
            # even
            while mp != -1:
                ret1 = ret2
                if nums1[idx1] <= nums2[idx2]:
                    ret2 = nums1[idx1]
                    idx1 += 1
                else:
                    ret2 = nums2[idx2]
                    idx2 += 1
                mp -= 1
            return (ret1 + ret2) / 2

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = [9]
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d = [2, 4, 6]

    s = Solution()
    print(s.find_median(a, b))
    print(s.find_median(c, d))
