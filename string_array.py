# substring 模版
# 395. Longest Substring with At Least K Repeating Characters 模版失效？

def substring(s):
    table = {}
    p1 = p2 = 0
    
    while p2 < len(s):
        table[s[p2]] = table.get(s[p2], 0) + 1
        p2 += 1
        
        while p1 < p2 and some statement: #找最小是符合，找最大是不符合。
            res = min(res, p2 - p1) # get min length here
            
            table[s[p1]] -= 1
            p1 += 1
        res = max(res, p2 - p1) # get max length here

    return res
