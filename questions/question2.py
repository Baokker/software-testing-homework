# 2. 万年历问题（用边界值方法分别分析和设计测试用例）。

# 判断两个单独函数 判断年是否为润，判断月是大月，还是小月，还是二月
import datetime

import numpy


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
    # 手动测试的函数实现
    nums = input("请输入年月日，用空格隔开：")
    year, month, day = map(int, nums.split())
    print(f"输入的年月日为：{year}年{month}月{day}日，测试结果为：{get_calender(year, month, day)}")
    pass


def auto_test():
    data = numpy.loadtxt(open("testData/problem_2.csv"), delimiter=",", usecols=[1, 2, 3])
    print("question 2 auto test")
    for data_row in data:
        year = int(data_row[0])
        month = int(data_row[1])
        day = int(data_row[2])
        print("输入的年月日为：%d 年 %d 月 %d 日" % (year,month,day))
        print("测试结果为：" + get_calender(year,month,day))
    # 自动测试的函数实现
    pass


def explain():
    # 解释说明的函数实现
    print("更多的解释说明见作业文档")
    print('''
    本问题输入为年月日，输出为输入的年月日的下一天，格式为xxxx-xx-xx
- 年y(1000<=y<=4000)
- 月m(1<=m<=12)
- 日d(1,3,5,7,8,10,12月：1<=d<=31;4,6,9,11月: 1<=d<=30;闰年2月：1<=d<=29;平年二月：1<=d<=28)
若采用边界值分析，对y、m、d分别取min，min+，normal，max-，max。得到三个取值集合:
- x = [1000, 1001, 3000, 3999, 4000]
- y = [1, 2, 6, 11, 12]
- z = [1, 2, 15, 27, 28, 29, 30, 31]
若增加健壮性分析，对每个集合再分别增加min-,max+，可得:
- x = [999, 1000, 1001, 3000, 3999, 4000, 4001]
- y = [0, 1, 2, 6, 11, 12, 13]
- z = [0, 1, 2, 15, 27, 28, 29, 30, 31, 32]
共有6+6+6*3+1=31个测试用例。''')


if __name__ == "__main__":
    manual_test()
    auto_test()
    explain()
