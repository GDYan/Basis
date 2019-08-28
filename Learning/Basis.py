import sys
#中文编码python3 默认utf-8编码
from base64 import encode
from random import shuffle, choice
import os

def basis1():
    print("======换行 数据链接======")
    x = 1 + \
        2 + \
        3
    print("x", x)
    print("======命令行参数======")
    for i in sys.argv:
        print("python路径", i)

    print("======输出指定数据类型======")
    print('x的类型', type(x))  # 输出本身的类型
    print("======判断数据类型是不是指定的类型======")
    print('x的数据类型是不是整形呢', isinstance(x, int))  # isinstance会拿到数据的父类对象来做比较
    print("======del 删除数据引用======")
    print('x本来的值', x)
    del x
    # print('删除引用之后的x值', x) 报错
    print("======幂运算======")
    print('2的5次方', 2 ** 5)
    print("======除法运算======")
    print('5/2', 5 / 2)  # 默认浮点数
    print('5//2', 5 // 2)  # 向下入最接近除数值(类型跟随被除数)
    print("======复数类型======")
    print(complex(1, 2))
    string = 'myname'  # 字符串不允许被改变没有string[0]=*
    print(string)
    for i in range(2, 4):  # range  2--4所以输出2，3两个字符
        print(string[i])

    string1 = list(string)
    print(string1)
    print(string1.reverse())
    print(string[-1::-1])
    tuple = ('tom', 'tom', 'jrrey')  # 强转成set 进行去重
    set1 = set(tuple)
    print(set1)

        # is not is


    a = b = 20
    # b = 20

    if (a is b):
        print("1 - a 和 b 有相同的标识")
    else:
        print("1 - a 和 b 没有相同的标识")

    if (id(a) == id(b)):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    # 修改变量 b 的值
    b = 30
    if (a is b):
        print("3 - a 和 b 有相同的标识")
    else:
        print("3 - a 和 b 没有相同的标识")

    if (a is not b):
        print("4 - a 和 b 没有相同的标识")
    else:
        print("4 - a 和 b 有相同的标识")

    a = ['1','2','3']
    b = a[:]

    print('a', a, 'b', b, b is a)#?????????

    del a, b
    a = [1, 2, 3, 4, 5]
    print('before', a)
    print('choice', choice(a))
    shuffle(a)
    print("after shuffle a is %s" % (a))
    print()

    print()
    print('after', a)  # ????????????
    # 强转倒转字符串
    string1 = list(string)
    print(string1)
    print(string1.reverse())  # list倒置
    b1 = -10
    print('b+', abs(b1))

    print('b=%d,%s' % (b1, '小明'))


def base2():
    file = open('../doc/title.txt')
    val = {}
    for line in file:
        key, vaule = line.split('=')
        val[key.strip()] = vaule.strip()

    print(val)

def batch_change_filename():
    path = 'D:\迅雷下载\火影忍者/'
    all_path = os.listdir(path)
    num = list(range(600, 721))
    suffix = ['.rmvb', '.mkv', '.mp4']
    old_file_suffix = None
    for old_file in all_path:
        for suf in suffix:
            if old_file.find(suf) != -1:
                old_file_suffix = old_file[old_file.find(suf):]
        old_file = path + old_file
        for i in num:
            if old_file.find(str(i)) != -1:
                new_file = path + '火影忍者-' + str(i) + old_file_suffix
                os.rename(old_file, new_file)
                print(new_file, 'success')
                num.remove(i)
    for i in num:
        print(i)






if __name__ == "__main__":
    #basis1()
    #base2()
    batch_change_filename()
