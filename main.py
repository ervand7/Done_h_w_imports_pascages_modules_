from applcation import salary
from applcation.db.people import get_employees
import datetime


def print_time():
    print(f'Now the time is {datetime.datetime.now()}')


if __name__ == '__main__':
    print_time()
    salary.calculate_salary()
    get_employees()
