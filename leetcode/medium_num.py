'''
合并两个有序数组，二分查找，时间复杂度为O(log(m+n))
根据中位数的定义，当 m+n 是奇数时，中位数是两个有序数组中的第 (m+n)/2个元素，当 m+n 是偶数时，
中位数是两个有序数组中的第 (m+n)/2个元素和第 (m+n)/2+1个元素的平均值。这道题可以转化成寻找两个有序数组中的第 k小的数,
k为(m+n)/2或 (m+n)/2+1。
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2
Solution().findMedianSortedArrays([1,3], [2])

