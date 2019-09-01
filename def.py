# -*- coding:utf-8 -*-
def user_abs(x, y, func):
    return func(x) + func(y)


print(user_abs(1, -1, abs))