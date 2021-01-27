#coding:gbk

'''
�������������ҳ���������ʹ���ǵĺ�Ϊ target��
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
                return [r+1, l+1] #���ص��±�ֵ���Ǵ�0��ʼ
        return None


##ʢ���ˮ������
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

##������ά����
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

##ɾ�����������е��ظ���
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

#�ƶ�0
class Solution():
    def movezeros(self, nums):
        j = 0  #��ָ��
        for i in range(len(nums)):  #i�ǿ�ָ��
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums


####����֮��
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # �洢����б�
        res_list = []
        # ��nums�б���������޷���ֵ������ֱ�Ӹı�nums˳��
        nums.sort()
        for i in range(len(nums)):
            # ���������һ����������0��������ѭ������������Ϊ0������֮��
            if nums[i] > 0:
                break
            # ������������������ȣ���������ǰѭ��������һ��ѭ������ͬ����ֻ��Ҫ����һ��
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # ��¼i����һ��λ��
            j = i + 1
            # ���һ��Ԫ�ص�λ��
            k = len(nums) - 1
            while j < k:
                # �ж�����֮���Ƿ�Ϊ0
                if nums[j] + nums[k] == -nums[i]:
                    # �ѽ������������
                    res_list.append([nums[i], nums[j], nums[k]])
                    # �ж�j����Ԫ���Ƿ���ȣ��еĻ��������
                    while j < k and nums[j] == nums[j+1]: j += 1
                    # �жϺ���k������Ԫ���Ƿ���ȣ��ǵĻ�����
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    # û�������j+1��k-1����С��Χ
                    j += 1
                    k -= 1
                # С��-nums[i]�Ļ���������ȡ
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list


if __name__ == '__main__':
    s = Solution()
    result_list = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(result_list)


#####����֮��

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

#�ϲ�2����������
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
        ##����
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
        def search(chars, times):  # charsΪ��ɸ����ַ�����times��ʾ��ǰ���м���ɾ������
            begin, end = 0, len(chars) - 1
            while begin < end:
                if chars[begin] != chars[end]:  # ������ָ��ָ����ַ���ͬ������ begin end�ķ�Χ������Ҫ��ɾ���ĵ�
                    if times == 0:  # �����˲�ͬ������ȴû�п���ɾ���Ĵ����ˣ���ô�϶����������ĿҪ��
                        return False
                    # �����һ��û���أ�˵�����пɹ�ɾ���Ĵ���
                    # ѡ��ɾ����ǰleft,right���������߻����ұߺ󣬼���������Ӧʣ�µĲ��֣����ܷ������ĿҪ��
                    # ����ѡ��ɾ����߻����ұߣ�����Ѿ�����һ��ɾ�����ᣬ���Եݹ��ʱ����times-1
                    return search(chars[begin:end], times - 1) or search(chars[begin + 1:end + 1], times - 1)
                # ���԰�begin end��ɼ��ӵ����ˣ�������������if��֧(Ҳ����˵�����������˵�Ԫ����ͬ)
                # ��ô�ͰѼ����ս�
                begin += 1
                end -= 1
            return True  # �����һ·˳���ߵ��⣬˵�������charsΪ���ģ�����Ȼ����True�Ϳ�����

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
        �ⷨ1����������
        '''
        res = []
        window = {}     # ��¼�����и����ַ��������ֵ�
        needs = {}      # ��¼Ŀ���ַ����и����ַ��������ֵ�
        for c in p: needs[c] = needs.get(c, 0) + 1  # ͳ��Ŀ���ַ�������Ϣ

        length, limit = len(p), len(s)
        left = right = 0                    # ��������ָ�룬�ֱ��ʾ���ڵ����ҽ���

        while right < limit:
            c = s[right]
            if c not in needs:              # ����������Ҫ���ַ�ʱ
                window.clear()              # ��֮ǰͳ�Ƶ���Ϣȫ������
                left = right = right + 1    # ����һλ�ÿ�ʼ����ͳ��
            else:
                window[c] = window.get(c, 0) + 1            # ͳ�ƴ����ڸ����ַ����ֵĴ���
                if right-left+1 == length:                  # �����ڴ�С��Ŀ���ַ�������һ��ʱ
                    if window == needs: res.append(left)    # ��������ڵĸ��ַ�������Ŀ���ַ���һ�¾ͽ�left��ӵ������
                                                 # left����
                    window[s[left]] -= 1                    # �����Ƴ����ַ�������һ
                    left += 1
                right += 1                                  # right����
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
                lst[l], lst[r] = lst[r], lst[l]  #����
                l = l + 1
                r = r - 1
            elif lst[l] not in dic:
                l = l + 1
            elif lst[r] not in dic:
                r = r - 1

        return ''.join(lst)















