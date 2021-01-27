#coding:gbk
##二分查找的时间复杂度是log2n
#伪代码
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


#####给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的target，如果目标值存在返回下标
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

#744 寻找比目标字母大的最小字母
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
#有序数组中的单一元素
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


