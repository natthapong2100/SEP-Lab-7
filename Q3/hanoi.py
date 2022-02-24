from turtle import *
from pole import Pole
from disk import Disk


class Hanoi(object):
    def __init__(self, n=4, start="A", workspace="B", destination="C"):
        self.start_pos = Pole(start, 0, 0)
        self.workspace_pos = Pole(workspace, 150, 0)
        self.destination_pos = Pole(destination, 300, 0)
        self.start_pos.show_pole()
        self.workspace_pos.show_pole()
        self.destination_pos.show_pole()
        for i in range(n):
            self.start_pos.push_disk(
                Disk("d" + str(i), 0, i * 150, 20, (n - i) * 30))

    def move_disk(self, start, destination):
        disk = start.pop_disk()
        destination.push_disk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve(self):
        self.move_tower(6, self.start_pos,
                        self.destination_pos, self.workspace_pos)


if __name__ == "__main__":
    speed(0)
    try:
        h = Hanoi()
        h.solve()
    except IndexError:
        pass
    finally:
        done()