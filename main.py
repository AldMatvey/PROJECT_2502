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

        self.slots = Slots(diam, 840)

    score = 0

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
            img = Image.open('pics_2502/game_over_alt.png')
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("ComicSansMS3.ttf", 25)
            draw.text((380, 300), str(self.score), (0, 0, 0), font=font)
            img.save("pics_2502/game_over_alt_score.png")
            picture_label = QLabel(MainWindow)
            pixmap = QPixmap('pics_2502/game_over_alt_score.png')
            pixmap4 = pixmap.scaled(MainWindow.geometry().height(), 1000, QtCore.Qt.KeepAspectRatio)
            picture_label.setPixmap(pixmap4)
            picture_label.resize(pixmap4.width(), pixmap4.height())
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
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("background-color: rgb(50, 50, 50)")
        self.background_pick = QPixmap('pics_2502/bg_bg.png')
        self.background = QLabel(self)
        self.background.setPixmap(self.background_pick)
        self.background.resize(840, 1000)
        self.background.move(0, 0)
        self.background.show()
        self.board_diam = 4
        self.board = Board(self, self.board_diam)
        self.setCentralWidget(self.board)
        self.setGeometry(0, 0, 1200, 840)
        self.scoreLabel = QtCore.QRectF(1000, 1000, 1200, 1000)
        self.show()
        self.restart_button = QtWidgets.QPushButton('Restart', self)
        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.restart_button.setGeometry(900, 15, 200, 100)
        self.restart_button.move(900, 150)
        self.restart_button.setStyleSheet(
            "QPushButton {background-color:rgb(40, 40, 40); color: rgb(119, 110, 101); border-radius:10;}")
        self.restart_button.setFont(QtGui.QFont('Arial', 14))
        self.restart_button.clicked.connect(self.restart)
        self.restart_button.show()
        self.slider.setGeometry(900, 300, 200, 30)
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
        self.slider.show()
        self.text_field_4 = QLabel('<h1 style="color: rgb(119, 110, 101);">4x4', self)
        self.text_field_4.setGeometry(897, 320, 30, 20)
        self.text_field_4.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_4.show()
        self.text_field_5 = QLabel('<h1 style="color: rgb(119, 110, 101);">5x5', self)
        self.text_field_5.setGeometry(958, 320, 30, 20)
        self.text_field_5.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_5.show()
        self.text_field_6 = QLabel('<h1 style="color: rgb(119, 110, 101);">6x6', self)
        self.text_field_6.setGeometry(1019, 320, 30, 20)
        self.text_field_6.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_6.show()
        self.text_field_7 = QLabel('<h1 style="color: rgb(119, 110, 101);">7x7', self)
        self.text_field_7.setGeometry(1080, 320, 30, 20)
        self.text_field_7.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_7.show()

    def restart(self):
        self.background_pick = QPixmap('pics_2502/bg_bg.png')
        self.background = QLabel(self)
        self.background.setPixmap(self.background_pick)
        self.background.resize(840, 1000)
        self.background.move(0, 0)
        self.background.show()
        self.board = Board(self, self.board_diam)
        self.setCentralWidget(self.board)
        self.scoreLabel = QtCore.QRectF(1000, 1000, 1200, 1000)
        self.show()
        self.restart_button = QtWidgets.QPushButton('Restart', self)
        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.restart_button.setGeometry(900, 15, 200, 100)
        self.restart_button.move(900, 150)
        self.restart_button.setStyleSheet(
            "QPushButton {background-color:rgb(40, 40, 40); color: rgb(200, 50, 70); border-radius:10;}")
        self.restart_button.setFont(QtGui.QFont('Arial', 14))
        self.restart_button.clicked.connect(self.restart)
        self.restart_button.show()
        self.slider.setGeometry(900, 300, 200, 20)
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
                                background-color:rgb(200, 50, 70);;
                                border-radius: 5px;
                            }
                        """)
        self.slider.setSliderPosition(self.board_diam - 4)
        self.slider.show()
        self.text_field_4 = QLabel('<h1 style="color: rgb(119, 110, 101);">4x4', self)
        self.text_field_4.setGeometry(897, 320, 30, 20)
        self.text_field_4.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_4.show()
        self.text_field_5 = QLabel('<h1 style="color: rgb(119, 110, 101);">5x5', self)
        self.text_field_5.setGeometry(958, 320, 30, 20)
        self.text_field_5.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_5.show()
        self.text_field_6 = QLabel('<h1 style="color: rgb(119, 110, 101);">6x6', self)
        self.text_field_6.setGeometry(1019, 320, 30, 20)
        self.text_field_6.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_6.show()
        self.text_field_7 = QLabel('<h1 style="color: rgb(119, 110, 101);">7x7', self)
        self.text_field_7.setGeometry(1080, 320, 30, 20)
        self.text_field_7.setFont(QtGui.QFont("Times", 6, QtGui.QFont.Bold))
        self.text_field_7.show()
        self.slider.valueChanged.connect(self.resize)

    def resize(self, value):
        self.board_diam = value + 4


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.restart()
    MainWindow.show()
    sys.exit(app.exec_())
