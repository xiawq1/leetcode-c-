#coding:gbk
#704
class Solution():
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        if nums[right] == target:
            return right

        return -1
#69
class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        left = 0
        right = x-1
        while left < right:
            mid = (left+right+1)//2
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return left

#34
class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        if nums[left] == target:
            left_bound = left
        else:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[right] == target:
            right_bound = right
        else:
            right_bound = left_bound
        return [left_bound, right_bound]
Solution().searchRange([5,7,7,8,8,10], 8)

#35
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search_t(nums, target):
            if nums is None or len(nums) == 0:
                return -1
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if nums[left] == target:
                return left
            else:
                return -1
        if nums is None or len(nums) == 0:
            return 0
        now_search = search_t(nums, target)
        if now_search != -1:
            return now_search
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
#153

#ץס��ת�����е��ص㣬�������ֳ������֣��������涼�������У�������������С���ң����������7���������0ʱ�ͻ��ҵ���Сֵ�ˡ�
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        #һ����
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right ) // 2
            if nums[mid] > nums[right]:#�ڵڶ�������һ��ʲôʱ���ܰ�[mid]�ų������϶���������[right]��ֵʱ
                left = mid + 1
            else:
                right = mid
        return nums[left]

#154 ���ظ�ֵ
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) == 0:
            return -1
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right-left) // 2
            if numbers[mid] > numbers[right]: #��ֻ֤��һ��if
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]

#33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def min_num(nums):#�����ת������Сֵ��Ӧ������ֵ
            if nums is None or len(nums) == 0:
                return -1
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]: #Ҫע�⽫left�Ƶ�mid������������ǲ�����ȫ�ģ��ҵľ�������߼�
                    left = mid + 1
                else:
                    right = mid
            return left
        def search_t(nums, target):
            if nums is None or len(nums) == 0:
                return -1
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if nums[left] == target:
                return left
            else:
                return -1
        #def search(nums, target):
        if nums is None or len(nums) == 0:
            return -1
        min_num_index = min_num(nums)
        if target >= nums[min_num_index] and target <= nums[-1]:
            now_nums = nums[min_num_index: ]
            now_search = search_t(now_nums, target)
            if now_search == -1:
                return -1
            else:
                return min_num_index + now_search
        else:
            now_nums = nums[ :min_num_index]
            now_search = search_t(now_nums, target)
            return now_search

#81
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def min_num(nums):#�����ת������Сֵ��Ӧ������ֵ
            if nums is None or len(nums) == 0:
                return -1
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]: #Ҫע�⽫left�Ƶ�mid������������ǲ�����ȫ�ģ��ҵľ�������߼�
                    left = mid + 1
                else:
                    right = mid
            return left
        def search_t(nums, target):
            if nums is None or len(nums) == 0:
                return -1
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if nums[left] == target:
                return left
            else:
                return -1
        #def search(nums, target):
        if nums is None or len(nums) == 0:
            return -1
        min_num_index = min_num(nums)
        if target >= nums[min_num_index] and target <= nums[-1]:
            now_nums = nums[min_num_index: ]
            now_search = search_t(now_nums, target)
            if now_search == -1:
                return -1
            else:
                return min_num_index + now_search
        else:
            now_nums = nums[ :min_num_index]
            now_search = search_t(now_nums, target)
            return now_search


#69
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

#81
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[mid] <= nums[-1]:

                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False