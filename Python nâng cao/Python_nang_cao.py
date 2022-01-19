from datetime import datetime

class Employee():
    def __init__(self, full_name, name, year_of_birth, position, skills, start_year):
        self.full_name = full_name
        self.name = name
        self.year_of_birth = year_of_birth
        self.position = position
        self.skills = skills
        self.start_year = start_year


class TechEmployee(Employee):
    def __init__(self, full_name, name, year_of_birth, position, skills, start_year, programming_language, projects):
        Employee.__init__(self, full_name, name, year_of_birth, position, skills, start_year)
        self.programming_language = programming_language
        self.projects = projects
        self.start_year = start_year


import os 
def file_read(path):
    if os.path.exists(path) == False:
        raise Exception('File {} not exist'.format(path))

    file = open(path, 'r')
    data = file.read()
    file.close()

    return data


def get_employee_list(list_employee_path):
    data = file_read(list_employee_path)

    lines = data.split('\n')
    lines = lines[1:]

    list_employee = []
    for line in lines:
        full_name, name, year_of_birth, position, skills, start_year = line.split(',')
        name = full_name.split(' ')[-1]
        skills = skills.split('_')
        start_year = int(start_year)

        employee = Employee(full_name, name, year_of_birth, position, skills, start_year)
        list_employee.append(employee)

    return list_employee
    

def get_priority(employee):
    number_of_skills = len(employee.skills)
    year_of_work = 2022 - int(employee.start_year)
    name = employee.name
    full_name = employee.full_name

    return(number_of_skills, year_of_work, name, full_name)


def get_learner_list(list_employee):
    list_learner = list_employee.copy()
    list_learner.sort(key = get_priority, reverse = True)

    return list_learner[:3]

   
def get_tech_employee_list1(list_tech_employee_path):
    data = file_read(list_tech_employee_path)

    lines = data.split('\n')
    lines = lines[1:]

    list_tech_employee = []
    for line in lines:
        full_name, name, year_of_birth, position, skills, start_year, programming_language, projects = line.split(',')
        skills = skills.split('_')
        start_year = int(start_year)
        programming_language = programming_language.split('_')
        projects = projects.split('_')
        tech_team = TechEmployee(full_name, name, year_of_birth, position, skills, start_year, programming_language, projects)

        list_tech_employee.append(tech_team)

    return list_tech_employee


def get_num_of_project(tech_team):
    num_of_project = len(tech_team.projects)
    
    return num_of_project


def get_use_python_list(list_tech_employee):
    employee_use_python = list(filter(lambda x:"Python" in x.programming_language,list_tech_employee))
    employee_use_python.sort(key = get_num_of_project, reverse = True)

    return employee_use_python  


def get_tech_employee_list2(list_tech_employee_path):
    data = file_read(list_tech_employee_path)

    lines = data.split('\n')
    lines = lines[1:]

    list_tech_employee = []
    for line in lines:
        full_name, name, year_of_birth, position, skills, start_year, programming_language, projects = line.split(',')
        skills = skills.split('_')
        start_year = int(start_year)
        programming_language = programming_language.split('_')
        projects = projects.split('_')
        tech_team2 = TechEmployee(full_name, name, year_of_birth, position, skills, start_year, programming_language, projects)

        list_tech_employee.append(tech_team2)

    return list_tech_employee


def get_experienced_employee_list(list_tech_employee):
    employee_from30 = list(filter(lambda x:(2022 - int(x.year_of_birth)) >= 30, list_tech_employee))
    experienced_employee = list(filter(lambda x:len(x.projects) > 5, employee_from30))
    
    return experienced_employee


def print_list1(list_learner):
    print(f"Employees participating in the course: ")
    for em in list_learner:
        print(f"""
        Full Name : {em.full_name}
        YOB : {em.year_of_birth}
        Position : {em.position}
        The number of skills : {len(em.skills)}
        Start year: {em.start_year}
                """)
            
            
list_employee_path = "Employee.txt"
list_employee = get_employee_list(list_employee_path)
list_leaner = get_learner_list(list_employee)

print_list1(list_leaner)


def print_list2(employee_use_python):
    print("Employees use Python and have more projects: ")
    for em in employee_use_python:
        print(f"""
        Full Name : {em.full_name}
        YOB : {em.year_of_birth}
        Position : {em.position}
        Is use Python : {"Python" in em.programming_language}
        The number of projects : {len(em.projects)}
                """)


def print_list3(experienced_employee):
    print("Employees from 30 and have greater 5 projects: ")
    for em in experienced_employee:
        print(f"""
        Full Name : {em.full_name}
        YOB : {em.year_of_birth}
        Position : {em.position}
        The number of projects : {len(em.projects)}
            """)


list_tech_employee_path = "TechEmployee.txt"
list_tech_employee = get_tech_employee_list1(list_tech_employee_path)
employee_use_python = get_use_python_list(list_tech_employee)
list_tech_employee = get_tech_employee_list2(list_tech_employee_path)
experienced_employee = get_experienced_employee_list(list_tech_employee)

print_list2(employee_use_python)
print_list3(experienced_employee)

