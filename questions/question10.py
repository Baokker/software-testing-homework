# 10. 万年历问题（等价类方法分别分析和设计测试用例）

# 判断两个单独函数 判断年是否为润，判断月是大月，还是小月，还是二月
import datetime


def year_calculate(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1  # 闰年
    else:
        return 0  # 平年


def month_calculate(month):
    if month == 2:  # 2月
        return 0
    elif month in [4, 6, 9, 11]:  # 小月
        return 1
    else:
        return 2  # 大月


def year_month_day_calculate(year, month, day):
    if month_calculate(month) == 0 and year_calculate(year) == 1:
        if day == 29:
            return 2
        elif day < 29:
            return 1
        else:
            return 0
    elif month_calculate(month) == 0 and year_calculate(year) == 0:
        if day == 28:
            return 2
        elif day < 28:
            return 1
        else:
            return 0
    elif month_calculate(month) == 1:
        if day == 30:
            return 2
        elif day < 30:
            return 1
        else:
            return 0
    else:
        if day == 31:
            return 2
        elif day < 31:
            return 1
        else:
            return 0


def get_calender(year, month, day):
    if year in range(1000, 4000 + 1) and month in range(1, 12 + 1) and day in range(1, 31 + 1):
        if month == 12 and day == 31:
            if year == 4000:
                return 'Out of year'
            else:
                next_date = str(year + 1) + '-1-1'
                date = datetime.datetime.strptime(next_date, '%Y-%m-%d')
                return date.strftime('%Y-%m-%d')
        else:
            if year_month_day_calculate(year, month, day) == 2:
                next_date = str(year) + '-' + str(month + 1) + '-' + str(1)
                date = datetime.datetime.strptime(next_date, '%Y-%m-%d')
                return date.strftime('%Y-%m-%d')

            elif year_month_day_calculate(year, month, day) == 1:
                next_date = str(year) + '-' + str(month) + '-' + str(day + 1)
                date = datetime.datetime.strptime(next_date, '%Y-%m-%d')
                return date.strftime('%Y-%m-%d')
            else:
                return 'Day out of month'
    else:
        return 'Out of range'


def manual_test():
    print("手动测试")
    # input year month and day
    nums = input("请输入年月日，用空格隔开：")
    year, month, day = map(int, nums.split())
    print(f"输入的年月日为：{year}年{month}月{day}日，测试结果为：{get_calender(year, month, day)}")


def auto_test():
    print("自动测试")
    print("采用强一般等价类")
    print("年：Y1={非闰年}，Y2={能被4整除不能被100整除}，Y3={能被400整除}")
    print("月：M1={除12月外的大月份}，M2={小月份}，M3={2月份}，M4={12月}")
    print("日：D1={1~27}，D2={28}，D3={29}，D4={30}，D5={31}")
    print("测试用例：")
    years = [2023, 2020, 2000]
    months = [1, 4, 2, 12]
    days = [1, 28, 29, 30, 31]
    count = 1
    for year in years:
        for month in months:
            for day in days:
                print(f"测试{count} 输入的年月日为：{year}年{month}月{day}日，测试结果为：{get_calender(year, month, day)}")
                count += 1


def explain():
    # 解释说明的函数实现
    print('''
本问题输入为年月日，输出为输入的年月日的下一天，格式为xxxx-xx-xx
将年Y（假设范围为1000-4000年）划分为以下等价类：
- Y1={非闰年}
- Y2={能被4整除不能被100整除}
- Y3={能被400整除}。
月M划分为以下等价类：
- M1={除12月外的大月份}
- M2={小月份}
- M3={2月份}
- M4={12月}。
日D划分为以下等价类：
- D1={1~27}
- D2={28}
- D3={29}
- D4={30}
- D5={31}
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
