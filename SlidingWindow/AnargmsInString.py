
from itertools import count


def findAnargms(s,p):
    table = {}
    ans = []

    for c in p:
        table[c] = table.get(c, 0) + 1

    if len(s)<len(p) or len(table)==0 or len(p)==0:
        return []
    
    begin , end = 0,0
    word_size = len(p)
    counter = len(table)

    while end < len(s):
        endchar = s[end]

        if endchar in table:
            table[endchar] -= 1
            if table[endchar] == 0:
                counter -= 1
        end += 1

        while counter == 0:
            if end - begin == word_size:
                ans.append(begin)
            
            beginchar = s[begin]
            if beginchar in table:
                table[beginchar] += 1
                if table[beginchar] > 0:
                    counter += 1
            begin += 1
    return ans

print(findAnargms("ADOABCBAECODEBANCBA", "ABC"))