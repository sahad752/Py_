class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        dic = {}
        length = 0
        l = 0
        for r in range(n):
            if s[r] in dic:
                l = max(dic[s[r]] + 1, l)
            dic[s[r]] = r
            length = max(length, r - l + 1)
        return length
    
