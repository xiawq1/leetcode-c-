#coding:gbk
'''
����һ���������� nums ���ҵ�һ���������͵����������飨���������ٰ���һ��Ԫ�أ�������������
'''


#########̰���㷨
class Solution:
    def maxsubarray(self, nums):
        length = len(nums)
        au = nums[0]  #��ǰ�ĺ�
        temp_result = nums[0]  #֮ǰ�ĺ�
        for index in range(1, length):
            au = max(nums[index], au+nums[index])  ###����֮ǰ����
            temp_result = max(au, temp_result)
        result = temp_result
        return result
result = Solution().maxsubarray([-2,1,-3,4,-1,2,1,-5,4])
#[-2,1,-3,4,-1,2,1,-5,4]

##��̬�滮��
class Solution2:
    def maxsub2(self, nums):
        n = len(nums)
        for i in range(1, n):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)
Solution2().maxsub2([-2,1,-3,4,-1,2,1,-5,4])