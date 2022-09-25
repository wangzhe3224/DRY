---
title: 如何实现函数Curry
tags: functions,intermediate
date: 2021-10-30
---

Curry是函数式编程的基石之一，实质上就是闭包的应用。

```python
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)

add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```