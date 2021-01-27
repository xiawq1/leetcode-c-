#coding:gbk
#���ظ��ַ�����Ӵ�
class Solution:
    def lengthOfLongestSubstring(self, s):
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

ans  = Solution().lengthOfLongestSubstring("pwwkew")


class Solution1:
    def minWindow(self, s, t):
        from collections import defaultdict   ####����key������ʱ�������쳣
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1   ######������ĳ�����ʳ��ֵ�Ƶ��
        start = 0   ##���ַ���������Ϻ��ƶ�һ���ַ�
        end = 0   #####���ƶ�������t�е��ַ�ʱ����¼��ֱ��ȫ�����ϣ���¼�����ַ����ĳ��ȡ�
        min_len = float("inf")  # �����
        counter = len(t)  # counterΪ0ʱ����ʼ�����ƶ�
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:  # ���д����г���һ��t���ַ��;ͼ�¼һ��
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:  # �ƶ�����
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    # ��Ϊ������������ַ���t���ַ�����ֻ����Ϊ�����г���һ�ξ�ֹͣ�ƶ�
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

        for i in range(0, one_word):  # ��ֹ���ʽضϵ�����
            cur_cnt = 0  # ������ÿ����һ�ε��ʾͼ�һ����words�е��ʼ�һ
            left = i  # ������ָ��
            right = i  # ������ָ��
            cur_Counter = Counter()  # ��������
            while right + one_word <= n:  # ������ָ���ƶ�����s
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
                    # �����г��ַ�words�е��ʻ���words�е��ʳ���1�����ϣ����ƶ�������ָ�룬�ƶ���w��λ��
                    left_w = s[left:left + one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:  # words�е������ڴ�����ȫ������
                    res.append(left)
        return res

#209
class Solution:
    def minSubArrayLen(self, s, nums):
        if sum(nums) < s:   ##���nums���ܺ�С��s���򷵻�0
            return 0
        if sum(nums) == s:
            return len(nums)
        left = 0  #��ָ��
        right = 0 ##��ָ��
        sub_sum = 0
        length = len(nums)
        for right, item in enumerate(nums):
            sub_sum += item
            while sub_sum >= s:
                length = min(length, right-left+1)
                sub_sum -= nums[left]   ##
                left += 1
        return length

#53   ��������






    ##��̬�滮
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

#152����һ���������� nums �������ҳ������г˻���������������,�����ظ�����������Ӧ�ĳ˻���
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxF = nums[0], minF = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int mx = maxF, mn = minF;
            maxF = max(mx * nums[i], max(nums[i], mn * nums[i]));   #�������ֵ
            minF = min(mn * nums[i], min(nums[i], mx * nums[i]));   #������Сֵ
            ans = max(maxF, ans);
        }
        return ans;
    }
};








