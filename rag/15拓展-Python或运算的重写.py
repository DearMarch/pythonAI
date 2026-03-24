
class Test(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return MySequence(self, other)

    def __str__(self):
        return self.name


class MySequence(object):
    def __init__(self, *args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)

    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):
        for item in self.sequence:
            print(item)


if __name__ == '__main__':
    t1 = Test('t1')
    t2 = Test('t2')
    t3 = Test('t3')
    t4 = Test('t4')
    t5 = Test('t5')
    t6 = Test('t6')
    t7 = Test('t7')
    t8 = Test('t8')
    t9 = Test('t9')
    t10 = Test('t10')

    t = t1 | t2 | t3 | t4 | t5 | t6 | t7 | t8 | t9 | t10
    t.run()
