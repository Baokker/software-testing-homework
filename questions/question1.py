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
    #data_t = np.loadtxt(open("testData/triangle_equivalenceclass.csv"), delimiter=",", usecols=[4])
    print("question 1 auto test")
    for data_row in data:
        print("本次自动测试的数据为 %d %d %d" % (data_row[0], data_row[1], data_row[2]))
        print("输出结果为：" + triangle_atom(data_row[0], data_row[1], data_row[2]))
        #print("解释说明：" + data_row[3])
    # 自动测试的函数实现
    pass


def explain():
    # 解释说明的函数实现
    print("更多的解释说明见作业文档")


if __name__ == "__main__":
    manual_test()
    auto_test()
    explain()
