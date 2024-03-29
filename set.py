# -*- coding:utf8 -*-

# set 集合

s = set([0, 1, 2, 2])

# 添加元素
s.add(4)
s.add(4)

# 移除元素
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合（确定性、互异性、无序性）

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

# 不可变对象【str是不变对象，而list是可变对象。】
a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
print(a)
print(a.replace('a', 'A'))
print(a)

# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
# 相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：

# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

t = [1, 2, 3]
t.append([4])
print(t)
