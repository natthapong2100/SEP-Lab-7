from turtle import *


class Pole(object):
    def __init__(self, name="", x_pos=0, y_pos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.px_pos = x_pos
        self.py_pos = y_pos
        self.pthick = thick
        self.plength = length

    def show_pole(self):
        left(90)
        penup()
        goto(self.px_pos, self.py_pos)
        pendown()
        rt(90)
        for x in range(2):
            forward(self.pthick/2)
            left(90)
            forward(self.plength)
            left(90)
            forward(self.pthick/2)

    def push_disk(self, disk):
        disk.new_pos(self.px_pos, self.toppos)
        disk.show_disk()
        self.stack.append(disk)
        self.toppos += disk.disk_height
        self.toppos += 1

    def pop_disk(self):
        d = self.stack.pop()
        d.clear_disk()
        self.toppos -= 1
        self.toppos -= d.disk_height
        return d