from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

current_date = date.today()
print(f'Текущая дата: {current_date}')
if __name__ == '__main__':
    while True:
        command = input('Введите команду: ')
        if command == 's':
            calculate_salary()
            break
        elif command == 'e':
            get_employees()
            break