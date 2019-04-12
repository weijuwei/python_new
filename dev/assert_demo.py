#"断言"是一个心智正常的检查，确保代码没有做什么明显错误的事情。
#这些检查由assert语句执行。如果失败，就会抛出异常

ss = 'red'
assert ss == 'red', 'ss need to be red'

ss = 'green'
assert ss == 'red','ss need to be red'