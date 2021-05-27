import random
import PySimpleGUI as sg
import os


class PasswordGen:
    def __init__(self):
        #Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Application', size=(11, 1)),
             sg.Input(key='site', size=(21, 1))],
            [sg.Text('E-mail/User', size=(11, 1)),
             sg.Input(key='user', size=(21, 1))],
            [sg.Text('Number of characters'), sg.Combo(values=list(
                range(31)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Generate Password')]
        ]
        #Window
        self.window = sg.Window('Password Generator', layout)

    def start(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Generate Password':
               new_password = self.gen_password(values)
               print(new_password)
               self.save_password(new_password, values)

    def gen_password(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(values['total_chars']))
        new_password = ''.join(chars)
        return new_password

    def save_password(self, new_password, values):
        with open('passwords.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site:{values['site']}, user: {values['user']}, new password: {new_password}")

        print('File saved')


gen = PasswordGen()
gen.start()
