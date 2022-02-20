from operator import le


def lengthOfLongestSubstring( s):
    seen = {}
    begin,end = 0,0
    len1 = 0
    ans = ""
    
    while end < len(s):
        current = s[end]
        if current in seen and seen[current] >= begin:
            begin = seen[current] + 1
        else:
            seen[current] = end
            end += 1
        
        if end - begin > len1:
            len1 = end - begin
            ans = s[begin:end-begin]
    return len1

print(lengthOfLongestSubstring("abcabcbb"))