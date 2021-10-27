---
title: f-string的技巧 
tags: string,intermediate
date: 2021-10-27
---

f-string 已经是Python必不可少的工具。

1. `=` 可以打印变量名和他的值

```python
str_val = 'apples'
num_val = 42
print(f'{str_val=}, {num_val = }') 
# str_val='apples', num_val = 42
```

2. 数字格式化

```python
price_val = 6.12658
print(f'{price_val:.2f}') # 6.13
```

3. 日期格式化

```python
from datetime import datetime;
date_val = datetime.utcnow()
print(f'{date_val=:%Y-%m-%d}') # date_val=2021-07-09
```
