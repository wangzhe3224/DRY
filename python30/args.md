---
title: 如何写只接受关键字参数的函数
tags: functions,intermediate
date: 2021-11-06
---

工程实践中我们经常需要强制某个函数只使用关键字参数作为参数，以增加可读性、避免参数顺序错误。
我们需要 `*` 来实现这种要求，放置在 `*` 后的所有参数都会被要求使用关键字参数传入。

实现：

```python
def recv(maxsize, *, block): 
    'Receives a message' 
    pass
recv(1024, True) # 这种情况会直接抛出类型异常
recv(1024, block=True) # Ok
```