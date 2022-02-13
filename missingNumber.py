class Solution(object):
    def findDisappearedNumbers(self, nums):
        for n in nums:
            i = abs(n)-1
            nums[i] = -1* abs(nums[i])

        res = []

        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)

        return res


res = Solution().findDisappearedNumbers([1,2,3,2,1,2])
print(res)