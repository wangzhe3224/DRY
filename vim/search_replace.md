# Search and replace

```
body    { color: #3c3c3c; } 
a       { color: #0000EE; }
strong  { color: #000; }
```

I love Paris in the
the springtime. their

```
:%s///gn   count matched numbers and lines.
117 matches on 65 lines
```

`:[range]s[ubstitute]/{pattern}/{string}/[flags]`

`:%s/content/copy/gc`  eye ball selection.

last name,first name,email
neil,drew,drew@vimcasts.org
doe,john,john@example.com