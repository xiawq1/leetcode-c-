#coding:gbk
'''
����һ���Ǹ��������飬�����λ������ĵ�һ��λ�á�

�����е�ÿ��Ԫ�ش������ڸ�λ�ÿ�����Ծ����󳤶ȡ�

�ж����Ƿ��ܹ��������һ��λ�á�
����: [2,3,1,1,4]
���: true
����: ���ǿ������� 1 ������λ�� 0 ���� λ�� 1, Ȼ���ٴ�λ�� 1 �� 3 ���������һ��λ�á�
̰���㷨
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
