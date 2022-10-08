# VS Code 学 VIM （4）- 标记 Marks

this is 1


this is 2


this is 3


```text
# navigate from marks
]'
['
]`
[`

# usually ` means position wise, ' means line wise

# delete mark
:delm!
:delmarks!  delete all
:delmarks a  delete mark a
:delmarks a-z 

# special marks
`.   jump to last changed place
`0   jump to last modified file location
``   jump back in position current buffer
''   jump back in line
`]   last changed or yanked text
```
