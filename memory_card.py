from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QButtonGroup,
    QRadioButton,
    QPushButton,
    QLabel,
)
from random import shuffle
from random import randint

app = QApplication([])
window = QWidget()

window.cur_question = -1

class Question():
    def __init__(self, question, RRight_btn, Wrong2, Wrong3, Wrong4):
        self.question = question
        self.RRight_btn = RRight_btn
        self.Wrong2 = Wrong2
        self.Wrong3 = Wrong3
        self.Wrong4 = Wrong4

Question_list = []
Question_list.append(
    Question(
        'Удалось ли мне реализовать Memory Card?',
        'Ну раз я это читаю, я думаю что да',
        'Нет',
        'Я не уверен точно',
        'Гык'
    )
)

Question_list.append(
    Question(
        "Это вопрос!",
        'Круто!',
        'Не очень',
        '2/10',
        'Нет'
    )
)

Question_list.append(
    Question(
        'О?',
        'O!',
        'A',
        'Че?',
        'Cool'
    )
)

Question_list.append(
    Question(
        'Меня заставили сделать еще 6 вопросов. Что делать?',
        'Просто сделай их и будь счастлив',
        'Я абсолютно неправильный ответ',
        'Я абсолютно неправильный ответ',
        'Прыгни в окно, тут не высоко',
    )
)

Question_list.append(
    Question(
        '',
        '',
        '',
        '',
        '',
    )
)

window.setWindowTitle('Memory Card')
window.resize(400,300)
quest = QLabel('вопрос')
button = QPushButton('Ответить')
RRight_btn = QRadioButton('вариант ответа')
Wrong2 = QRadioButton('вариант ответа')
Wrong3 = QRadioButton('вариант ответа')
Wrong4 = QRadioButton('вариант ответа')


GrBox = QGroupBox('Варианты ответов')
RadioGroup = QButtonGroup()
RadioGroup.addButton(RRight_btn)
RadioGroup.addButton(Wrong2)
RadioGroup.addButton(Wrong3)
RadioGroup.addButton(Wrong4)

AnswerGrBox = QGroupBox('Результат')
IdResult = QLabel('ты прав или нет?')
IdCorrect = QLabel('Ответ тут показан!!!')

AnswerGrBox.hide()

VBox_res = QVBoxLayout()
VBox_res.addWidget(IdResult, alignment=Qt.AlignLeft | Qt.AlignTop)
VBox_res.addWidget(IdCorrect, alignment=Qt.AlignCenter,stretch=2)

AnswerGrBox.setLayout(VBox_res)

HBox1 = QHBoxLayout()
VBox1 = QVBoxLayout()
VBox2 = QVBoxLayout()

VBox1.addWidget(RRight_btn)
VBox1.addWidget(Wrong2)
VBox2.addWidget(Wrong3)
VBox2.addWidget(Wrong4)

def show_question():
    AnswerGrBox.hide()
    GrBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    RRight_btn.setChecked(False)
    Wrong2.setChecked(False)
    Wrong3.setChecked(False)
    Wrong4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    GrBox.hide()
    AnswerGrBox.show()
    button.setText('Следующий вопрос')

def start_test():
    if button.text() == 'Ответить':
        button.clicked.connect(show_result)
    else:
        button.clicked.connect(show_question)

answer = [RRight_btn, Wrong2, Wrong3, Wrong4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.RRight_btn)
    answer[1].setText(q.Wrong2)
    answer[2].setText(q.Wrong3)
    answer[3].setText(q.Wrong4)
    quest.setText(q.question)
    IdCorrect.setText(q.RRight_btn)
    show_question()

def show_correct(res):
    IdResult.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!!')
        window.score += 1
        print('Статистика\n- Всего вопросов:',window.total,'\n- Всего правильных ответов:',window.score,'\n- Всего неправильных ответов:',window.lose)
        print('Рейтинг:',window.score/window.total*100,'%')
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неправильно')
        window.lose += 1
        print('Статистика\n- Всего вопросов:',window.total,'\n- Всего правильных ответов:',window.score,'\n- Всего неправильных ответов:',window.lose)
        print('Рейтинг:',window.score/window.total*100,'%')

def next_question():
    window.total += 1
    # print('Статистика\n- Всего вопросов:',window.total,'\n- Всего правильных ответов:',window.score,'\n- Всего неправильных ответов:',window.lose)
    cur_question = randint(0,len(Question_list)-1)
    q = Question_list[cur_question]
    ask(q)

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


button.clicked.connect(click_ok)

HBox1.addLayout(VBox1)
HBox1.addLayout(VBox2)

GrBox.setLayout(HBox1)

HBox_1 = QHBoxLayout()
HBox_2 = QHBoxLayout()
HBox_3 = QHBoxLayout()

HBox_1.addWidget(quest, alignment=Qt.AlignCenter)
HBox_2.addWidget(GrBox)
HBox_2.addWidget(AnswerGrBox)
HBox_3.addWidget(button)

VBox_1 = QVBoxLayout()
VBox_1.addLayout(HBox_1,stretch=2)
VBox_1.addLayout(HBox_2,stretch=8)
VBox_1.addStretch(1)
VBox_1.addLayout(HBox_3,stretch=1)
VBox_1.addStretch(1)
VBox_1.setSpacing(5)

window.setLayout(VBox_1)

window.lose = 0
window.total = 0
window.score = 0
next_question()


window.show()
app.exec_()
