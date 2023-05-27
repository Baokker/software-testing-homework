# 9. 判断三角形类型（等价类方法分别分析和设计测试用例）。
import numpy as np


def triangle_atom(a, b, c):
    if a == 0:
        return "a不能为0"
    if b == 0:
        return "b不能为0"
    if c == 0:
        return "c不能为0"
    if a < 0:
        return "a取值不能为负"
    if b < 0:
        return "b取值不能为负"
    if c < 0:
        return "c取值不能为负"
    if a >= 800:
        return "a取值不在范围之内"
    if b >= 800:
        return "b取值不在范围之内"
    if c >= 800:
        return "c取值不在范围之内"
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b and b == c:
                return '等边三角形'
            else:
                return '等腰三角形'
        else:
            return '不等边三角形'
    else:
        return '非三角形'


def manual_test():
    # 手动测试的函数实现
    print("手动测试")
    while True:
        nums = input("请输入三条边长a、b、c，以空格分隔，例如1 1 1：")
        a, b, c = map(float, nums.split())
        print("实际输出：", triangle_atom(a, b, c))
    pass


def auto_test():
    # 自动测试的函数实现
    data = np.loadtxt(open("../testData/triangle_equivalenceclass.csv"), delimiter=",", usecols=[1, 2, 3])
    print("自动测试")
    for data_row in data:
        print("本次自动测试的数据为 %g %g %g" % (data_row[0], data_row[1], data_row[2]))
        print("输出结果为：" + triangle_atom(data_row[0], data_row[1], data_row[2]))
    pass


def explain():
    # 解释说明的函数实现
    print("更多的解释说明见作业文档")


if __name__ == "__main__":
    while True:
        choice = input("请选择测试类型，1为手动测试，2为自动测试：")
        if choice == '1':
            manual_test()
            break
        elif choice == '2':
            auto_test()
            break
        else:
            print("选择有误，请重新输入")
    explain()
