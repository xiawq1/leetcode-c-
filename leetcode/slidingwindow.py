#coding:gbk
#无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s):
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

ans  = Solution().lengthOfLongestSubstring("pwwkew")


class Solution1:
    def minWindow(self, s, t):
        from collections import defaultdict   ####避免key不存在时引发的异常
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1   ######计数，某个单词出现的频率
        start = 0   ##当字符串遇上完毕后，移动一个字符
        end = 0   #####先移动，碰到t中的字符时，记录，直到全都遇上，记录整个字符串的长度。
        min_len = float("inf")  # 无穷大
        counter = len(t)  # counter为0时，开始窗口移动
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:  # 可行窗口中出现一次t中字符就就记录一次
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:  # 移动窗口
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    # 行为窗口中最左的字符是t中字符并且只在行为窗口中出现一次就停止移动
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res

Solution1().minWindow("ADOBECODEBANC","ABC")

#30
class Solution4:
    def findSubstring(self, s, words):
        from collections import Counter
        if not s or not words: return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word: return []
        words = Counter(words)
        res = []

        for i in range(0, one_word):  # 防止单词截断的问题
            cur_cnt = 0  # 窗口中每出现一次单词就加一，非words中单词减一
            left = i  # 窗口左指针
            right = i  # 窗口右指针
            cur_Counter = Counter()  # 创建窗口
            while right + one_word <= n:  # 窗口右指针移动遍历s
                w = s[right:right + one_word]
                right += one_word

                # cur_Counter[w] += 1
                # cur_cnt += 1

                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1

                while cur_Counter[w] > words[w]:
                    # 窗口中出现非words中单词或者words中单词出现1次以上，需移动窗口左指针，移动到w的位置
                    left_w = s[left:left + one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:  # words中单词已在窗口中全部出现
                    res.append(left)
        return res

#209
class Solution:
    def minSubArrayLen(self, s, nums):
        if sum(nums) < s:   ##如果nums的总和小于s，则返回0
            return 0
        if sum(nums) == s:
            return len(nums)
        left = 0  #左指针
        right = 0 ##右指针
        sub_sum = 0
        length = len(nums)
        for right, item in enumerate(nums):
            sub_sum += item
            while sub_sum >= s:
                length = min(length, right-left+1)
                sub_sum -= nums[left]   ##
                left += 1
        return length

#53   滑动窗口






    ##动态规划
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = 0, maxAns = nums[0];
        for (const auto &x: nums) {
            pre = max(pre + x, x);
            maxAns = max(maxAns, pre);
        }
        return maxAns;
    }
};

#152给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组,并返回该子数组所对应的乘积。
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxF = nums[0], minF = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int mx = maxF, mn = minF;
            maxF = max(mx * nums[i], max(nums[i], mn * nums[i]));   #保存最大值
            minF = min(mn * nums[i], min(nums[i], mx * nums[i]));   #保存最小值
            ans = max(maxF, ans);
        }
        return ans;
    }
};








