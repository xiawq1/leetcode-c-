#coding:gbk
'''
二分查找
判断左闭右开区间 = [left, mid, right)

def binary_search(left, right):
    while left < right:
        mid = left + (right - l) // 2
        if isResult(mid):  return mid
        if judge(mid):
            right = mid    # next range = [l, m)
        else:
            left = mid + 1    # next range = [m+1, r)
    return left

'''

###35给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#在一个有序数组中找第一个大于等于 target 的下标二分查找所需的时间复杂度为 O ( logn)
class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        if target > nums[-1]:
            return n
        left, right = 0, n-1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans

#69 求开方
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                return mid
        return right
