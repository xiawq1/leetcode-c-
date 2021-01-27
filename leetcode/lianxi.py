#coding:gbk

'''
1.����һ���������� nums ��һ������Ŀ��ֵ target�������ڸ��������ҳ� ��ΪĿ��ֵ ���� ���� ���������������ǵ������±ꡣ

'''


#ö����
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

'''
2. ��������?�ǿ� ��������ʾ�����Ǹ�������������ÿλ���ֶ��ǰ���?����?�ķ�ʽ�洢�ģ�����ÿ���ڵ�ֻ�ܴ洢?һλ?���֡�

���㽫��������ӣ�������ͬ��ʽ����һ����ʾ�͵�����


'''

class ListNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        sumlistnode = ListNode(0)
        temp = sumlistnode
        sum = 0
        while l1 and l2:
            res = (l1.val + l2.val + sum) % 10
            sum = (l1.val + l2.val + sum) // 10
            temp.next = ListNode(res)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            res = (l1.val + sum) % 10
            sum = (l1.val + sum) // 10
            temp.next = ListNode(res)
            temp = temp.next
            l1 = l1.next
        while l2:
            res = (l2.val + sum) % 10
            sum = (l2.val + sum) // 10
            temp.next = ListNode(res)
            temp = temp.next
            l2 = l2.next
        if sum == 1:
            temp.next = ListNode(1)
            temp = temp.next
        return sumlistnode.next

'''
3. ����һ���ַ����������ҳ����в������ظ��ַ��� ��Ӵ� �ĳ��ȡ�
'''


#��������
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ��ϣ���ϣ���¼ÿ���ַ��Ƿ���ֹ�
        occ = set()
        n = len(s)
        # ��ָ�룬��ʼֵΪ -1���൱���������ַ�������߽����࣬��û�п�ʼ�ƶ�
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # ��ָ�������ƶ�һ���Ƴ�һ���ַ�
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # ���ϵ��ƶ���ָ��
                occ.add(s[rk + 1])
                rk += 1
            # �� i �� rk ���ַ���һ�����������ظ��ַ��Ӵ�
            ans = max(ans, rk - i + 1)
        return ans
'''
4. ����������СΪ m �� n �����򣨴�С�������� nums1 �� nums2�������ҳ������������������������λ����
������: [2 3 5] ��Ӧ����λ��Ϊ3

ż����: [1 4 7 9] ��Ӧ����λ��Ϊ (4 + 7) /2 = 5.5

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:




'''
5����һ���ַ��� s���ҵ� s ����Ļ����Ӵ���
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # ö���Ӵ��ĳ��� l+1
        for l in range(n):   #i����ʼλ�ã� l�ǳ���
            # ö���Ӵ�����ʼλ�� i����������ͨ�� j=i+l �õ��Ӵ��Ľ���λ��
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans

'''
6 ��һ�������ַ��� s ���ݸ��������� numRows ���Դ������¡������ҽ��� Z �������С�
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        rows = ['' for i in range(numRows)]
        i = 0
        flag = -1
        for c in s:
            rows[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return ''.join(rows)

'''
7. ����һ�� 32 λ���з�������������Ҫ�����������ÿλ�ϵ����ֽ��з�ת��

32λ��intȡֵ��Χ��-2^31~2^31-1
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        elif x > 0:
            x = str(x)
            x = int(x[::-1])
        elif x < 0:
            x = str(-x)
            x = int(x[::-1])
            x = -x
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        else:
            return 0


'''
9. 
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >=0:
            a = str(x)
            a = int(a[::-1])
            if x == a:
                return True
            else:
                return  False

'''
10. ����һ���ַ���?s?��һ���ַ�����?p��������ʵ��һ��֧�� '.'?��?'*'?��������ʽƥ�䡣

'.' ƥ�����ⵥ���ַ�
'*' ƥ���������ǰ�����һ��Ԫ��
��νƥ�䣬��Ҫ����?����?�ַ���?s�ģ������ǲ����ַ�����

'''

#��̬�滮


'''
11. ���� n ���Ǹ����� a1��a2��...��an��ÿ�������������е�һ����?(i,?ai) ���������ڻ� n ����ֱ�ߣ���ֱ�� i?�������˵�ֱ�Ϊ?(i,?ai) �� (i, 0) ���ҳ����е������ߣ�ʹ��������?x?�Ṳͬ���ɵ�����������������ˮ��

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        left = 0
        right = n-1
        area = 0
        while left < right:
            area = max(min(height[left], height[right])*(right-left), area)
            if height[left] >= height[right]:
                right = right - 1
            else:
                left = left + 1

        return area

'''
12.
'''



