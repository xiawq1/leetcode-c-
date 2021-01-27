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

#452  排序加贪心算法
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

#763贪心算法加双指针
class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        # 先确定思路：看见开头一个字母，就要看这个字母最后出现在哪，然后康康这个开头和结尾之间的那些其他字母是不是都落在这个区间里，
        # 如果不是，则扩充区间，如果是，那就最好了ww。
        # 另一点是确定用什么方法，很多题你不看参考答案真的想不出来要走哪条路，倒不是说这条路有多难，而是不能确定到底应该往哪个方向去想。
        # 对于这道题，一个关键点是利用字典key的唯一性来记载一个字母最大的index是几。
        # 然后，遍历字符串并跟它比较，用max函数来康康是边界大还是当前遍历的这个字母的最大index大，
        # 如果当前遍历字母的最大index大，那就说明超过了边界，那就要更新边界，大概就是这个思路。
        # 结合我说的，康康下面的代码哈。

        max_index = {item: idx for idx, item in enumerate(S)}  # 这样写就是一个键：一个值，然后通过遍历来更新到最大的那个index
        start, end = 0, 0  # 起始边界， 结束边界
        ans = []

        for idx, i in enumerate(S):
            end = max(end, max_index[i])  # 这里就是用边界和当前遍历到的那个字母的最大index去比较，看看谁大，
            # 如果最大index大就扩充边界。
            if idx == end:  # 最后，遍历的位置和边界重合了，那就ok了，从这里截断并记录长度。 就这些，可以再慢慢理解下。
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






