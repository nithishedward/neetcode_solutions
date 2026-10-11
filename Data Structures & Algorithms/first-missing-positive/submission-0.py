class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=1
        while True:
            flag = True
            for n in nums:
                if m==n:
                    flag=False
                    break
            if flag:
                return m
            m+=1