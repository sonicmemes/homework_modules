import datetime
import application.salary as salary
import application.db.people as people

if __name__ == '__main__':
    print(datetime.date.today())
    salary.calculate_salary()
    people.get_employees()
    
