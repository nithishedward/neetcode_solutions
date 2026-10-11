class Solution:
    def twoSum(self,n:List[int],t:int)->List[int]:
        l,r=0,len(n)-1
        while l<r:
            s = n[l]+n[r]
            if s==t: return [l+1, r+1]
            l,r=(l+1,r) if s<t else (l,r-1)
        return []