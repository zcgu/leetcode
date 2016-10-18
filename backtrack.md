# 排列组合题

一般是组合题，比如n = 4，k = 2, 选:[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]，
[2, 3, 6, 7]，sum7，选[[7],[2, 2, 3]]，
选subset，[1,2,3]，[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]。

组合题，用一个start：
```
    def dfs(self, nums, k剩余次数, start):   # nums可以是list，可以是最大值。k是sum，或者是还要取几个。
        if k == 0: return [[]]              # 成功
        if start == len(nums): return []    # 截至
        
        res = []
        for l in self.dfs(n, k, start + 1):   # 下一项，不取start
            res.append(l)
        
        for l in self.dfs(n, k - 1, start + 1):  #下一项，取start
            res.append([start] + l)
        
        return res
```

有重复的组合题，先排序！再加一个used：

```
    def dfs(self, cs, target, start, used):
        if target == 0: return [[]]
        if target < 0 or start == len(cs): return []
        
        res = []
        
        for l in self.dfs(cs, target, start + 1, used):   # 下一项，不取start，这是总可以的
            res.append(l)
        
        if start > 0 and cs[start] == cs[start - 1] and not used[start  -1]:  # 如果重复的且上一个没取，这个就不取
            return res
        
        used[start] = True                                #下一项，取start，要标记used
        for l in self.dfs(cs, target - cs[start], start + 1, used):
            res.append([cs[start]] + l)
        used[start] = False
        
        return res
```
这基本涵盖所有情况了。


排列题，不需要start，要used：

```
    def dfs(self, nums, used):
        if False not in used: return [[]]
        
        res = []
        for i in range(len(nums)):
            if used[i]: continue
            
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:    # 输入有重复的判断，没重复不要。
                continue
            
            used[i] = True
            for lst in self.dfs(nums, used):
                res.append([nums[i]] + lst)
            used[i] = False
        
        return res
```
