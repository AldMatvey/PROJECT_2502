
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
import sys
import random
'''
def sum2d(arr):
    summ = 0
    for i in range(len(arr)):
        summ += sum(arr[i])
    return summ




class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top = 150
        self.left = 150
        self.width = 800
        self.height = 800
        MAX_HEIGHT = 256

        # heighs generation

        ysize = 500
        xsize = 500
        heighs = np.zeros((xsize, ysize))
        for i in range(xsize):
            for j in range(ysize):
                heighs[i][j] = random.randint(0, MAX_HEIGHT)
        heighs_output = np.zeros((xsize, ysize))
        for k in range(30):
            for i in range(xsize):
                for j in range(ysize):
                    heighs_output[i][j] = (heighs[i][j] * 10 + (
                            heighs[i - 1][j] + heighs[i - 1][j - 1] + heighs[i - 1][(j + 1) % ysize] + heighs[i][
                        (j + 1) % ysize] +
                            heighs[(i + 1) % xsize][(j + 1) % ysize] + heighs[(i + 1) % xsize][j] +
                            heighs[(i + 1) % xsize][j - 1] + heighs[i][j - 1] +
                            heighs[(i + 1) % xsize][j - 2] + heighs[i - 1][j - 2] + heighs[i][j - 2] +
                            heighs[(i + 1) % xsize][(j + 2) % ysize] +
                            heighs[i][(j + 2) % ysize] + heighs[i - 1][(j + 2) % ysize] + heighs[i - 2][j - 1] +
                            heighs[i - 2][j] +
                            heighs[i - 2][(j + 1) % ysize] + heighs[(i + 2) % xsize][j - 1] +
                            heighs[(i + 2) % xsize][j] +
                            heighs[(i + 2) % xsize][(j + 1) % ysize]) * 2 + heighs[i - 3][j] + heighs[i - 3][
                                               j - 1] + heighs[i - 3][(j + 1) % ysize] +
                                           heighs[i - 2][j - 2] + heighs[i - 1][j - 3] + heighs[i][j - 3] +
                                           heighs[(i + 1) % xsize][j - 3] +
                                           heighs[(i + 2) % xsize][j - 2] + heighs[(i + 3) % xsize][j - 1] +
                                           heighs[(i + 3) % xsize][j] + heighs[(i + 3) % xsize][(j + 1) % ysize] +
                                           heighs[(i + 2) % xsize][(j + 2) % ysize] + heighs[(i + 1) % xsize][
                                               (j + 3) % ysize] + heighs[i][(j + 3) % ysize] +
                                           heighs[i - 1][(j + 3) % ysize] + heighs[i - 2][(j + 2) % ysize]) // 65.4
            heighs, heighs_output = heighs_output, heighs
        mn = 1000
        for i in range(xsize):
            for j in range(ysize):
                if mn > heighs_output[i][j]:
                    mn = heighs_output[i][j]
        for i in range(xsize):
            for t in range(ysize):
                heighs_output[i][t] -= mn
        self.heights = heighs_output

        # temperature generation

        temps = np.zeros((xsize, ysize))
        for i in range(xsize):
            for j in range(ysize):
                temps[i][j] = random.randint(0, 5)
        temps_output = np.zeros((xsize, ysize))
        for k in range(30):
            for i in range(xsize):
                for j in range(ysize):
                    temps_output[i][j] = (temps[i][j] * 10 + (
                            temps[i - 1][j] + temps[i - 1][j - 1] + temps[i - 1][(j + 1) % ysize] +
                            temps[i][(j + 1) % ysize] +
                            temps[(i + 1) % xsize][(j + 1) % ysize] + temps[(i + 1) % xsize][j] +
                            temps[(i + 1) % xsize][j - 1] + temps[i][j - 1] +
                            temps[(i + 1) % xsize][j - 2] + temps[i - 1][j - 2] + temps[i][j - 2] +
                            temps[(i + 1) % xsize][(j + 2) % ysize] +
                            temps[i][(j + 2) % ysize] + temps[i - 1][(j + 2) % ysize] + temps[i - 2][j - 1] +
                            temps[i - 2][j] +
                            temps[i - 2][(j + 1) % ysize] + temps[(i + 2) % xsize][j - 1] +
                            temps[(i + 2) % xsize][j] +
                            temps[(i + 2) % xsize][(j + 1) % ysize]) * 2 + temps[i - 3][j] + temps[i - 3][
                                               j - 1] + temps[i - 3][(j + 1) % ysize] +
                                           temps[i - 2][j - 2] + temps[i - 1][j - 3] + temps[i][j - 3] +
                                           temps[(i + 1) % xsize][j - 3] +
                                           temps[(i + 2) % xsize][j - 2] + temps[(i + 3) % xsize][j - 1] +
                                           temps[(i + 3) % xsize][j] + temps[(i + 3) % xsize][(j + 1) % ysize] +
                                           temps[(i + 2) % xsize][(j + 2) % ysize] + temps[(i + 1) % xsize][
                                               (j + 3) % ysize] + temps[i][(j + 3) % ysize] +
                                           temps[i - 1][(j + 3) % ysize] + temps[i - 2][(j + 2) % ysize]) // 52.8
            temps, temps_output = temps_output, temps
        mn = 1000
        for i in range(xsize):
            for j in range(ysize):
                if mn > temps_output[i][j]:
                    mn = temps_output[i][j]

        for i in range(xsize):
            for t in range(ysize):
                temps_output[i][t] -= mn
                if temps_output[i][t] >= 81:
                    temps_output[i][t] = 2
                elif 10 <= temps_output[i][t] <= 80:
                    temps_output[i][t] = 1
                else:
                    temps_output[i][t] = 0
        print(temps_output[0][0])
        self.temps = temps_output




        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):

            #low temperature

        textures = [[[165, 242, 243, 255], [165, 242, 243, 255], [165, 242, 243, 255], [165, 242, 243, 255],
                            [165, 242, 243, 255],
                            [165, 242, 243, 255], [165, 242, 243, 255], [165, 242, 243, 255], [165, 242, 243, 255],
                            [165, 242, 243, 255],
                            [165, 242, 243, 255], [165, 242, 243, 255], [203, 199, 183, 255], [228, 228, 228, 255],
                            [228, 228, 228, 255],
                            [235, 235, 235, 255], [235, 235, 235, 255], [11, 70, 44, 255], [11, 70, 44, 255],
                            [86, 86, 85, 255], [86, 86, 85, 255],
                            [86, 86, 85, 255], [68, 68, 64, 255], [68, 68, 64, 255], [68, 68, 64, 255],
                            [240, 255, 255, 255], [240, 255, 255, 255],
                            [255, 250, 250, 255], [255, 250, 250, 255], [255, 250, 250, 255], [255, 250, 250, 255],
                            [255, 250, 250, 255]],

            #middle temperature


                            [[0, 84, 147, 255], [0, 84, 147, 255], [0, 84, 147, 255], [0, 84, 147, 255],
                            [14, 151, 255, 255],
                            [14, 151, 255, 255], [14, 151, 255, 255], [136, 203, 255, 255], [136, 203, 255, 255],
                            [136, 203, 255, 255],
                            [136, 203, 255, 255], [136, 203, 255, 255], [242, 226, 166, 255], [12, 218, 81, 255],
                            [12, 218, 81, 255],
                            [65, 163, 23, 255], [65, 163, 23, 255], [56, 124, 44, 255], [56, 124, 44, 255],
                            [86, 86, 85, 255], [86, 86, 85, 255],
                            [86, 86, 85, 255], [68, 68, 64, 255], [68, 68, 64, 255], [68, 68, 64, 255],
                            [240, 255, 255, 255], [240, 255, 255, 255],
                            [255, 250, 250, 255], [255, 250, 250, 255], [255, 250, 250, 255], [255, 250, 250, 255],
                            [255, 250, 250, 255]],

            #high temperature

                            [[0, 84, 147, 255], [0, 84, 147, 255], [0, 84, 147, 255], [0, 84, 147, 255],
                            [14, 151, 255, 255],
                            [14, 151, 255, 255], [14, 151, 255, 255], [136, 203, 255, 255], [136, 203, 255, 255],
                            [136, 203, 255, 255],
                            [136, 203, 255, 255], [136, 203, 255, 255], [242, 226, 166, 255], [255, 221, 82, 255],
                            [255, 221, 82, 255],
                            [255, 215, 53, 255], [255, 215, 53, 255], [229, 183, 0, 255], [229, 183, 0, 255],
                            [86, 86, 85, 255], [86, 86, 85, 255],
                            [86, 86, 85, 255], [68, 68, 64, 255], [68, 68, 64, 255], [68, 68, 64, 255],
                            [240, 255, 255, 255], [240, 255, 255, 255],
                            [255, 250, 250, 255], [255, 250, 250, 255], [255, 250, 250, 255], [255, 250, 250, 255],
                            [255, 250, 250, 255]]]
        xsize = len(self.heights)
        ysize = len(self.heights[0])
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        for i in range(xsize):
            for j in range(ysize):
                painter.setBrush(QBrush(QColor(textures[int(self.temps[i][j])][int(self.heights[i][j])][0], textures[int(self.temps[i][j])][int(self.heights[i][j])][1],
                                           textures[int(self.temps[i][j])][int(self.heights[i][j])][2], textures[int(self.temps[i][j])][int(self.heights[i][j])][3]), Qt.SolidPattern))
                painter.setPen(QPen(QColor(textures[int(self.temps[i][j])][int(self.heights[i][j])][0], textures[int(self.temps[i][j])][int(self.heights[i][j])][1],
                                           textures[int(self.temps[i][j])][int(self.heights[i][j])][2], textures[int(self.temps[i][j])][int(self.heights[i][j])][3]), 0, Qt.SolidLine))
                painter.drawRect(i * 4, j * 4, 4, 4)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
'''
'''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 1111, 581))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(749, 589, 361, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.color_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.color_pushButton.setObjectName("color_pushButton")
        self.verticalLayout.addWidget(self.color_pushButton)
        self.font_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.font_pushButton.setObjectName("font_pushButton")
        self.verticalLayout.addWidget(self.font_pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionSave_as)
        self.menu.addAction(self.actionOpen)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.color_pushButton.setText(_translate("MainWindow", "color"))
        self.font_pushButton.setText(_translate("MainWindow", "font"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 
'''
"""
from PyQt5 import QtGui, QtCore, QtWidgets
import random as rnd

class Snake:

    def __init__(self, width, height):
        self.body = [[5, 10], [5, 11]]
        self.head = self.body[0]

        self.direction = 'left'
        self.grow = False
        self.color = QtGui.QColor(0x538846)

        self.width = width
        self.height = height

    def is_dead(self):
        pass


    def move(self):

        if self.direction == 'left':
            self.head = [self.head[0] - 1, self.head[1]]

            if self.head[0] == -1:
                self.head[0] = self.width - 1

        if self.direction == 'right':
            self.head = [self.head[0] + 1, self.head[1]]

            if self.head[0] == self.width:
                self.head[0] = -1

        if self.direction == 'up':
            self.head = [self.head[0], self.head[1] - 1]

            if self.head[1] == -1:
                self.head[1] = self.height - 1

        if self.direction == 'down':
            self.head = [self.head[0], self.head[1] + 1]

            if self.head[1] == self.height:
                self.head[1] = -1

        self.body.insert(0, self.head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

class Food:
    COLOR = [QtGui.QColor(0xcb3333), QtGui.QColor(0xf30a66), QtGui.QColor(0x5188c4)]

    def __init__(self, width, height):
        self.bag = []

        self.width = width
        self.height = height

    def drop(self):
        random.seed(random.randint(10, 40))

        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        color = random.randint(0, len(Food.COLOR) - 1)

        self.bag.append({'coord': [x, y], 'color': Food.COLOR[color]})


class Board(QtWidgets.QFrame):
    SPEED = 80

    HEIGHTINBLOCKS = 40
    WIDTHINBLOCKS = 60

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.timer = QtCore.QBasicTimer()

        self.snake = Snake(Board.WIDTHINBLOCKS, Board.HEIGHTINBLOCKS)
        self.food = Food(Board.WIDTHINBLOCKS, Board.HEIGHTINBLOCKS)

    def block_width(self):
        return self.frameGeometry().width() / Board.WIDTHINBLOCKS

    def block_height(self):
        return self.frameGeometry().height() / Board.HEIGHTINBLOCKS

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        painter = QtGui.QPainter(self)

        rect = self.contentsRect()

        boardtop = rect.bottom() - self.frameGeometry().height()

        for cord in self.snake.body:
            self.drawrect(painter, rect.left() + cord[0] * self.block_width(),
                          boardtop + cord[1] * self.block_height(), self.snake.color)
        for fruit in self.food.bag:
            cord = fruit['coord']
            self.drawrect(painter, rect.left() + cord[0] * self.block_width(), boardtop + cord[1] * self.block_height(), fruit['color'])

    def drawrect(self, painter, x, y, color):
        painter.fillRect(int(x), int(y), int(self.block_width() - 2), int(self.block_height() - 2), color)

    def timerEvent(self, a0: QtCore.QTimerEvent) -> None:

        if a0.timerId() == self.timer.timerId():
            self.snake.move()
            self.collision()
            self.drop()
            self.update()

    def collision(self):
        for fruit in self.food.bag:
            if fruit['coord'] == self.snake.head:
                self.snake.grow = True
                self.food.bag.remove(fruit)
                break
    def drop(self):
        if len(self.food.bag) == 0:
            self.food.drop()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:

        key = a0.key()

        if key == QtCore.Qt.Key.Key_Left:
            if self.snake.direction != 'right':
                self.snake.direction = 'left'

        if key == QtCore.Qt.Key.Key_Right:
            if self.snake.direction != 'left':
                self.snake.direction = 'right'

        if key == QtCore.Qt.Key.Key_Up:
            if self.snake.direction != 'down':
                self.snake.direction = 'up'

        if key == QtCore.Qt.Key.Key_Down:
            if self.snake.direction != 'up':
                self.snake.direction = 'down'


    def is_dead(self):
        pass

    def start(self):
        self.timer.start(Board.SPEED, self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.setGeometry(100, 100, 600, 400)
        self.board.start()

        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
"""

