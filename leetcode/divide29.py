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
