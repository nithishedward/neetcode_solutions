class Solution:
    def removeDuplicates(self,n: list[int])->int:
        u=sorted(set(n))
        n[:len(u)]=u
        return len(u)