import random

from PyQt5 import QtGui, QtCore, QtWidgets


class Slot:

    def __init__(self, size, color, x, y, mean=0):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.mean = mean


class Slots:

    def __init__(self, count, size):

        self.brushes = {
            0: QtGui.QBrush(QtGui.QColor(0xcdc1b4)),
            1: QtGui.QBrush(QtGui.QColor(0x999999)),
            2: QtGui.QBrush(QtGui.QColor(0xeee4da)),
            4: QtGui.QBrush(QtGui.QColor(0xede0c8)),
            8: QtGui.QBrush(QtGui.QColor(0xf2b179)),
            16: QtGui.QBrush(QtGui.QColor(0xf59563)),
            32: QtGui.QBrush(QtGui.QColor(0xf67c5f)),
            64: QtGui.QBrush(QtGui.QColor(0xf65e3b)),
            128: QtGui.QBrush(QtGui.QColor(0xedcf72)),
            256: QtGui.QBrush(QtGui.QColor(0xedcc61)),
            512: QtGui.QBrush(QtGui.QColor(0xedc850)),
            1024: QtGui.QBrush(QtGui.QColor(0xedc53f)),
            2048: QtGui.QBrush(QtGui.QColor(0xedc22e)),
        }

        self.count = count
        self.size = size
        self.slots = [Slot(self.size // self.count, self.brushes[0], i % self.count, i // self.count)
                      for i in range(self.count ** 2)]
        self.empty_slots = [Slot(size // count, self.brushes[0], i % self.count, i // self.count)
                            for i in range(self.count ** 2)]
        self.add_slot()
        self.add_slot()

    def add_slot(self):
        if len(self.empty_slots) == 0:
            return
        if len(self.empty_slots) == 1:
            num = 0
        else:
            num = random.randrange(0, len(self.empty_slots) - 1)
        for i in range(len(self.slots)):
            if self.slots[i].x == self.empty_slots[num].x and self.slots[i].y == self.empty_slots[num].y:
                self.slots[i] = Slot(self.size // self.count, self.brushes[2],
                                     self.empty_slots[num].x, self.empty_slots[num].y, mean = 2)
        self.empty_slots.pop(num)

    def is_game_over(self):
        pass


class Board(QtWidgets.QFrame):

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.slots = Slots(4, 300)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        painter = QtGui.QPainter(self)

        rect = self.contentsRect()

        board_top = rect.bottom() - self.frameGeometry().height()

        for slot in self.slots.slots:
            self.draw_rect(painter, rect.left() + slot.x * slot.size,
                           board_top + slot.y * slot.size, slot.color, slot.size)

    def MakeFlags(self, size):
        flags_table = []
        for i in range(size):
            flags_table.append([True] * size)
        return flags_table

    def DisplayField(self, field):
        size = len(field)
        for i in range(size):
            for j in range(size):
                if field[i][j] // 10 == 0:
                    print(field[i][j], end="    ")
                elif field[i][j] // 100 == 0:
                    print(field[i][j], end="   ")
                elif field[i][j] // 1000 == 0:
                    print(field[i][j], end="  ")
                else:
                    print(field[i][j], end=" ")
            print()

    def MoveUp(self):
        size = 4
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size, size ** 2):
                if self.slots.slots[i].mean == self.slots.slots[i - size].mean and self.slots.slots[i].mean != 0 and flags[i // size - 1][i % size] and flags[i // size][i % size]:
                    flag = True
                    self.slots.slots[i - size].mean = 2 * self.slots.slots[i - size].mean
                    self.slots.slots[i - size].color = self.slots.brushes[self.slots.slots[i - size].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size**2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[i // size][i % size] = False
                    flags[i//size - 1][i % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - size].mean == 0:
                    flag = True
                    self.slots.slots[ i - size].color = self.slots.slots[i].color
                    self.slots.slots[i - size].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])


    def PossibleUp(self, a):
        size = len(a)
        flags = self.MakeFlags(size)
        flag = True
        while (flag):
            flag = False
            for i in range(1, size):
                for j in range(size):
                    if a[i][j] == a[i - 1][j] and flags[i][j] and a[i][j] != 0:
                        return True
                    if a[i - 1][j] == 0 and a[i][j] != 0:
                        return True
        return False

    def MoveLeft(self):
        size = 4
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2 - 1, -1, -1):
                if i % 4 == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i - 1].mean and self.slots.slots[i].mean != 0 and flags[(i - 1) // size][(i - 1) % size] and flags[i // size][i % size]:
                    flag = True
                    self.slots.slots[i - 1].mean = 2 * self.slots.slots[i - 1].mean
                    self.slots.slots[i - 1].color = self.slots.brushes[self.slots.slots[i - 1].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[i // size][i % size] = False
                    flags[(i - 1) // size][(i - 1) % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - 1].mean == 0:
                    flag = True
                    self.slots.slots[i - 1].color = self.slots.slots[i].color
                    self.slots.slots[i - 1].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleLeft(self, a):
        size = len(a)
        flags = self.MakeFlags(size)
        flag = True
        while (flag):
            flag = False
            for i in range(size):
                for j in range(1, size):
                    if a[i][j] == a[i][j - 1] and flags[i][j] and a[i][j] != 0:
                        return True
                    if a[i][j - 1] == 0 and a[i][j] != 0:
                        return True
        return False

    def MoveDown(self):
        size = 4
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2 - size - 1, -1, -1):
                if self.slots.slots[i].mean == self.slots.slots[i + size].mean and self.slots.slots[i].mean != 0 and flags[i // size + 1][i % size] and flags[i // size][i % size]:
                    flag = True
                    self.slots.slots[i + size].mean = 2 * self.slots.slots[i + size].mean
                    self.slots.slots[i + size].color = self.slots.brushes[self.slots.slots[i + size].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[i // size][i % size] = False
                    flags[i // size + 1][i % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i + size].mean == 0:
                    flag = True
                    self.slots.slots[i + size].color = self.slots.slots[i].color
                    self.slots.slots[i + size].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleDown(self, a):
        size = len(a)
        flags = self.MakeFlags(size)
        flag = True
        while (flag):
            flag = False
            for i in range(size - 1):
                for j in range(size):
                    if a[i][j] == a[i + 1][j] and flags[i][j] and a[i][j] != 0:
                        return True
                    if a[i + 1][j] == 0 and a[i][j] != 0:
                        return True
        return False

    def MoveRight(self):
        size = 4
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2 - 1, -1, -1):
                if (i - 3) % 4 == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i + 1].mean and self.slots.slots[i].mean != 0 and flags[(i - 1) // size][(i + 1) % size] and flags[i // size][i % size]:
                    flag = True
                    self.slots.slots[i + 1].mean = 2 * self.slots.slots[i + 1].mean
                    self.slots.slots[i + 1].color = self.slots.brushes[self.slots.slots[i + 1].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[i // size][i % size] = False
                    flags[(i + 1) // size][(i + 1) % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i + 1].mean == 0:
                    flag = True
                    self.slots.slots[i + 1].color = self.slots.slots[i].color
                    self.slots.slots[i + 1].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.brushes[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleRight(self, a):
        size = len(a)
        flags = self.MakeFlags(size)
        flag = True
        fl1 = False
        while (flag):
            flag = False
            for i in range(size):
                for j in range(size - 1):
                    if a[i][j] == a[i][j + 1] and flags[i][j] and a[i][j] != 0:
                        return True
                    if a[i][j + 1] == 0 and a[i][j] != 0:
                        return True
        return False
    def draw_rect(self, painter, x, y, color, size):
        painter.fillRect(x, y, size - 2, size - 2, color)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:

        key = a0.key()

        if key == QtCore.Qt.Key_Left:
            self.MoveLeft()

        if key == QtCore.Qt.Key_Right:
            self.MoveRight()

        if key == QtCore.Qt.Key_Up:
            self.MoveUp()

        if key == QtCore.Qt.Key_Down:
            self.MoveDown()

        self.slots.add_slot()
        self.update()

    def is_game_over(self):
        pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.setGeometry(100, 100, 600, 400)

        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())