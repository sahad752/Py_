


def minWindow(s, t):
    table = {}
    for c in t:
        table[c] = table.get(c, 0) + 1
    
    begin,end = 0,0
    counter = len(table)
    len1 = float('inf')
    ans = ""
    while end < len(s):
        endchar = s[end]
        if endchar in table:
            table[endchar] -= 1
            if table[endchar] == 0:
                counter -= 1
        end += 1

        # if counter == 0: # find a window
        while counter == 0:
            if end - begin < len1:
                len1 = end - begin
                ans = s[begin:end]
            startchar = s[begin]
            if startchar in table:
                table[startchar] += 1
                if table[startchar] > 0:
                    counter += 1
            begin += 1
    return ans


print(minWindow("ADOBECODEBANC", "ABC"))


