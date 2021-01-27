#coding:gbk

#��������ջ�����������ź�������ƥ�䣬�������ų�ջ������ж�ջ�Ƿ�Ϊ�գ�Ϊ��ΪTrue������ΪFalse.
class Solution:
    def isValid(self, s):
        stack = [] #���ڴ�ſ�����
        mapping = {')':'(', '}':'{', ']':'['} #ɢ�б�����ƥ������
        for char in s:
            if char in mapping:
                if len(stack) != 0:
                    tmp = stack.pop()
                    if mapping[char] != tmp:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return not stack
Solution().isValid("([)]")

#42

class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        hei_len = len(height)
        left = 0
        right = hei_len - 1
        max_left = height[0]
        max_right = height[-1]
        res = 0
        while left < right:
            if height[left] < height[right]: #ע������������������ߵ����ұ�ʱ������߿�ʼ��������ߴ����ұ�ʱ�����ұ߿�ʼ��������Զ����ϵ�һ�࣡
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1 #�������������
            else:
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1
        return res
Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])

#ջ��Ӧ��https://leetcode-cn.com/problems/trapping-rain-water/solution/dan-diao-zhan-jie-fa-fu-xiang-xi-jie-ti-kmyyl/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        stack = [] ######��¼����

        sum = 0
        for i in range(0, len(height)):
            while stack and height[i] > height[stack[-1]]:
                temp = height[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1  #���
                    h = min(height[i], height[stack[-1]])-temp
                    sum += w*h
            stack.append(i)
        return sum



#496
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        dic = {}
        for i in nums2:
            while stack and stack[-1] < i:
                dic[stack.pop()] = i
            stack.append(i)
        return [dic.get(i, -1) for i in nums1]
Solution().nextGreaterElement([4,1,2], [1,3,4,2])

#503
class Solution:
    def nextGreaterElements(self, nums):
        nums1 = nums + nums
        res = [-1] * len(nums1) #�����ſ��Խ���res[stack.pop()] = nums1[i]����
        # tar = nums[0]
        stack = []
        for i in range(len(nums1)):
            while stack and nums1[stack[-1]] < nums1[i]:
                res[stack.pop()] = nums1[i]
            stack.append(i)
        return res[:len(nums)]
#739
class Solution:
    def dailyTemperatures(self, T):
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res

#901
class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

#84
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        left, right = [0] * n, [0] * n
        ## ���������ұ��

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
Solution().largestRectangleArea([2,1,5,6,2,3])

#71
class Solution:
    def simplifyPath(self, path):
        stack = []
        path = path.split("/")
        for item in path:
            if item == "..":
                if stack : stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)
Solution().simplifyPath("/a/./b/../../c/")

