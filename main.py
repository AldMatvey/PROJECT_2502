import random

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider, QLabel, QLineEdit, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtGui import QPixmap, QPainter, QPen, QBrush, QColor
from PIL import Image, ImageFont, ImageDraw
import webbrowser
import os

class Slot:

    def __init__(self, size, image, x, y, mean=0):
        self.size = size
        self.image = image
        self.x = x
        self.y = y
        self.mean = mean


class Slots:
    def __init__(self, count, size):

        self.images = {
            0: QtGui.QImage('pics_2502/bg.png'),
            1: QtGui.QImage('pics_2502/obeme.jpeg'),
            2: QtGui.QImage('pics_2502/2.png'),
            4: QtGui.QImage('pics_2502/4.png'),
            8: QtGui.QImage('pics_2502/8.png'),
            16: QtGui.QImage('pics_2502/16.png'),
            32: QtGui.QImage('pics_2502/32.png'),
            64: QtGui.QImage('pics_2502/64.png'),
            128: QtGui.QImage('pics_2502/128.png'),
            256: QtGui.QImage('pics_2502/256.png'),
            512: QtGui.QImage('pics_2502/512.png'),
            1024: QtGui.QImage('pics_2502/1024.png'),
            2048: QtGui.QImage('pics_2502/2048.png'),
            4096: QtGui.QImage('pics_2502/4096.png'),
            8192: QtGui.QImage('pics_2502/8192.png'),
        }

        self.count = count
        self.size = size
        self.slots = [Slot(self.size // self.count, self.images[0], i % self.count, i // self.count)
                      for i in range(self.count ** 2)]
        self.empty_slots = [Slot(size // count, self.images[0], i % self.count, i // self.count)
                            for i in range(self.count ** 2)]
        self.add_slot()
        self.add_slot()

    def add_slot(self):
        two_or_four = random.randint(0, 10)
        if two_or_four > 8:
            newslot = 4
        else:
            newslot = 2
        if len(self.empty_slots) == 1:
            num = 0
        else:
            num = random.randrange(0, len(self.empty_slots) - 1)
        for i in range(len(self.slots)):
            if self.slots[i].x == self.empty_slots[num].x and self.slots[i].y == self.empty_slots[num].y:
                self.slots[i] = Slot(self.size // self.count, self.images[newslot],
                                     self.empty_slots[num].x, self.empty_slots[num].y, mean=newslot)
        self.empty_slots.pop(num)


class Board(QtWidgets.QFrame):
    def __init__(self, parent, diam):
        super(Board, self).__init__(parent)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.score = 0
        self.slots = Slots(diam, 840)


    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        painter = QtGui.QPainter(self)

        rect = self.contentsRect()

        board_top = rect.bottom() - self.frameGeometry().height()

        for slot in self.slots.slots:
            self.draw_rect(painter, rect.left() + slot.x * slot.size,
                           board_top + slot.y * slot.size, slot.image, slot.size)
        painter.setBrush(QtGui.QColor(0x282828))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRoundedRect(900, 15, 200, 100, 10.0, 10.0)
        painter.setPen(QtGui.QPen(QtGui.QColor(0xC83246)))
        painter.setFont(QtGui.QFont('Arial', 9))
        painter.drawText(QtCore.QRectF(900, 5, 200, 50), "SCORE",
                         QtGui.QTextOption(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter))
        painter.setFont(QtGui.QFont('Arial', 22))
        painter.drawText(QtCore.QRectF(900, 45, 200, 70), str(self.score),
                         QtGui.QTextOption(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter))

    def MakeFlags(self, size):
        flags_table = []
        for i in range(size):
            flags_table.append([True] * size)
        return flags_table

    def MoveUp(self):
        size = self.slots.count
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size, size ** 2):
                if self.slots.slots[i].mean == self.slots.slots[i - size].mean and self.slots.slots[i].mean != 0 and \
                        flags[i // size - 1][i % size] and flags[i // size][i % size]:
                    flag = True
                    self.score += 2 * self.slots.slots[i].mean
                    self.slots.slots[i - size].mean = 2 * self.slots.slots[i - size].mean
                    self.slots.slots[i - size].image = self.slots.images[self.slots.slots[i - size].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[i // size - 1][i % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - size].mean == 0:
                    flag = True
                    self.slots.slots[i - size].image = self.slots.slots[i].image
                    self.slots.slots[i - size].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleUp(self):
        flag = True
        size = self.slots.count
        while (flag):
            flag = False
            for i in range(size, size ** 2):
                if self.slots.slots[i].mean == self.slots.slots[i - size].mean and self.slots.slots[i].mean != 0:
                    return True
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - size].mean == 0:
                    return True
        return False

    def MoveLeft(self):
        size = self.slots.count
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2):
                if i % size == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i - 1].mean and self.slots.slots[i].mean != 0 and \
                        flags[(i - 1) // size][(i - 1) % size] and flags[i // size][i % size]:
                    flag = True
                    self.score += 2 * self.slots.slots[i - 1].mean
                    self.slots.slots[i - 1].mean = 2 * self.slots.slots[i - 1].mean
                    self.slots.slots[i - 1].image = self.slots.images[self.slots.slots[i - 1].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[(i - 1) // size][(i - 1) % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - 1].mean == 0:
                    flag = True
                    self.slots.slots[i - 1].image = self.slots.slots[i].image
                    self.slots.slots[i - 1].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleLeft(self):
        size = self.slots.count
        flag = True
        while (flag):
            flag = False
            for i in range(size ** 2 - 1, -1, -1):
                if i % size == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i - 1].mean and self.slots.slots[i].mean != 0:
                    return True
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i - 1].mean == 0:
                    return True
        return False

    def MoveDown(self):
        size = self.slots.count
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2 - size - 1, -1, -1):
                if self.slots.slots[i].mean == self.slots.slots[i + size].mean and self.slots.slots[i].mean != 0 and \
                        flags[i // size + 1][i % size] and flags[i // size][i % size]:
                    flag = True
                    self.score += 2 * self.slots.slots[i + size].mean
                    self.slots.slots[i + size].mean = 2 * self.slots.slots[i + size].mean
                    self.slots.slots[i + size].image = self.slots.images[self.slots.slots[i + size].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[i // size + 1][i % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i + size].mean == 0:
                    flag = True
                    self.slots.slots[i + size].image = self.slots.slots[i].image
                    self.slots.slots[i + size].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleDown(self):
        size = self.slots.count
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
        size = self.slots.count
        flag = True
        flags = self.MakeFlags(size)
        while (flag):
            flag = False
            for i in range(size ** 2 - 1, -1, -1):
                if (i - size + 1) % size == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i + 1].mean and self.slots.slots[i].mean != 0 and \
                        flags[(i - 1) // size][(i + 1) % size] and flags[i // size][i % size]:
                    flag = True
                    self.score += 2 * self.slots.slots[i + 1].mean
                    self.slots.slots[i + 1].mean = 2 * self.slots.slots[i + 1].mean
                    self.slots.slots[i + 1].image = self.slots.images[self.slots.slots[i + 1].mean]
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])
                    flags[(i + 1) // size][(i + 1) % size] = False
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i + 1].mean == 0:
                    flag = True
                    self.slots.slots[i + 1].image = self.slots.slots[i].image
                    self.slots.slots[i + 1].mean = self.slots.slots[i].mean
                    self.slots.slots[i].mean = 0
                    self.slots.slots[i].image = self.slots.images[0]
                    self.slots.empty_slots = []
                    for j in range(size ** 2):
                        if self.slots.slots[j].mean == 0:
                            self.slots.empty_slots.append(self.slots.slots[j])

    def PossibleRight(self):
        size = self.slots.count
        flag = True
        while (flag):
            flag = False
            for i in range(size ** 2 - 1, -1, -1):
                if (i - size + 1) % size == 0:
                    continue
                if self.slots.slots[i].mean == self.slots.slots[i + 1].mean and self.slots.slots[i].mean != 0:
                    return True
                elif self.slots.slots[i].mean != 0 and self.slots.slots[i + 1].mean == 0:
                    return True
        return False

    def draw_rect(self, painter, x, y, image, size):
        rect = QtCore.QRect(x, y, size - 2, size - 2)
        painter.drawImage(rect, image)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:

        key = a0.key()
        success_move = False
        if self.is_game_over():
            MainWindow.leaderboard.score = self.score
            img = Image.open('pics_2502/game_over_alt.png')
            MainWindow.leaderboard.show_me_what_i_need()
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("chiller_regular.ttf", 35)
            draw.text((365, 262), str(self.score), (200, 50, 70), font=font)
            MainWindow.leaderboard.setData()
            points_check = list(map(int, MainWindow.leaderboard.data.values()))
            points_check.append(self.score)
            points_check = sorted(points_check, reverse = True)
            draw.text((425, 396), str((points_check.index(self.score) + 1)), (200, 50, 70), font=font)
            img.save("pics_2502/game_over_alt_score.png")
            picture_label = QLabel(MainWindow)
            pixmap = QPixmap('pics_2502/game_over_alt_score.png')
            pixmap = pixmap.scaled(MainWindow.geometry().height(), 1000, QtCore.Qt.KeepAspectRatio)
            picture_label.setPixmap(pixmap)
            picture_label.resize(pixmap.width(), pixmap.height())
            picture_label.show()

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
        if (self.PossibleLeft() or self.PossibleUp() or self.PossibleDown() or self.PossibleRight()):
            return False
        return True

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, diam=4):
        super(MainWindow, self).__init__()
        self.board_diam = diam
        self.background_pick = QPixmap('pics_2502/bg_bg.png')
        self.background = QLabel(self)
        self.board = Board(self, self.board_diam)
        self.scoreLabel = QtCore.QRectF(1000, 1000, 1200, 1000)
        self.SetBackground(diam)
        self.name_edit = QLineEdit(self)
        self.add_name_button = QtWidgets.QPushButton("Name", self)
        self.SetNameEdit()
        self.restart_button = QtWidgets.QPushButton('Restart', self)
        self.SetRestartButton()
        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.SetSlider(diam - 4)
        self.text_field = QLabel(f'', self)
        for i in range(4):
            self.SetTextField(i)
        self.setTable()
        self.leaderboard = Leaderboard(self, self.leaderboard_table, self.name_edit, self.add_name_button, self.board_diam, self.board.score)
        self.leaderboard.write_to_table()
    def restart(self, diam=4):
        self.SetBackground(self.slider.value() + 4)
        self.SetNameEdit()
        self.SetRestartButton()
        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.SetSlider(self.slider.value())
        self.text_field = QLabel(f'', self)
        for i in range(4):
            self.SetTextField(i)
        self.setTable()
        self.leaderboard = Leaderboard(self, self.leaderboard_table, self.name_edit, self.add_name_button, self.board_diam, self.board.score)
    def setTable(self):
        self.leaderboard_table = QTableWidget(self)
        self.leaderboard_table.setColumnCount(2)
        self.leaderboard_table.setRowCount(6)
        self.leaderboard_table.setHorizontalHeaderLabels(["Name", "Record "])
        self.leaderboard_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.leaderboard_table.verticalHeader().setSectionResizeMode(0)
        self.leaderboard_table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.leaderboard_table.horizontalHeaderItem(0).setData(Qt.ForegroundRole, QVariant((QtGui.QColor(200, 50, 70))))
        self.leaderboard_table.horizontalHeaderItem(1).setData(Qt.ForegroundRole, QVariant((QtGui.QColor(200, 50, 70))))
        self.leaderboard_table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.leaderboard_table.setColumnWidth(0, 100)
        self.leaderboard_table.setColumnWidth(1, 75)
        self.leaderboard_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.leaderboard_table.setGeometry(100, 200, 200, 310)
        self.leaderboard_table.move(900, 400)
        self.leaderboard_table.setStyleSheet("""
                    QTableWidget{
                        background-color: #222;
                        color: rgb(200, 50, 70);
                    }
                    QWidget > QHeaderView{
                    background-color: #333}"

                """)
        self.leaderboard_table.show()
    def SetBackground(self, board_diam=4):
        self.setStyleSheet("background-color: rgb(50, 50, 50)")
        self.background.setPixmap(self.background_pick)
        self.background.resize(840, 1000)
        self.background.move(0, 0)
        self.background.show()
        self.board_diam = board_diam
        self.board = Board(self, self.board_diam)
        self.setCentralWidget(self.board)
        self.setGeometry(0, 0, 1200, 840)
        self.scoreLabel = QtCore.QRectF(1000, 1000, 1200, 1000)
        self.show()
    def SetNameEdit(self):
        self.name_edit = QLineEdit(self)
        self.name_edit.setGeometry(300, 300, 280, 60)
        self.name_edit.move(900, 760)
        self.name_edit.setStyleSheet("color: red;")
        self.add_name_button = QtWidgets.QPushButton("Name", self)
        self.add_name_button.setGeometry(100, 15, 100, 40)
        self.add_name_button.move(900, 718)
        self.add_name_button.setStyleSheet(
            "QPushButton {background-color:rgb(40, 40, 40); color: rgb(200, 50, 70); border-radius:10;}")
        self.add_name_button.setFont(QtGui.QFont('Arial', 14))

    def SetRestartButton(self):
        self.restart_button = QtWidgets.QPushButton('Restart', self)
        self.restart_button.setGeometry(900, 15, 200, 100)
        self.restart_button.move(900, 150)
        self.restart_button.setStyleSheet(
            "QPushButton {background-color:rgb(40, 40, 40); color: rgb(200, 50, 70); border-radius:10;}")
        self.restart_button.setFont(QtGui.QFont('Arial', 14))
        self.restart_button.clicked.connect(self.restart)
        self.restart_button.show()

    def SetSlider(self, diam):
        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setGeometry(900, 300, 200, 10)
        self.slider.setMaximum(3)
        self.slider.setStyleSheet("""
                            QSlider{
                                background: #323232;
                            }
                            QSlider::groove:horizontal {  
                                height: 10px;
                                margin: 0px;
                                border-radius: 5px;
                                background-color: rgb(119, 110, 101);
                            }
                            QSlider::handle:horizontal {
                                background: #fff;
                                border: 1px solid #B0AEB1;
                                width: 17px;
                                margin: -5px 0; 
                                border-radius: 8px;
                            }
                            QSlider::sub-page:qlineargradient {
                                background-color:rgb(200, 50, 70);
                                border-radius: 5px;
                            }
                        """)
        self.slider.setSliderPosition(self.board_diam - 4)
        self.slider.show()

    def SetTextField(self, n):
        self.text_field = QLabel(f'<h1 style="color: rgb(119, 110, 101);">{n + 4}x{n + 4}', self)
        self.text_field.setGeometry(n * 61 + 897, 320, 30, 20)
        self.text_field.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field.show()


class Leaderboard:
    def __init__(self, mw, lb,  nf, bt, bd, sc):
        add = str(bd)
        self.filename = "leaderboard" + add + ".txt"
        self.MainWindow = mw
        self.file = open(self.filename, 'r+')
        self.leaderboard = lb
        self.name_field = nf
        self.button = bt
        self.data = dict()
        self.lines_count = sum(1 for line in open(self.filename))
        self.score = sc
        self.write_to_table()
        self.button.clicked.connect(self.write_to_file)


    def write_to_table(self):
        self.file = open(self.filename)
        for i in range(6):
            self.leaderboard.setItem(i, 0, QTableWidgetItem())
            self.leaderboard.setItem(i, 1, QTableWidgetItem())
        self.lines_count = sum(1 for line in open(self.filename))
        self.file.seek(0)
        for i in range(min(6, self.lines_count)):
            name, points = self.file.readline().split()
            self.leaderboard.setItem(i, 0, QTableWidgetItem(name))
            self.leaderboard.setItem(i, 1, QTableWidgetItem(points))


    def show_me_what_i_need(self):
        self.name_field.show()
        self.button.show()


    def dict_sort(self):
        inverse_dict = {v: k for k, v in self.data.items()}
        inverse_dict = dict(sorted(inverse_dict.items(), reverse = True))
        self.data = {v: k for k, v in inverse_dict.items()}

    def setData(self):
        beta_data = []
        self.file = open(self.filename)
        self.lines_count = sum(1 for line in open(self.filename))
        for i in range(self.lines_count):
            name, points = self.file.readline().split()
            beta_data.append([name, int(points)])
        self.data.update(beta_data)
        self.file.seek(0)
    def write_to_file(self):
        self.setData()
        name = self.name_field.text()
        if len(name) > 12:
            print("Your name can't be longer than 12 symbols!")
            return
        if name.count(" ") > 0:
            print("You can't use space symbol in your name!")
            return
        if len(name) == 0:
            print("Enter your name!")
            return
        for key in self.data.keys():
            if self.data[key] == self.score:
                self.data.pop(key)
                self.data[name] = self.score
                break
        if name in self.data.keys():
            self.data[name] = max(self.score, self.data[name])
            if self.score < self.data[name]:
                print("You have a higher record! Enter your name or click Restart!")

        else:
            self.data[name] = self.score
        self.dict_sort()
        with open(self.filename, 'w') as out:
            for key, val in self.data.items():
                out.write('{} {}\n'.format(key, val))
        self.write_to_table()


    def resize(self, value):
        self.board_diam = value + 4


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.restart()
    MainWindow.show()
    sys.exit(app.exec_())
