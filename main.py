from threading import Thread
from datetime import datetime
from random import randint
from multiprocessing import Process

def check(students, x, y):
    max_bag_h = 0
    max_bag_w = 0
    max_bag_namber = 0
    check_list = []
    noDocumentList = []
    for i in students:
        if i.size_h > x or i.size_w > y:
            check_list.append(i.id)
            if i.size_h * i.size_w > max_bag_w * max_bag_h:
                max_bag_h = i.size_h
                max_bag_w = i.size_w
                max_bag_namber = i.id
            if i.document == 0:
                noDocumentList.append(i.id)
        else:
            if i.document == 0:
                noDocumentList.append(i.id)
    print('Самая большая сумка: ', max_bag_namber)
    print('Студенты со слишком большими сумками: ', check_list)
    print('Студенты без документа: ', noDocumentList)

class Student:
    def __init__(self, id, document, size_h, size_w):
        self.id = id
        self.document = document
        self.size_h = size_h
        self.size_w = size_w

if __name__ == '__main__':
    students = []
    for i in range(100):
        students.append(Student(i, randint(0, 1), randint(10, 50), randint(10, 50)))

    start1 = datetime.now()
    print("Введите допустимые размеры сумки ")
    x = int(input())
    y = int(input())
    print('Для первого корпуса: ', check(students, x, y))
    print('Для второго корпуса: ', check(students, x, y))
    finish1 = datetime.now() - start1
    print('Время работы 1:', finish1)

    start1 = datetime.now()
    t1 = Thread(target=check, args=(students, x, y))
    t2 = Thread(target=check, args=(students, x, y))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    finish2 = datetime.now() - start1
    print('Время работы 2:', finish2)

    start1 = datetime.now()
    p1 = Process(target=check, args=(students, x, y))
    p2 = Process(target=check, args=(students, x, y))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish3 = datetime.now() - start1
    print('Время работы 3:', finish3)