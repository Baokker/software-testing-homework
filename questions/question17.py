# 17. 销售系统白盒测试
def manual_test():
    # 手动测试的函数实现
    pass


def auto_test():
    # 自动测试的函数实现
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
