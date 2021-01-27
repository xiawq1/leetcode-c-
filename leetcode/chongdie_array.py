#coding:gbk
'''
����һ������ļ��ϣ���ϲ������ص������䡣


����
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # ����б�Ϊ�գ����ߵ�ǰ��������һ���䲻�غϣ�ֱ�����
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # ����Ļ������ǾͿ�������һ������кϲ�
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
