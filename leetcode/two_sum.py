###¹şÏ£±í
def twonums(nums, target):
    hash = {}
    for index, num in enumerate(nums):
        hash[num] = index
    for i, num in enumerate(nums):
        j = hash.get(target-num)
        if j is not None and i != j:
            return [i, j]

a = twonums([2, 7, 11, 15], 9)
print(a)

class two_sum(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def find_target(self):
        for i, t in enumerate(self.nums):
            for j, k in enumerate(self.nums):
                if t + k == self.target and i!=j:
                    return [t, k]
s = two_sum([2, 7, 11, 15], 9)
a = s.find_target()
print(a)
######±©Á¦Ã¶¾Ù£¬¸´ÔÓ¶Èo£¨n2£©
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


