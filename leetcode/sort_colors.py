#coding:gbk

'''
����һ��������ɫ����ɫ����ɫ��һ�� n ��Ԫ�ص����飬ԭ�ض����ǽ�������ʹ����ͬ��ɫ��Ԫ�����ڣ������պ�ɫ����ɫ����ɫ˳�����С�

˫ָ��   ʹ������ָ��ֱ��������� 00 �� 11��
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