# -*- coding: utf-8 -*
name = ['lily', 'charles', 'leo']

# 迭代
for k in name:
    print(k)

# range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))
total = list(range(101))

# 计算从1加到100
sums = 0
for k in total:
    sums += k
print(sums)

sums = 0
n = 99

while n > 0:
    sums += n
    n = n - 2

print(sums)

L = ['Bart', 'Lisa', 'Adam']
for k in L:
    print('Hello,', k)

# 打印1-100
n = 1
while n != 101:
    print(n)
    n = n + 1

print('END')

# 打印1-10
n = 1
while 1:
    print(n)
    n = n + 1
    if n > 10:
        break
print('END')

# 打印1-10
n = 0
while n < 10:
    n = n + 1
    print(n)
print('END')

# 打印1-10间的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('END')

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