import random

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap

class Slot:

    def __init__(self, size, color, x, y, mean=0):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.mean = mean


class Slots:
    def __init__(self, count, size):

        self.pictures = {
            0: QtGui.QImage('Pics/empty.jpg'),
            1: QtGui.QImage('Pics/obeme.jpeg'),
            2: QtGui.QImage('Pics/2(another kasatkin).png'),
            4: QtGui.QImage('Pics/4(spider_man).png'),
            8: QtGui.QImage('Pics/8(kasatkin).png'),
            16: QtGui.QImage('Pics/16(kozel).png'),
            32: QtGui.QImage('Pics/32(mish).png'),
            64: QtGui.QImage('Pics/64(chich).png'),
            128: QtGui.QImage('Pics/128(bour).png'),
            256: QtGui.QImage('Pics/256(stremich).png'),
            512: QtGui.QImage('Pics/512(koval).png'),
            1024: QtGui.QImage('Pics/1024(zhivotov).png'),
            2048: QtGui.QImage('Pics/obeme.jpeg'),
        }

        self.count = count
        self.size = size
        self.slots = [Slot(self.size // self.count, self.pictures[0], i % self.count, i // self.count)
                      for i in range(self.count ** 2)]
        self.empty_slots = [Slot(size // count, self.pictures[0], i % self.count, i // self.count)
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
                self.slots[i] = Slot(self.size // self.count, self.pictures[2],
                                     self.empty_slots[num].x, self.empty_slots[num].y, mean = 2)
        self.empty_slots.pop(num)

    def is_game_over(self):
        pass


class Board(QtWidgets.QFrame):

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.slots = Slots(4, 900)

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
                    self.slots.slots[i - size].color = self.slots.pictures[self.slots.slots[i - size].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.pictures[0]
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
                    self.slots.slots[i].color = self.slots.pictures[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])


    def PossibleUp(self):
        flag = True
        size = 4
        while (flag):
            flag = False
            for i in range(size, size ** 2):
                if self.slots.slots[i].mean == self.slots.slots[i - size].mean and self.slots.slots[i].mean != 0:
                    return True
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - size].mean == 0:
                    return True
        return False

    def MoveLeft(self):
        size = 4
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2):
                if i % 4 == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i - 1].mean and self.slots.slots[i].mean != 0 and flags[(i - 1) // size][(i - 1) % size] and flags[i // size][i % size]:
                    flag = True
                    self.slots.slots[i - 1].mean = 2 * self.slots.slots[i - 1].mean
                    self.slots.slots[i - 1].color = self.slots.pictures[self.slots.slots[i - 1].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.pictures[0]
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
                    self.slots.slots[i].color = self.slots.pictures[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleLeft(self):
        size = 4
        flag = True
        while (flag):
            flag = False
            for i in range(size ** 2 - 1, -1, -1):
                if i % 4 == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i - 1].mean and self.slots.slots[i].mean != 0:
                    return True
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - 1].mean == 0:
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
                    self.slots.slots[i + size].color = self.slots.pictures[self.slots.slots[i + size].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.pictures[0]
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
                    self.slots.slots[i].color = self.slots.pictures[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleDown(self):
        size = 4
        flag = True
        while (flag):
            flag = False
            for i in range(size ** 2 - size - 1, -1, -1):
                if self.slots.slots[i].mean == self.slots.slots[i + size].mean and self.slots.slots[i].mean != 0:
                    return True
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i + size].mean == 0:
                    return True
        return False

    def MoveRight(self):
        size = 4
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2):
                if (i - 3) % 4 == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i + 1].mean and self.slots.slots[i].mean != 0 and flags[(i - 1) // size][(i + 1) % size] and flags[i // size][i % size]:
                    flag = True
                    self.slots.slots[i + 1].mean = 2 * self.slots.slots[i + 1].mean
                    self.slots.slots[i + 1].color = self.slots.pictures[self.slots.slots[i + 1].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].color = self.slots.pictures[0]
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
                    self.slots.slots[i].color = self.slots.pictures[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleRight(self):
        size = 4
        flag = True
        while (flag):
            flag = False
            for i in range(size ** 2 - 1, -1, -1):
                if (i - 3) % 4 == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i + 1].mean and self.slots.slots[i].mean != 0:
                    return True
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i + 1].mean == 0:
                    return True
        return False
    def draw_rect(self, painter, x, y, color, size):
        rect = QtCore.QRect(x, y, size - 2, size - 2)
        painter.drawImage(rect, color)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:

        key = a0.key()
        success_move = False
        if self.is_game_over():
            msgBox = QMessageBox()
            msgBox.setText("YOU LOST!!")
            msgBox.setWindowTitle("GG")
        if key == QtCore.Qt.Key_Left:
            if self.PossibleLeft():
                self.MoveLeft()
                success_move = True

        if key == QtCore.Qt.Key_Right:
            if self.PossibleRight():
                self.MoveRight()
                success_move = True

        if key == QtCore.Qt.Key_Up:
            if self.PossibleUp():
                self.MoveUp()
                success_move = True

        if key == QtCore.Qt.Key_Down:
            if self.PossibleDown():
                self.MoveDown()
                success_move = True
        if success_move:
            self.slots.add_slot()
        self.update()

    def is_game_over(self):
        if (self.PossibleLeft() or self.PossibleUp() or self.PossibleDown() or self.PossibleRight()) == False:
            return True
        return False


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.setGeometry(500, 50, 900, 900)
        self.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
