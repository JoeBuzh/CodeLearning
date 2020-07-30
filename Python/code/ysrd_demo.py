# -*- coding: utf-8 -*-

import os
from datetime import datetime, timedelta


class Ysrd:
    """
        YSRD.
    """
    # class attr
    work_location = "FengTai"
    name = 'YSRD'

    # init
    def __init__(self, owner):
        self.name = cls.name
        self.owner = owner

    @classmethod
    def show(cls):
        print("We are {}, we work at {}".format(cls.name, cls.work_location))

    @staticmethod
    def annance(product: str):
        print("We are declear that the {} was invented by us!".format(product))



class Qhcg(Ysrd):
    work_location = 'HuaiRou'
    name = 'QHCG'

    def __init__(self, owner, building):
        self.building = building

    @staticmethod
    def annance(product: str, num: int):
        print("We have invented {} and produced with a scala of {} every day.".format(
            product, num)
        )


class Employee:
    """
        Employee.
    """
    jx = 1.1

    def __init__(self, name, company: object, age, skill):
        self.name = name
        self.age = age
        self.skill = skill
        self.company = company

    def _intro(self):
        print("My name is {}, I'm {}, and skilled at {}, glad to meet you at {}".format(
            self.name, self.age, self.skill, self.company)
        )

    @classmethod
    def update_jx(cls, new_jx: int):
        cls.jx = new_jx

    @staticmethod
    def work_day():
        print(datetime.now().date())


def main():
    qhcg = Qhcg('tianqm', 'science city')
    qhcg.show()
    qhcg.annance('智能温度计', 5000)
    zhangs = Employee('张三', qhcg, 22, 'DataAnalysis')
    zhangs.work_day()
    zhangs.update_jx(1.5)
    print(zhangs.jx)


if __name__ == '__main__':
    main()

        