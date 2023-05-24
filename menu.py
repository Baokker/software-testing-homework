from questions import question1, question2, question4, question7, question9, question10, question11, question15, question16, question17

def explain(question_id):
    if question_id == 1:
        question1.explain()
    elif question_id == 2:
        question2.explain()
    elif question_id == 4:
        question4.explain()
    elif question_id == 7:
        question7.explain()
    elif question_id == 9:
        question9.explain()
    elif question_id == 10:
        question10.explain()
    elif question_id == 11:
        question11.explain()
    elif question_id == 15:
        question15.explain()
    elif question_id == 16:
        question16.explain()
    elif question_id == 17:
        question17.explain()
    else:
        print("查不到此问题编号")


def auto_test(question_id):
    if question_id == 1:
        question1.auto_test()
    elif question_id == 2:
        question2.auto_test()
    elif question_id == 4:
        question4.auto_test()
    elif question_id == 7:
        question7.auto_test()
    elif question_id == 9:
        question9.auto_test()
    elif question_id == 10:
        question10.auto_test()
    elif question_id == 11:
        question11.auto_test()
    elif question_id == 15:
        question15.auto_test()
    elif question_id == 16:
        question16.auto_test()
    elif question_id == 17:
        question17.auto_test()
    else:
        print("查不到此问题编号")


def explain(question_id):
    if question_id == 1:
        question1.explain()
    elif question_id == 2:
        question2.explain()
    elif question_id == 4:
        question4.explain()
    elif question_id == 7:
        question7.explain()
    elif question_id == 9:
        question9.explain()
    elif question_id == 10:
        question10.explain()
    elif question_id == 11:
        question11.explain()
    elif question_id == 15:
        question15.explain()
    elif question_id == 16:
        question16.explain()
    elif question_id == 17:
        question17.explain()
    else:
        print("查不到此问题编号")


question_id_list = [1, 2, 4, 7, 9, 10, 11, 15, 16, 17]

def show_menu():
    while True:
        print("请输入数字选择问题（如输入1选择问题1：")
        print("0. 测试全部问题")
        print("1. 判断三角形类型（用边界值分析和设计测试用例）")
        print("2. 万年历问题（用边界值方法分别分析和设计测试用例）")
        print("4. 电脑销售系统")
        print("7. 电信收费问题系统")
        print("9. 判断三角形类型（等价类方法分别分析和设计测试用例）")
        print("10. 万年历问题（用状态转换图设计测试用例）")
        print("11. 万年历问题（用决策表设计测试用例，将年份划分成：非闰年，被4整除不被100整除的闰年和被400整除的闰年）")
        print("15. 设计ATM的系统状态图，设计出逻辑测试用例")
        print("16. 按照C语言程序前的编号，构建起程序图")
        print("17. 销售系统白盒测试")

        try:
            question_id = int(input())

            if question_id == 0:
                for id in question_id_list:
                    print("您选择的问题是：", id)
                    print("本问题解释说明如下：")
                    explain(id)
                    print("本问题自动测试如下：")
                    auto_test(id)

            if question_id not in question_id_list:
                print("输入错误，请重新选择！")
                continue

            print("您选择的问题是：", question_id)
            print("请输入数字选择测试方式")
            print("1. 手动测试")
            print("2. 自动测试")
            print("3. 解释说明")
            print("4. 返回上一级菜单")

            test_type = int(input())
            print("您选择的测试方式是：", test_type)

            if test_type == 1:
                explain(question_id)
            elif test_type == 2:
                auto_test(question_id)
            elif test_type == 3:
                explain(question_id)
            elif test_type == 4:
                continue
            else:
                print("输入错误，请重新选择！")
            
        except ValueError:
            print("输入错误，请重新选择！")

show_menu()