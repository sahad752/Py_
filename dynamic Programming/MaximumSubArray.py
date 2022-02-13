class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = 0
        
        for i in range(len(nums)):
            curSum = max(curSum+nums[i],nums[i])
            maxSum = max(curSum,maxSum)
        
        return maxSum

    def maxSubArray2(self, nums) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            curSum = max(curSum+n,n)
            maxSub = max(maxSub,curSum)
        return maxSub


print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))