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
        self.slots = [Slot(size // count, self.brushes[0], i // self.count, i % self.count)
                      for i in range(self.count ** 2)]
        self.empty_slots = [Slot(size // count, self.brushes[0], i // self.count, i % self.count)
                            for i in range(self.count ** 2)]
        self.size = size

    def is_game_over(self):
        pass

    def move(self):

        if self.direction == 'left':
            pass

        if self.direction == 'right':
            pass

        if self.direction == 'up':
            pass

        if self.direction == 'down':
            pass

        self.addSlot()


class Board(QtWidgets.QFrame):
    SPEED = 80

    HEIGHTINBLOCKS = 40
    WIDTHINBLOCKS = 60

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.snake = Slots()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        painter = QtGui.QPainter(self)

        rect = self.contentsRect()

        boardtop = rect.bottom() - self.frameGeometry().height()

        for cord in self.snake.body:
            self.drawrect(painter, rect.left() + cord[0] * self.block_width(),
                          boardtop + cord[1] * self.block_height(), self.snake.color)

    def drawrect(self, painter, x, y, color):
        painter.fillRect(x, y, self.block_width() - 2, self.block_height() - 2, color)

    def timerEvent(self, a0: QtCore.QTimerEvent) -> None:

        if a0.timerId() == self.timer.timerId():
            self.snake.move()
            self.update()

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


