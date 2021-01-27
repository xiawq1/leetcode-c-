#coding:gbk
'''
����һ���ַ��� s ��һЩ������ͬ�ĵ��� words���ҳ� s ��ǡ�ÿ����� words �����е��ʴ����γɵ��Ӵ�����ʼλ�á�
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        w_len, s_len = len(words[0]), len(s)
        t_len = w_len * len(words)  # �Ӵ��ĳ���

        word_dict = {}  # words�Ĺ�ϣ��
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        ans = []
        for offset in range(w_len):
            lo, lo_max = offset, s_len - t_len
            while lo <= lo_max:
                tmp_dict = word_dict.copy()
                match = True
                for hi in range(lo + t_len, lo, -w_len):    # ��β��ͷ��������
                    word = s[hi - w_len: hi]
                    if word not in tmp_dict or tmp_dict.get(word, 0) == 0:
                        match = False
                        break   # ��ǰ���ʲ�����Ҫ�� ֱ��ֹͣ����Ӵ�������
                    tmp_dict[word] -= 1
                if match:
                    ans.append(lo)
                lo = hi     # ��loֱ�Ӹ�ֵ �������ȷ����Ż��ĵط�
        return ans
