# Binary search

正常的
```
l = 0
r = len(nums) - 1

while l < r:
    mid = (l + r) / 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        r = mid - 1
    else:
        l = mid + 1
return nums(l) == target
```

找一系列的最左边一个，first bad version,
```
l = mid + 1
r = mid
```

找一系列的最右边一个，
```
mid = (l + r) / 2 + 1

l = mid
r = mid － 1
```



找比他大的那个，插入位置
```
r = len(nums)
l = mid + 1
r = mid
```


＃sorted array 有一系列，
[5,6,7,8,1,2,3].

判断重点
