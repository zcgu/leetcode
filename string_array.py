# substring 模版

def substring(s):
    table = {}
    p1 = p2 = 0
    
    while p2 < len(s):
        table[s[p2]] = table.get(s[p2], 0) + 1
        p2 += 1
        
        while table: #不符合
            table[s[p1]] -= 1
            p1 += 1
            res = min(res, p2 - p1) # get min le    ngth here

        res = max(res, p2 - p1) # get max length here

    return res
