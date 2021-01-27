#coding:gbk

#####ʢˮ��������
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        num = 0
        while i < j:
            num = max((min(height[i], height[j]) * (j - i)), num)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return num
#######������ά����ÿ������ÿ������
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j > -1:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False
#####����֮�ͣ�������������
class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return l+1, r+1
#ɾ�����������е��ظ���
class Solution2:
    def removeDuplicates(self, nums):
        a = 0
        b = 1
        while b < len(nums):
            if nums[a] == nums[b]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a+1
f = Solution2().removeDuplicates([1,1,2])
print(f)

##�ƶ�0
#ѭ��һ��
class Solution:
    def moveZeroes(self, nums) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums