from random import randint
from random import randint
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QLabel,QVBoxLayout,QRadioButton,QHBoxLayout,QPushButton

app = QApplication([])
main_win = QWidget
main_win.show()
main_win.resize(400,200)
main_win.win.setWindowTitle('Конкурс від Crazy People')
question = QLabel('В якому році канал отримав золоту кнопку від Youtube')
ans1 = QRadioButton('2005')
ans2 = QRadioButton('2010')
ans3 = QRadioButton('2015')
ans4 = QRadioButton('2020')
layout_main = QVBoxLayout()

layout1 = QHBoxLayout()
layoutH1= QHBoxLayout()
layoutH2= QHBoxLayout()
layoutH3= QHBoxLayout()

layoutH1.addWidget(question,alignment=Qt.AlignCenter)
layoutH2.addWidget(ans1,alignment=Qt.AlignCenter)
layoutH2.addWidget(ans2,alignment=Qt.AlignCenter)
layoutH3.addWidget(ans3,alignment=Qt.AlignCenter)
layoutH3.addWidget(ans4,alignment=Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

main_win.setLayout(layout_main)

def win():
    victory = QMessageBox()
    victory.setText('Правильно! Ви виграли гіроскутер')
    victory.exec_()
ans1.clicked.connect(win)
    
app.exec_()