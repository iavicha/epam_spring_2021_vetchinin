import pytest
from mock import Mock, patch

from homework5.oop_1 import *


@pytest.fixture
def teacher():
    return Teacher("Shadrin", "Daniil")


@pytest.fixture
def student():
    return Student("Petrov", "Roman")


def test_create_teacher(teacher):
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_create_student(student):
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_homework_is_created(teacher):
    homework = teacher.create_homework("Learn functions", 1)
    assert homework.text == "Learn functions"
    assert homework.is_active() is True


def test_homework_deadline():
    homework = Teacher.create_homework("task", 5)
    assert homework.deadline == datetime.timedelta(5)


@pytest.fixture
def outdated_homework():
    return Teacher.create_homework("Learn functions", 1)
