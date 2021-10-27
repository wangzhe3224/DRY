---
title: sort和sorted的区别
tags: list,intermediate
date: 2021-10-25
---

Python提供了两种列表排序操作：`sorted()` vs `[].sort()`，他们看起来很像，但是大有不同：`sorted()` 会返回一个新的列表，而 `sort()` 则会在原列表进行操作，返回值是 `None` 。了解这一区别，避免不必要的麻烦。

``` python
nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums)           # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())    # None
print(nums)           # [0, 1, 2, 3, 4, 5, 6]
```

从函数的调用方式可以帮助记忆：`[].sort()` 是对象方法的形式，意味着会才做对象本身；`sorted` 是函数调用方式，意味着会返回新的值。