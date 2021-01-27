
#coding:gbk
'''
����һ�����ص��� ������������ʼ�˵�����������б�

���б��в���һ���µ����䣬����Ҫȷ���б��е�������Ȼ�����Ҳ��ص�������б�Ҫ�Ļ������Ժϲ����䣩��
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # �ڲ���������Ҳ����޽���
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # �ڲ��������������޽���
                ans.append([li, ri])
            else:
                # ����������н������������ǵĲ���
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])
        return ans
