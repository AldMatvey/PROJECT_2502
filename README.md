# 2048
###### Игра 2048 с классическими правилами. Существует четыре размера игрового поля: 4х4, 5х5, 6х6, 7х7. Вы можете выбрать его перед перезапуском игры. Есть таблица лидеров, вы можете сохранить свой рекорд в конце игры и сравнить с другими результатами.

# Код
## Классы: 
###### Slot представляет собой одну ячейку на поле.
###### Slots представляут собой контейнер для всех ячеек. Функция add_slot() добавляет клетку с 2 или 4 баллами.
###### Board представляет собой игровое поле. Есть функции paintEvent - перерисовывать игровое поле; MakeFlags(), MoveUp(), PossibleUp(), MoveLeft(), PossibleLeft(), MoveDown(), PossibleDown(), MoveRight(), PossibleRight() - логика переподсчёта при движении вверх, влево, вниз или вправо соответственно; keyPressEvent() - функция отклика на нажатие клавиш вверх, вниз, вправо или влево; is_game_over() - проверка, закончилась ли игра.
###### MainWindow представляет собой окно игры с полем, ползунком размера поля, счётом и кнопкой restart, которая начинает новую игру. Есть функции restart() - перезапуск игры; resize() - изменение размеров поля.
###### Есть leaderboard_table с функцией rewrtite_leaderboard() - сохраннение нового пользователя. Пользователи и их очки сохраняются в файл leaderboard.txt.
