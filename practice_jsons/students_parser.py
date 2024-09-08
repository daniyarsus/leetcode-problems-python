import json


def parse_students(filename: str) -> list[str]:
    students = json.load(open(filename))
    for lesson, info in students['lessons'].items():
        print(f"    Email: {students['studen t_email']}")
        print(f"  {lesson.capitalize()}:")
        print(f"    GPA: {info['gpa']}")
        print(f"    Quantity: {info['quantity']}")


if __name__ == '__main__':
    parse_students("jsons/students.json")
