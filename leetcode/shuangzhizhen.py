#coding:gbk

'''
在有序数组中找出两个数，使它们的和为 target。
'''

class Solution1():
    def find_two(self, nums, target):
        r = 0
        l = len(nums)-1
        while r<l:
            sums = nums[r] + nums[l]
            if sums < target:
                r += 1
            elif sums > target:
                l -= 1
            else:
                return [r+1, l+1] #返回的下标值不是从0开始
        return None


##盛最多水的容器
class Solution2():
    def max_area(self, nums):
        r, l = 0, len(nums)-1
        maxarea = 0
        while r < l:
            maxarea = max((min(nums[r], nums[l])*(r-l)), maxarea)
            if nums[r] <= nums[l]:
                r += 1
            else:
                l -= 1
        return maxarea

##搜索二维矩阵
class Solution3():
    def search_matrix(self, matrix, target):
        if not matrix:
            return False
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >-1:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] >target:
                j -= 1
            else:
                return True
        return False

##删除排序数组中的重复项
class Solution4():
    def remove_duplicates(self, nums):
        a = 0
        b = 1
        while b < len(nums):
            if nums[a] == nums[b]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a+1
d = Solution4().remove_duplicates([0,0,1,1, 2,2,2,3, 5])

#移动0
class Solution():
    def movezeros(self, nums):
        j = 0  #慢指针
        for i in range(len(nums)):  #i是快指针
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums


####三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 存储结果列表
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                if nums[j] + nums[k] == -nums[i]:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j+1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list


if __name__ == '__main__':
    s = Solution()
    result_list = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(result_list)


#####四数之和

class Solution:
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

#合并2个有序数组
class Solution6():
    def merge_two_list(self, nums1, nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        l1 = 0
        l2 = 0
        merge_num = []
        while l1 < len(nums1) and l2 <len(nums2):
            if nums1[l1] < nums2[l2]:
                merge_num.append(nums1[l1])
                l1 += 1
            else:
                merge_num.append(nums2[l2])
                l2 += 1
        if l1 < len(nums1):
            merge_num += nums1[l1:]
        if l2 < len(nums2):
            merge_num += nums2[l2:]
        return merge_num

##
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        temp_h = 0
        while l <= r:
            min_h = min(height[l], height[r])
            if min_h > temp_h:
                res += (min_h - temp_h) * (r - l + 1)
                temp_h = min_h
            while l <= r and height[l] <= temp_h:
                l += 1
            while l <= r and height[r] <= temp_h:
                r -= 1
        res -= sum(height)
        return res




#167
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r += 1
        if numbers[l] + numbers[r] == target:
            return [l, r]
        return []

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ##复制
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:

                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

#141

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False




#142
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


#76   s = "ADOBECODEBANC", t = "ABC"
class Solution:
    def minWindow(self, s: str, t: str) -> str:



#633

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        a = 0
        b = math.isqrt(c) + 1
        while a <= b:
            if pow(a, 2) + pow(b, 2) == c:
                return True
            if pow(a, 2) + pow(b, 2) > c:
                b = b - 1
            if pow(a, 2) + pow(b, 2) < c:
                a = a + 1
        return False
#680
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def search(chars, times):  # chars为待筛查的字符串，times表示当前还有几次删除机会
            begin, end = 0, len(chars) - 1
            while begin < end:
                if chars[begin] != chars[end]:  # 若左右指针指向的字符不同，代表 begin end的范围内有需要被删除的点
                    if times == 0:  # 发现了不同，但是却没有可以删除的次数了，那么肯定不能完成题目要求
                        return False
                    # 如果上一步没返回，说明还有可供删除的次数
                    # 选择删除当前left,right闭区间的左边或者右边后，继续搜索对应剩下的部分，看能否完成题目要求
                    # 由于选择删除左边或者右边，这就已经用了一次删除机会，所以递归的时候传入times-1
                    return search(chars[begin:end], times - 1) or search(chars[begin + 1:end + 1], times - 1)
                # 可以把begin end想成夹子的两端，如果不走上面的if分支(也就是说夹子左右两端的元素相同)
                # 那么就把夹子收紧
                begin += 1
                end -= 1
            return True  # 如果能一路顺利走到这，说明传入的chars为回文，那自然返回True就可以了

        return search(s, 1)
#524

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        res = ""
        l1 = 0
        l2 = 0
        for word in d:
            l1 = len(s)
            l2 = len(word)
            if l2 > l1 :
                continue
            if self.judge(word, s):
                if len(word) > res:

                    res = word
        return res

    def judge(self, word, s):
        i = 0
        j = 0
        while i < len(word) and j < len(s):
            if word[i] == word[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(word)
#438
class Solution:
    def findAnagrams(self, s, p):
        '''
        解法1：滑动窗口
        '''
        res = []
        window = {}     # 记录窗口中各个字符数量的字典
        needs = {}      # 记录目标字符串中各个字符数量的字典
        for c in p: needs[c] = needs.get(c, 0) + 1  # 统计目标字符串的信息

        length, limit = len(p), len(s)
        left = right = 0                    # 定理两个指针，分别表示窗口的左、右界限

        while right < limit:
            c = s[right]
            if c not in needs:              # 当遇到不需要的字符时
                window.clear()              # 将之前统计的信息全部放弃
                left = right = right + 1    # 从下一位置开始重新统计
            else:
                window[c] = window.get(c, 0) + 1            # 统计窗口内各种字符出现的次数
                if right-left+1 == length:                  # 当窗口大小与目标字符串长度一致时
                    if window == needs: res.append(left)    # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                                                 # left右移
                    window[s[left]] -= 1                    # 并将移除的字符数量减一
                    left += 1
                right += 1                                  # right右移
        return res

#567
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = {}
        for c in s2:
            needs[c] = needs.get(c, 0) + 1




#239

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


#345
class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        lst = list(s)
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            if lst[l] in dic and lst[r] in dic:
                lst[l], lst[r] = lst[r], lst[l]  #交换
                l = l + 1
                r = r - 1
            elif lst[l] not in dic:
                l = l + 1
            elif lst[r] not in dic:
                r = r - 1

        return ''.join(lst)















