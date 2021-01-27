class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j=len(digits)-1
        while j>=0:
            if digits[j]+1<10:
                digits[j]+=1
                return digits
            else:
                digits[j]=0
                j-=1
        if digits[0]==0:
            digits.insert(0,1)
        return digits
