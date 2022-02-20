
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numset = set(nums)
        
        if len(nums) == len(numset):
            return False
        return True

print(Solution().containsDuplicate([1,2,3,1]))
