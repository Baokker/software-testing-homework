# 1. 判断三角形类型（用边界值分析和设计测试用例）。

def triangle_atom(a, b, c):
    if (a <= 0 or a > 800) or (b <= 0 or b > 800) or (c <= 0 or c > 800):
        return 'out of range'
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b and b == c:
                return 'equilateral triangle'
            else:
                return 'isosceles triangle'
        else:
            return 'normal triangle'
    else:
        return 'not a triangle'


def manual_test():
    print("question 1 manual test")
    print("Please enter the lengths of the three sides, for example 1 1 1")
    while True:
        a = int(input())
        b = int(input())
        c = int(input())
        print(triangle_atom(a, b, c))

    # 手动测试的函数实现
    pass


def auto_test():
    print("question 1 auto test")
    # 自动测试的函数实现
    pass


def explain():
    # 解释说明的函数实现
    print("更多的解释说明见作业文档")


if __name__ == "__main__":
    manual_test()
    auto_test()
    explain()
