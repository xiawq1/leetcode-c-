#coding:gbk
'''
���ֲ���
�ж�����ҿ����� = [left, mid, right)

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

###35����һ�����������һ��Ŀ��ֵ�����������ҵ�Ŀ��ֵ�������������������Ŀ��ֵ�������������У����������ᱻ��˳������λ�á�
#��һ�������������ҵ�һ�����ڵ��� target ���±���ֲ��������ʱ�临�Ӷ�Ϊ O ( logn)
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

#69 �󿪷�
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
