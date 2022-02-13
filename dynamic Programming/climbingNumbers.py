class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        
        dp = [0,1,2]
        for i in range(3,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]


print(Solution().climbStairs(5))