# Alyssum

this package contains my personal helpers if you want to use below the usage examples

## Title
```python
from alyssum.seperators import Title

title = Title(label='Default Text', length=80, color='yellow', design_char='*')
title.configure(label='Default Text', length=80,color='blue',design_char='*')

title.write() # writes "Default Text"
title.write("any title") # writes "any title"

title.configure(color=blue).write("any title") # can be usable
```

label length can not be greater than (length - 2)  
color can be 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan' or 'white'  
length must be greater than 1 and smaller than 81 



## Cleaner

```python
from alyssum.cleaners import Cleaner
Cleaner.clean("Hello World!")
```
