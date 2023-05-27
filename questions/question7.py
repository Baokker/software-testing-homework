# 7. 电信收费问题系统

def get_total(minutes, times):
    if minutes in range(0, 1000 + 1) and times in range(0, 8 + 1):
        if minutes <= 60:
            if times <= 1:
                return 25 + minutes * 0.15 * (1 - 0.01)
            else:
                return 25 + minutes * 0.15
        elif minutes <= 120:
            if times <= 2:
                return 25 + minutes * 0.15 * (1 - 0.015)
            else:
                return 25 + minutes * 0.15
        elif minutes <= 180:
            if times <= 3:
                return 25 + minutes * 0.15 * (1 - 0.02)
            else:
                return 25 + minutes * 0.15
        elif minutes <= 300:
            if times <= 3:
                return 25 + minutes * 0.15 * (1 - 0.025)
            else:
                return 25 + minutes * 0.15
        else:
            if times <= 6:
                return 25 + minutes * 0.15 * (1 - 0.03)
            else:
                return 25 + minutes * 0.15
    else:
        return 'Out of range'


def manual_test():
    # 手动测试的函数实现
    print("手动测试：")
    # input minutes and times
    nums = input("Please input minutes and times (e.g. 1 1): ")
    minutes, times = map(int, nums.split())
    # print the result
    print("通话分钟: {}, 不按时缴纳次数: {}, 总价: {}".format(minutes, times, get_total(minutes, times)))


def auto_test():
    # 自动测试的函数实现
    print("自动测试：")
    print("类型1 强一般等价类法")
    minutes = [30, 90, 150, 240, 500]
    times = [1, 2, 3, 4, 8]
    for i in minutes:
        for j in times:
            print("通话分钟: {}, 不按时缴纳次数: {}, 总价: {}".format(i, j, get_total(i, j)))

    print("类型2 决策表法")
    print("通话分钟: 30, 不按时缴纳次数: 1, 总价: {}".format(get_total(30, 1)))
    print("通话分钟: 30, 不按时缴纳次数: 2, 总价: {}".format(get_total(30, 2)))
    print("通话分钟: 90, 不按时缴纳次数: 2, 总价: {}".format(get_total(90, 2)))
    print("通话分钟: 90, 不按时缴纳次数: 3, 总价: {}".format(get_total(90, 3)))
    print("通话分钟: 150, 不按时缴纳次数: 3, 总价: {}".format(get_total(150, 3)))
    print("通话分钟: 150, 不按时缴纳次数: 4, 总价: {}".format(get_total(150, 4)))
    print("通话分钟: 210, 不按时缴纳次数: 3, 总价: {}".format(get_total(210, 3)))
    print("通话分钟: 210, 不按时缴纳次数: 4, 总价: {}".format(get_total(210, 4)))
    print("通话分钟: 350, 不按时缴纳次数: 6, 总价: {}".format(get_total(350, 6)))
    print("通话分钟: 350, 不按时缴纳次数: 11, 总价: {}".format(get_total(350, 11)))


def explain():
    # 解释说明的函数实现
    print('''
本月通话分钟N∈[0,1000]，其中：
- N1={0<=N<=60}
- N2={60<N<=120}
- N3={120<N<=180}
- N4={180<N<=300}
- N5={300<N<=1000}。
不按时缴纳次数M∈{0,1,2,3,4,5,6,7,8}
对本月通话分钟数分别进行五次基本边界值的方法，将每一个变量的对应区间中都分别取min,min+,normal,max-,max，其他变量取正常值，共设计41（9+4*8=41）个测试用例。
等价类法
通话分钟分为以下等价类：
- N1={0<N<=60}
- N2={60<N<=120}
- N3={120<N<=180}
- N4={180<N<=300}
- N5={300<N<=1000}
不按时缴纳次数分为以下等价类：
- M1={0,1}
- M2={2}
- M3={3}
- M4={4,5,6}
- M5={7,8}
采用强一般等价类的方法设计25个测试用例，再补充额外弱健壮等价类测试用例。
决策表法
通话分钟分为以下情况：
- N1={0<N<=60}
- N2={60<N<=120}
- N3={120<N<=180}
- N4={180<N<=300}
- N5={300<N<=1000}
不按时缴纳次数分为以下情况：
- M1={0,1}
- M2={2}
- M3={3}
- M4={4,5,6}
- M5={7,8}
决策表详见文档
''')


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
