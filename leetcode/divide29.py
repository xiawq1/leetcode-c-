class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [?2**31, 2**31?1]
        flag = 1  # 存储正负号，并将分子分母转化为正数
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor = -flag, -divisor

        res = 0
        while dividend >= divisor:  # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
            cur = divisor
            multiple = 1
            while cur + cur < dividend:  # 用加法求出保证divisor * multiple <= dividend的最大multiple
                cur += cur  # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
                multiple += multiple
            dividend -= cur
            res += multiple

        res = res if flag > 0 else -res  # 恢复正负号

        if res < MIN_INT:  # 根据是否溢出返回结果
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
