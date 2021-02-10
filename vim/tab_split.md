# Vim :-) 

## Tab
- `:tabnew {filename}`, lanuch an empty new tab
- `{number}gt`, jump to next tab or number tab
- `C-W T`, make current split into a tab

## Split

- `C-w +/-/</>`, adjust split size
- `C-w =`, adjust eually
- `C-w o`, close all split only left current one

## Buffer

- `:bd`, kill current buffer

## Surround actions

It depends on `vim.surround` plugin. 

- `cs{prev}{new}`, change surround mark from prev to new.
- `ds{curr}`, delete current surround marks.
- `ys{text object}{new}`, insert new marks around text object.
    * `ysiw"`, add double quotes around current word.
    * `yss{`, add {} around the whole line, recall `s` represents line.

## Command in Insert Mode

Press `C-o` in inert mode will bring us to a temperory Normal mode, in which
we can execute 1 command by 1 key stroke. For example, `C-o zz`.

edit text in insert mode:
- `C-h`, delete 1 char
- `C-w`, delete 1 word
- `C-u`, delete to the start of the line
- `C-b/f`, move the cursor back/front
- `C-j/k`, move the cursor up/down
- `C-p/n`, activate auto complete
- `C-m`, enter key

## Register

Access regiester: 
- In normal mode, `"{regiester name}`.
- In insert mode, `C-r {register name}`. 
- `:reg <register name>`.

Unamed registers: `""`. 

Numbered register will stores every thing you `d/x/y`

Execution register: `"=`. You can do `"=` then enter an expression, say `1+1<enter>`, you got 2 
 in the register. You can even do `system("ls")` to get system call result.

Search registers: `/`, `?`, `*`, `#`. 

Read only registers: 
- `".`, the last inserted text.
- `"%`, the current file path. 
- `":`, the most recent command executed.

## Repeat
- `.`, repeat last action
- `@:`, repeat last command
- `@{register}`, repeat whatever in the register, Marco.

## Fast edit in Insert mode

- `C-h`: delete back 1 char
- `C-w`: delete back 1 word
- `C-u`: delete back to start of line

there is a Insert - Normal mode, for example:

`<C-o>zz`, will take you to temperory normal mode an execute `zz`.

`<C-R>{register}` can be used. For example: `<C-R>=11*10` 

## Spell checks

- `:set spell`
- `z=`, check correctness.
- `zg`, add a word
- `]s`, next error
- `[s`, previous error
