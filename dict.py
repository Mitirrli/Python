# -*- coding:utf-8 -*-
# dict 字典（也称map）

d = {'name': 'Leo', 'age': 12}

# 用in来判断字典里是否含有某个键
w = 'age' in d
print(w)
print(d['name'])

# 使用get获得值,逗号后跟默认值
print(d.get('ages', -1))

# 删除key用pop
d.pop('age')
print(d)

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。


