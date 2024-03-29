# 数据类型
# 整数

# 浮点数
# 1.23x109就是1.23e9 0.000012可以写成1.2e-5

# 字符串
# 如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符
# 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
# 比如 'I\'m \"OK\"!'

# 转义字符\
print('I\'m "ok"')
print('I\'m learning \n python')
print('\\n')

# r''包着的默认不转义,字符串直接用+拼接
print(r'\n' + r'\n')

# bool值
# and 是与运算 只有所有都为True，and运算结果才是True
# or是或运算 只要其中有一个为True，or运算结果就是True
# not是非运算 它是一个单目运算符，把True变成False，False变成True
print(not 0)

# 空值 None

# 赋值语句的实际
# 当我们写a = 'ABC'
# 在内存中创建了一个'ABC'的字符串；
# 在内存中创建了一个名为a的变量，并把它指向'ABC'。
# 也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# 常量 通常用全部大写的变量名表示常量

# 除法
print(10 / 3)
# 地板除（/除法只取结果的整数部分）
print(10 // 3)
# 取余
print(10 % 3)

# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向
