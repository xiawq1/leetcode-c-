#coding:gbk
#135
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1]*len(ratings)

        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        i = len(ratings) - 1
        while i > 0:
            if ratings[i] < ratings[i-1]:
                res[i-1] = max(res[i] + 1, res[i-1])
            i -= 1

        sum = 0
        for i in res:
            sum += i
        return sum


#435
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]

        return n - ans

#452
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:


#455
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(s) and cookie < len(g):
            if s[child] <= g[cookie]:
                child += 1
                cookie += 1
            else:
                cookie += 1
        return child
#605  ???
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                prev = i

        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2

        return count >= n

#452  �����̰���㷨
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1

        return ans

#763̰���㷨��˫ָ��
class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        # ��ȷ��˼·��������ͷһ����ĸ����Ҫ�������ĸ���������ģ�Ȼ�󿵿������ͷ�ͽ�β֮�����Щ������ĸ�ǲ��Ƕ�������������
        # ������ǣ����������䣬����ǣ��Ǿ������ww��
        # ��һ����ȷ����ʲô�������ܶ����㲻���ο�������벻����Ҫ������·��������˵����·�ж��ѣ����ǲ���ȷ������Ӧ�����ĸ�����ȥ�롣
        # ��������⣬һ���ؼ����������ֵ�key��Ψһ��������һ����ĸ����index�Ǽ���
        # Ȼ�󣬱����ַ����������Ƚϣ���max�����������Ǳ߽���ǵ�ǰ�����������ĸ�����index��
        # �����ǰ������ĸ�����index���Ǿ�˵�������˱߽磬�Ǿ�Ҫ���±߽磬��ž������˼·��
        # �����˵�ģ���������Ĵ������

        max_index = {item: idx for idx, item in enumerate(S)}  # ����д����һ������һ��ֵ��Ȼ��ͨ�����������µ������Ǹ�index
        start, end = 0, 0  # ��ʼ�߽磬 �����߽�
        ans = []

        for idx, i in enumerate(S):
            end = max(end, max_index[i])  # ��������ñ߽�͵�ǰ���������Ǹ���ĸ�����indexȥ�Ƚϣ�����˭��
            # ������index�������߽硣
            if idx == end:  # ��󣬱�����λ�úͱ߽��غ��ˣ��Ǿ�ok�ˣ�������ضϲ���¼���ȡ� ����Щ����������������¡�
                ans.append(end - start + 1)
                start = idx + 1

        return ans


#122
class Solution:
    def maxProfit(self, prices: List[int]) -> int:




#406   ???
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans



#665

#[3,4,2,3]      [4,2,3]
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i+2 < len(nums) and i-1>= 0:
                    if nums[i+2] < nums[i] and nums[i-1] > nums[i+1]:
                        return False
            if count > 1:
                return False
        return True






