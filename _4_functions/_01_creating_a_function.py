import datetime


def greet():
    print("Hello")


greet()
greet()


def show_date_time():
    time: datetime = datetime.datetime.now().time()
    date: datetime = datetime.datetime.now().date()
    print(f"Time : {time:%H:%M:%S}")
    print(f"Date : {date:%d-%m-%y}")


show_date_time()
show_date_time()
