
#coding:gbk

'''
����һ������ n ������������?nums���ж�?nums?���Ƿ��������Ԫ�� a��b��c ��ʹ��?a + b + c = 0 �������ҳ��������������Ҳ��ظ�����Ԫ�顣

'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # ö�� a
        for first in range(n):
            # ��Ҫ����һ��ö�ٵ�������ͬ
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c ��Ӧ��ָ���ʼָ����������Ҷ�
            third = n - 1
            target = -nums[first]
            # ö�� b
            for second in range(first + 1, n):
                # ��Ҫ����һ��ö�ٵ�������ͬ
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # ��Ҫ��֤ b ��ָ���� c ��ָ������
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # ���ָ���غϣ����� b ����������
                # �Ͳ��������� a+b+c=0 ���� b<c �� c �ˣ������˳�ѭ��
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