'''
13.
'''


'''
14
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longest = strs[0]
        for i in range(1, len(strs)):

            longest = self.find_(longest, strs[i])
        return longest

    def find_(self, m, n):
        l = min(len(m), len(n))
        i = 0
        res = ''
        while i < l:
            if m[i] == n[i]:
                res += m[i]
            else:
                break
            i += 1
        return res

#15
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # ö�� a
        for first in range(n):
            # ��Ҫ����һ��ö�ٵ�������ͬ
            if first > 0 and nums[first] == nums[first - 1]:   #��ֹ�ظ�
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

#16
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return
        nums.sort()
        n = len(nums)


        best = float('inf')
        for first in range(n):


            if first > 0 and nums[first] == nums[first-1]:
                continue
            target1 = target-nums[first]
            l = first + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] > target1:
                    r -= 1
                elif nums[l] + nums[r] < target1:
                    l += 1
                elif nums[l] + nums[r] == target1:
                    return target
                res = nums[first] + nums[l] + nums[r]
                if abs(res-target) < abs(best - target):

                    best = res


        return res

#17
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backTrack(path, index):
            if len(path) == n:
                res.append(''.join(path))
                return

            for i in phoneMap[digits[index]]:

                backTrack(path+[i], index+1)


        n = len(digits)
        res = []
        backTrack([], 0)
        return res

#18

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                target1 = target - nums[i] - nums[j]

                l = j+1
                r = len(nums)-1
                while l < r:
                    if nums[l] + nums[r] > target1:
                        r0 = r - 1
                        if nums[r0] == nums[r]:
                            r0 = r0 -1
                        r = r0

                    if nums[l] + nums[r] < target1:
                        l0 = l + 1
                        if nums[l0] == nums[l]:
                            l0 = l0 + 1
                        l = l0

                    if nums[l] + nums[r] == target1:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
        return res


#19

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        if not head:
            return
        length = getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        temp = head
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
# 20  ջ
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
#21
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return

        dummy = ListNode(0)
        temp = dummy
        while l1 and l2:
            if l1.val >= l2.val:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next


#22
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(l, r, path):
            if len(path) == n*2:
                res.append(path)
                return

            if l < n:

                backtrack(l + 1, r, path + '(')

            if r < l:

                backtrack(l, r+1, path + ')')

        res = []
        backtrack(0, 0, '')
        return res


#23 merge k list   �Ⱥϲ�2������ѭ��һֱ����

#24
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return []
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy

        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummy.next

#25 K ��һ�鷭ת����
class Solution:
    # ��תһ�����������ҷ����µ�ͷ��β
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # �鿴ʣ�ಿ�ֳ����Ƿ���ڵ��� k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # �����������½ӻ�ԭ����
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next
#26
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        b = 1
        while b < len(nums):
            if nums[b] == nums[a]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a+1


#27
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b
#28
#��������



#29
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [?2**31, 2**31?1]
        flag = 1  # �洢�����ţ��������ӷ�ĸת��Ϊ����
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor = -flag, -divisor

        res = 0
        while dividend >= divisor:  # ����1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
            cur = divisor
            multiple = 1
            while cur + cur < dividend:  # �üӷ������֤divisor * multiple <= dividend�����multiple
                cur += cur  # ��cur�ֱ����1, 2, 4, 8, 16...2^n��������������
                multiple += multiple
            dividend -= cur
            res += multiple

        res = res if flag > 0 else -res  # �ָ�������

        if res < MIN_INT:  # �����Ƿ�������ؽ��
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT

#30





#31     buhui
class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
#32




#33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1


        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

#34
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] >= target:
                r = mid


#36
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:



#38
class Solution:
    def countAndSay(self, n: int) -> str:
        pre = ''
        cur = '1'

        # �ӵ� 2 �ʼ
        for _ in range(1, n):
            # ����ע��Ҫ�� cur ��ֵ�� pre
            # ��Ϊ��ǰ�������һ���ǰһ��е��ƣ����������
            pre = cur
            # ���� cur ��ʼ��Ϊ�գ�����ƴ��
            cur = ''
            # ����˫ָ�� start��end
            start = 0
            end = 0
            # ��ʼ����ǰһ���ʼ����
            while end < len(pre):
                # ͳ���ظ�Ԫ�صĴ��������ֲ�ͬԪ��ʱ��ֹͣ
                # ��¼���ֵĴ�����
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                # Ԫ�س��ִ�����Ԫ�ؽ���ƴ��
                cur += str(end - start) + pre[start]
                # ������� start����ʼ��¼��һ��Ԫ��
                start = end

        return cur


#41
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

#42











































































