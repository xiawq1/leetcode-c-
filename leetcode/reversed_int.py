# coding=gbk
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。32位机int取值范围是-2^31~2^31-1
'''
def reverse_force(self, x: int) -> int:
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[:0:-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0

# class Solution {
#     public int reverse(int x) {
#         int ans = 0;
#         while (x != 0) {
#             int pop = x % 10;
#             if (ans > Integer.MAX_VALUE / 10 || (ans == Integer.MAX_VALUE / 10 && pop > 7))
#                 return 0;
#             if (ans < Integer.MIN_VALUE / 10 || (ans == Integer.MIN_VALUE / 10 && pop < -8))
#                 return 0;
#             ans = ans * 10 + pop;
#             x /= 10;
#         }
#         return ans;
#     }
# }


class Solution(object):
    def reverse(self, x):
        ans = 0
        flag = 1
        if x <0:
            x = -x;
            flag = -flag

        while x  != 0:
            cur = x % 10
            ans = ans*10 + cur
            x //= 10
        return ans*flag if -2**31 <ans*flag <2**31 else 0
a = Solution().reverse(874)
print(a)




