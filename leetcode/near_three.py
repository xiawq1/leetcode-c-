class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7

        # ���ݲ�ֵ�ľ���ֵ�����´�
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # ö�� a
        for i in range(n):
            # ��֤����һ��ö�ٵ�Ԫ�ز����
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # ʹ��˫ָ��ö�� b �� c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # �����Ϊ target ֱ�ӷ��ش�
                if s == target:
                    return target
                update(s)
                if s > target:
                    # ����ʹ��� target���ƶ� c ��Ӧ��ָ��
                    k0 = k - 1
                    # �ƶ�����һ������ȵ�Ԫ��
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # �����С�� target���ƶ� b ��Ӧ��ָ��
                    j0 = j + 1
                    # �ƶ�����һ������ȵ�Ԫ��
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best

