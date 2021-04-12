"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

import datetime


class Student:
    """
        Атрибуты:
        last_name
        first_name
    Методы:
        do_homework - принимает объект Homework и возвращает его же,
        если задание уже просрочено, то печатет 'You are late' и возвращает None
    """

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework):
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return None


class Teacher:
    """
        Атрибуты:
         last_name
         first_name
    Методы:
        create_homework - текст задания и количество дней на это задание,
        возвращает экземпляр Homework
        Обратите внимание, что для работы этого метода не требуется сам объект.
    """

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, days):
        self.text = text
        self.days = days
        return Homework(text, days)


class Homework:
    """
        Атрибуты:
        text - текст задания
        deadline - хранит объект datetime.timedelta с количеством
        дней на выполнение
        created - c точной датой и временем создания
    Методы:
        is_active - проверяет не истекло ли время на выполнение задания,
        возвращает boolean
    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.date.today()

    def is_active(self):
        if self.created + self.deadline <= datetime.date.today():
            return True
        else:
            return False


if __name__ == "__main__":
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    print(teacher.last_name)  # Daniil
    print(student.first_name)  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
