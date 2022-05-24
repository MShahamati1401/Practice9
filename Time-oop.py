class Time:
    hours = None
    minutes = None
    second = None
    time_second = None

    def __init__(self):
        self.hours = int(input('Please Inter  Time Hours:')) * 3600
        self.minutes = int(input('Please Inter  Time Minutes:')) * 60
        self.second = int(input('Please Inter  Time Second:'))
        self.time_second = self.hours + self.minutes + self.second


class Result_time:
    op = None
    time_second_f = None
    hours_f = None
    minutes_f = None
    second_f = None

    def get_op(self):
        self.op = input('Please Inter Operator: ')

    def show_time(time):
        Result_time.hours_f = time // 3600
        time = time % 3600
        Result_time.minutes_f = time // 60
        time = time % 60
        Result_time.second_f = time
        print(f'Time: {Result_time.hours_f} : {Result_time.minutes_f} : {Result_time.second_f}')

    def menu_time():
        print('1- Sum two time "+"')
        print('2- subtract two time "-"')
        print('3- Show Time based on seconds: ')
        print('4- Show Time Format H:M:S ')
        get_op = input('Please Select Operator')
        return get_op

    def sum_time():
        output = Time_1.time_second + Time_2.time_second
        Result_time.show_time(output)

    def subtract_time():
        output = Time_1.time_second - Time_2.time_second
        Result_time.show_time(output)


op = Result_time.menu_time()

if op != '4':
    Time_1 = Time()
else:
    get_second = int(input('Please Inter Time based on seconds:'))
    Result_time.show_time(get_second)

if op == '+' or op == '1':
    Time_2 = Time()
    Result_time.sum_time()

if op == '-' or op == '2':
    Time_2 = Time()
    Result_time.subtract_time()

if op == '3':
    print(f'Time based on seconds: {Time_1.time_second}')

