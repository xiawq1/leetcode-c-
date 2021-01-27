#coding:gbk
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
'''


#########贪心算法
class Solution:
    def maxsubarray(self, nums):
        length = len(nums)
        au = nums[0]  #当前的和
        temp_result = nums[0]  #之前的和
        for index in range(1, length):
            au = max(nums[index], au+nums[index])  ###舍弃之前的数
            temp_result = max(au, temp_result)
        result = temp_result
        return result
result = Solution().maxsubarray([-2,1,-3,4,-1,2,1,-5,4])
#[-2,1,-3,4,-1,2,1,-5,4]

##动态规划法
class Solution2:
    def maxsub2(self, nums):
        n = len(nums)
        for i in range(1, n):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)
Solution2().maxsub2([-2,1,-3,4,-1,2,1,-5,4])