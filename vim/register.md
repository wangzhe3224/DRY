# Register

The default register: `"`.
It contains anything you delete or yank.
    Vim use content inside `"` as the content of paste command `p`.

- `p` -> `""p`
- `"2p` paste content in register 2
- `:reg` show all the content in the registers

Read only registers:

- `".`: last inserted content
- `"%`: the current file path
- `":`: the most recent executed command
- `"#`: alternate file

In `Insert` mode, hit `C-r` will trigger register access, it show a `"` waiting
for you to type in the register name and yank the content.

`"*` the system clip board.
