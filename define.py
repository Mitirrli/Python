# -*- coding:utf-8 -*-

def add(x):
    if x > 10:
        return 'big'
    else:
        return 'small'


print(add(101))


# 请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。


def nop():
    pass


# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# 异常机制
def test(x):
    if not isinstance(x, (int, float)):
        raise TypeError('数值类型错误')
    if x >= 0:
        return x
    else:
        return -x


print(test('1'))
