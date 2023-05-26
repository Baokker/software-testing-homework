# 4. 电脑销售系统

def get_total_value(host, screen, equipment):
    if get_range(host, screen, equipment) == 'Calculate total':
        return host * 70 + screen * 30 + equipment * 45
    elif get_range(host, screen, equipment) == 'Out of range':
        return 'Out of range'
    else:
        return host * 25 + screen * 30 + equipment * 45


def get_range(host, screen, equipment):
    if host == -1 and screen in range(1, 80 + 1) and equipment in range(1, 90 + 1):
        return 'Calculate total'
    elif host in range(1, 70 + 1) and screen in range(1, 80 + 1) and equipment in range(1, 90 + 1):
        return 'In range'
    else:
        return 'Out of range'


def get_commission(host, screen, equipment):
    if get_range(host, screen, equipment) == 'Out of range':
        return 'Out of range'
    else:
        basic = get_total_value(host, screen, equipment)
        if basic <= 1000:
            return '{:g}'.format(basic * 0.1)
        elif basic <= 1800:
            return '{:g}'.format(basic * 0.15)
        else:
            return '{:g}'.format(basic * 0.2)


def manual_test():
    print("手动测试：")
    # input host, screen and equipment
    nums = input("Please input host, screen and equipment (e.g. 1 1 1): ")
    host, screen, equipment = map(int, nums.split())
    # print the result
    print("主机: {}, 显示器: {}, 外设: {}, 总价: {}, 佣金: {}".format(host, screen, equipment,
                                                                      get_total_value(host, screen, equipment),
                                                                      get_commission(host, screen, equipment)))


def auto_test():
    print("自动测试：")
    hosts = [0, 1, 2, 40, 69, 70, 71]
    normal_host = 40
    screen = [0, 1, 2, 40, 79, 80, 81]
    normal_screen = 40
    equipment = [0, 1, 2, 40, 89, 90, 91]
    normal_equipment = 40
    for host in hosts:
        print("主机: {}, 显示器: {}, 外设: {}, 总价: {}, 佣金: {}".format(host, normal_screen, normal_equipment,
                                                                          get_total_value(host, normal_screen,
                                                                                          normal_equipment),
                                                                          get_commission(host, normal_screen,
                                                                                         normal_equipment)))
    for screen in screen:
        print("主机: {}, 显示器: {}, 外设: {}, 总价: {}, 佣金: {}".format(normal_host, screen, normal_equipment,
                                                                          get_total_value(normal_host, screen,
                                                                                          normal_equipment),
                                                                          get_commission(normal_host, screen,
                                                                                         normal_equipment)))
    for equipment in equipment:
        print("主机: {}, 显示器: {}, 外设: {}, 总价: {}, 佣金: {}".format(normal_host, normal_screen, equipment,
                                                                          get_total_value(normal_host, normal_screen,
                                                                                          equipment),
                                                                          get_commission(normal_host, normal_screen,
                                                                                         equipment)))
    print("主机: {}, 显示器: {}, 外设: {}, 总价: {}, 佣金: {}".format(-1, 75, 85, get_total_value(-1, 75, 85),
                                                                      get_commission(-1, 75, 85)))


def explain():
    # 解释说明的函数实现
    print("解释说明：")
    print('''
在本题中，测试用例的输入变量有
- 主机销售数量(1<=x<=70)
- 显示器销售数量(1<=y<=80)
- 外设销售数量(1<=z<=90)
测试输出有
- 员工佣金
- 员工本月销售总额
若采用边界值分析，对x、y、z分别取min，min+，normal，max-，max。得到三个取值集合:
- x = [1, 2, 40, 69, 70]
- y = [1, 2, 40, 79, 80]
- z = [1, 2, 40, 89, 90]
若增加健壮性分析，对每个集合再分别增加min-,max+，可得:
- x = [0, 1, 2, 40, 69, 70, 71]
- y = [0, 1, 2, 40, 79, 80, 81]
- z = [0, 1, 2, 40, 89, 90, 91]
共有6*3+1=19个测试用例,再加上当x=-1时输出员工当月销售总额，所以共有20个测试用例。
    ''')


if __name__ == "__main__":
    manual_test()
    auto_test()
    explain()
