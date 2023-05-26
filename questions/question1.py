# 1. 判断三角形类型（用边界值分析和设计测试用例）。
import numpy as np


def triangle_atom(a, b, c):
    if (a <= 0 or a > 800) or (b <= 0 or b > 800) or (c <= 0 or c > 800):
        return 'Out of range'
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b and b == c:
                return 'Equilateral triangle'
            else:
                return 'Isosceles triangle'
        else:
            return 'Normal triangle'
    else:
        return 'Not a triangle'


def manual_test():
    print("question 1 manual test")
    print("Please enter the lengths of the three sides, for example 1 1 1")
    while True:
        nums = input("请输入三个数字，以空格分隔：")
        a, b, c = map(float, nums.split())
        print(triangle_atom(a, b, c))

    # 手动测试的函数实现1
    pass


def auto_test():
    data = np.loadtxt(open("testData/triangle_equivalenceclass.csv"), delimiter=",", usecols=[1, 2, 3])
    print("question 1 auto test")
    for data_row in data:
        print("本次自动测试的数据为 %d %d %d" % (data_row[0], data_row[1], data_row[2]))
        print("输出结果为：" + triangle_atom(data_row[0], data_row[1], data_row[2]))
    # 自动测试的函数实现
    pass


def explain():
    # 解释说明的函数实现
    print("更多的解释说明见作业文档")
    print('''在本题中，测试用例的输入变量有
- 三角形三条边的长度（0< a,b,c <=800）
测试输出有
- 三角形种类
若采用边界值分析，对a、b、c分别取min，min+，normal，max-，max。得到三个取值集合:
- a,b,c = [1, 2, 400, 799, 800]
若增加健壮性分析，对每个集合再分别增加min-,max+，可得:
- a,b,c = [0, 1, 2, 400, 799, 800, 801]

共有6*3+1=19个测试用例,所以共有19个测试用例。''')


if __name__ == "__main__":
    manual_test()
    auto_test()
    explain()
