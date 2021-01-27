#coding:gbk
#����һ���ַ����������ҳ����в������ظ��ַ��� ��Ӵ� �ĳ��ȡ�
##����ָ��
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
s = "abcabcbb"
ans = Solution().lengthOfLongestSubstring(s)
