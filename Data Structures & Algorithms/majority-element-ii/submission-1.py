class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [num for num, freq in count.items() if freq > len(nums) // 3]