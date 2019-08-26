# age = 20
# if age >= 18:
#     # print('你的年龄是%d' % age)
#     print('你的年龄是', age)
#     print('adult')


# age = 3
# if age >= 18:
#     # print('你的年龄是%d' % age)
#     print('你的年龄是', age)
#     print('adult')
# else:
#     print('你的年龄是', age)
#     print('teenager')


# age = 3
# if age >= 18:
#     # print('你的年龄是%d' % age)
#     print('你的年龄是', age)
#     print('adult')
# elif age == 3:
#     print('three')
# else:
#     print('你的年龄是', age)
#     print('teenager')


# if x:
#     print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False

# input 返回的数据类型是string

number = 100
guess = input('请输入你猜的数：')
if number == int(guess):
    print('win')
else:
    print('lose')
