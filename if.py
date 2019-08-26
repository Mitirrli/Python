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

# number = 100
# guess = input('请输入你猜的数：')
# if number == int(guess):
#     print('win')
# else:
#     print('lose')


height = 1.75
weight = 80.5

bmi = weight / height / height
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi <= 32:
    print('肥胖')
elif bmi > 32:
    print('严重肥胖')
else:
    print('您的输入有误')
