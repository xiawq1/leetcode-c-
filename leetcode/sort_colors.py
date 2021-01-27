#coding:gbk

'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

双指针   使用两个指针分别用来交换 00 和 11。
'''

class Solution:
    def sortColors(self, nums):
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
Solution().sortColors([2,0,2,1,1,0])
unk_token = "<unk>"
pad_token = "<pad>"
extra_tokens = [pad_token, unk_token]
pad = extra_tokens.index(pad_token)
print(pad)