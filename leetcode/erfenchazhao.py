#coding:gbk
##���ֲ��ҵ�ʱ�临�Ӷ���log2n
#α����
# def Binarysearch(max, min, target):
#     while min<=max:
#         mid = (min+max)/2
#         if mid == target:
#             return mid
#         elif mid>target:
#             max = mid-1
#         else:
#             min = mid+1
#     return max


#####����һ�� n ��Ԫ������ģ������������� nums ��һ��Ŀ��ֵ target ��дһ���������� nums �е�target�����Ŀ��ֵ���ڷ����±�
class Solution():
    def find_target(self, nums, target):
        if not nums or nums[-1] < target or nums[0] > target:
            return -1
        min, max = 0, len(nums)
        while min <= max:
            mid = (min+max)//2
            if nums[mid] > target:
                max = mid-1
            if nums[mid] < target:
                min = mid + 1
            if target == nums[mid]:
                return mid
        return -1

#744 Ѱ�ұ�Ŀ����ĸ�����С��ĸ
class Solution():
    def find_nearest_letter(self, letters, target):
        if letters[-1] <= target: return letters[0]

        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[left]
##540
#���������еĵ�һԪ��
class Solution5():
    def find_single_num(self, nums):
        dict = {}
        for i in nums:
            if dict.get(i):
                dict[i] +=1
            else:
                dict[i] = 1
        for i in nums:
            if dict.get(i) == 1:
                return i
ss = Solution5().find_single_num([1,1,2,3,3,4,4,8,8])
print(ss)


