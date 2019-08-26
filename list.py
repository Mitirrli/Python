color = ['red', 'blue', 'yellow']
print(color)
print(len(color))
print(color[0])

# 取最后一个元素
print(color[-1])

# 取最后第二个元素
print(color[-2])

# list是可变的有序表,可以追加元素到末尾
color.append('pink')
print(color)

# 将元素插入到指定位置
color.insert(1, 'black')
print(color)

# 删除末尾的元素
color.pop()
print(color)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：


# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
color[1] = 'test'
print(color)

print(len(color))

# 元组 tuple tuple和list非常类似，但是tuple一旦初始化就不能修改
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
a = (1, 2)
print(a)

# 要定义一个只有1个元素的tuple
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)

# >>> t = ('a', 'b', ['A', 'B'])
# >>> t[2][0] = 'X'
# >>> t[2][1] = 'Y'
# >>> t
# ('a', 'b', ['X', 'Y'])
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
