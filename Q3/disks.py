from turtle import *


class Disk(object):
    def __init__(self, name="", x_pos=0, y_pos=0, height=20, width=40):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.disk_height = height
        self.disk_width = width

    def show_disk(self):
        left(90)
        penup()
        goto(self.x_pos, self.y_pos)
        pendown()
        rt(90)
        for x in range(2):
            forward(self.disk_width/2)
            left(90)
            forward(self.disk_height)
            left(90)
            forward(self.disk_width/2)

    def new_pos(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def clear_disk(self):
        pencolor("white")
        self.show_disk()
        pencolor("black")