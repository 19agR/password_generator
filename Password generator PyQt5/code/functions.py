import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from design import Ui_MainWindow

import sqlite3

import random
import string

# Инициализация окна и ui
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setWindowIcon(QtGui.QIcon('resources/icon_main.png'))
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


# Подключение и создание базы данных, если еще не создана
file_name = 'resources/db_of_passwords.db'
db = sqlite3.connect(file_name)
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                key TEXT,
                password TEXT
                )''')

# Необходимы для работы функций генерации пароля
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits[2:]
already_used_passwords = set()

for lower, upper in zip(lower_letters, upper_letters):
    if lower in ['I', 'l', '1', 'o', 'O', '0']:
        lower_letters = lower_letters.replace(lower, '')
    if upper in ['I', 'l', '1', 'o', 'O', '0']:
        upper_letters = upper_letters.replace(upper, '')

all_symbols = lower_letters + upper_letters + numbers


def generate_password(length):
    """Генерация пароля как минимум с 1 цифрой, буквой верхнего и нижнего регистров"""
    password, result = [], ''

    password.append(random.choice(lower_letters))
    password.append(random.choice(upper_letters))
    password.append(random.choice(numbers))
    random.shuffle(password)

    cur_all_symbols = all_symbols[:]
    for symbol in password:
        cur_all_symbols = cur_all_symbols.replace(symbol, '')

    for symbol in random.sample(cur_all_symbols, k=length - 3):
        password += symbol

    return ''.join(password)


def main(quantity, length):
    """Генерация сразу нескольких паролей на основе функции generate_password(length)"""
    i = 0
    result = []
    while i < quantity:
        new_password = generate_password(length)
        if new_password in already_used_passwords:
            continue
        else:
            already_used_passwords.add(new_password)
            result.append(new_password)
            i += 1
    return result


def run():
    """Запуск программы"""

    # Привязка функций к кнопкам
    ui.button_generate.clicked.connect(click_on_button_generate)

    ui.button_complete.clicked.connect(click_on_button_complete)

    ui.button_take_all_passwords.clicked.connect(show_all_passwords_dialog)

    ui.button_del_all_passwords.clicked.connect(lambda: show_del_dialog(one=False))

    # Отключаем возможоность писать тест в поле пароля, если активна кнопка "получить из бд"
    if ui.radio_button_from_db.isChecked():
        ui.line_password_2.setReadOnly(True)

    # Если переключаются радио кнопки,
    # делаем проверку на то, нужно ли ставить readOnly на поле пароля
    ui.radio_button_to_db.toggled.connect(check_radio_button)
    ui.radio_button_from_db.toggled.connect(check_radio_button)

    MainWindow.show()
    sys.exit(app.exec_())


def click_on_button_generate():
    """Обрабатывает нажатие на кнопку 'Сгенировать пароль'"""
    length = ui.spinBox_length.text()
    password = generate_password(int(length))
    ui.line_password.setText(password)
    if ui.radio_button_to_db.isChecked():
        ui.line_password_2.setText(password)


def click_on_button_complete():
    """Обрабатывает нажатие на кнопку 'Выполнить'"""
    if ui.radio_button_to_db.isChecked():
        write_to_db()
    elif ui.radio_button_from_db.isChecked():
        take_from_db()
    elif ui.radio_button_del.isChecked():
        show_del_dialog(key=ui.line_key.text())


def check_radio_button():
    """
    Проверка положения радио кнопок и выставления режима ReadOnly на поле пароля,
    если активна кнопка 'получить из бд'
    """
    if ui.radio_button_to_db.isChecked():
        ui.line_password_2.setReadOnly(False)
        ui.line_password_2.setFrame(1)
        ui.line_password_2.setTextMargins(-2, 0, 0, 0)
        ui.line_password_2.setStyleSheet('background-color:rgb(255, 255, 255)')
    elif ui.radio_button_from_db.isChecked() or ui.radio_button_del.isChecked():
        if ui.line_password_2.text():
            show_clear_line_password_2_dialog()
        else:
            ui.line_password_2.setFrame(0)
            ui.line_password_2.setTextMargins(0, 2, 0, 2)
            ui.line_password_2.setStyleSheet('background-color:rgb(218, 218, 218)')
            ui.line_password_2.setReadOnly(True)


def write_to_db():
    """Запись в базу данных"""
    password = ui.line_password_2.text()
    key = ui.line_key.text()

    if key and password:
        try:
            cursor.execute(f"SELECT key FROM users WHERE key = '{key}'")
            if cursor.fetchone() is None:
                cursor.execute(f"INSERT INTO users VALUES (?, ?)", (key, password))
                db.commit()
            else:
                show_warning_dialog('Запись уже существует')
        except sqlite3.Error as error:
            print("Не удалось вставить данные в таблицу sqlite")
            print("Класс исключения: ", error.__class__)
            print("Исключение", error.args)
    else:
        if not key:
            text = 'Поле "Сайт/ключ" не может быть пустым'
        elif not password:
            text = 'Поле "Пароль" не может быть пустым'
        else:
            text = 'Непредвиденная ошибка'

        show_warning_dialog(text)


def take_from_db():
    """Получение записи из базы данных"""
    key = ui.line_key.text()

    try:
        cursor.execute(f"SELECT password FROM users WHERE key = '{key}'")
        result = cursor.fetchone()
        if result is not None:
            ui.line_password_2.setText(result[0])
        else:
            show_warning_dialog('Такой записи нет')

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)


def del_from_bd(one=True, key=''):
    """Удаление записи/записей из базы данных"""
    try:
        if one:
            cursor.execute(f"DELETE FROM users WHERE key = '{key}'")
        elif not one:
            cursor.execute(f"DELETE FROM users")
        db.commit()
    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)


def show_warning_dialog(text):
    """Диалоговое окно ошибки"""
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowIcon(QtGui.QIcon('resources/icon_warning.png'))
    msg.setText(text)
    msg.setWindowTitle('Ошибка')
    font = QtGui.QFont()
    font.setPointSize(11)
    msg.setFont(font)
    msg.exec_()


def show_del_dialog(key='', one=True):
    """Диалоговое окно с вопросом об удалении"""
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowIcon(QtGui.QIcon('resources/icon_warning.png'))
    msg.setWindowTitle('Ошибка')
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    text = ''
    if one:
        cursor.execute(f"SELECT password FROM users WHERE key = '{key}'")
        password = cursor.fetchone()
        if password is not None:
            text = f'Вы точно хотите удалить эту запись: \nСайт/ключ: {key};' \
                   f' Пароль: {password[0]}?'
        else:
            show_warning_dialog('Такой записи нет')
            return

    elif not one:
        text = f'Вы точно хотите удалить все записи?'
    msg.setText(text)

    font = QtGui.QFont()
    font.setPointSize(11)
    msg.setFont(font)

    return_value = msg.exec_()

    if return_value == QMessageBox.Yes:
        del_from_bd(one=one, key=key)


def show_all_passwords_dialog():
    """Диалоговое окно со всеми паролями"""
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Close)
    msg.setWindowIcon(QtGui.QIcon('resources/icon_main.png'))

    text = f"Пароли представлены в виде: <key>; <password>\n"
    cursor.execute('SELECT * FROM users')
    for key, password in cursor.fetchall():
        text += f"{key}; {password}\n"

    msg.setText('Нажмите "Show Details", чтобы просмотреть сохраненные пароли')
    msg.setWindowTitle('Your passwords')

    msg.setDetailedText(text)
    font = QtGui.QFont()
    font.setPointSize(11)
    msg.setFont(font)

    msg.exec_()


def show_clear_line_password_2_dialog():
    """Диалоговое окно с вопросом очистить ли поле пароля"""
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText('Поле пароля будет очищено. Нажмите "Оk", если согласны и "Cancel" для выхода')
    msg.setWindowTitle('Очистка поля')
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    font = QtGui.QFont()
    font.setPointSize(11)
    msg.setFont(font)

    return_value = msg.exec_()

    if return_value == QMessageBox.Ok:
        ui.line_password_2.setFrame(0)
        ui.line_password_2.setTextMargins(0, 2, 0, 2)
        ui.line_password_2.setStyleSheet('background-color:rgb(218, 218, 218)')
        ui.line_password_2.setText('')
        ui.line_password_2.setReadOnly(True)
    elif return_value == QMessageBox.Cancel:
        ui.radio_button_to_db.click()
