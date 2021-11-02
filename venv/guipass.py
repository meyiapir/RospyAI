# импортируем библиотеку tkinter всю сразу
from tkinter import *
from tkinter import messagebox
from time import sleep as sl
from maincode import *

def gui_pass_main():

    # главное окно приложения
    window = Tk()
    # заголовок окна
    window.title('Авторизация')
    # размер окна
    window.geometry('450x230')
    # можно ли изменять размер окна - нет
    window.resizable(False, False)

    # кортежи и словари, содержащие настройки шрифтов и отступов
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}


    # обработчик нажатия на клавишу 'Войти'
    def clicked():
        global username
        global password
        # получаем имя пользователя и пароль
        username = username_entry.get()
        password = password_entry.get()

        # выводим в диалоговое окно введенные пользователем данные
    #    messagebox.showinfo('Заголовок', '{username}, {password}'.format(username=username, password=password))
        window.destroy()

    # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
    # для всех остальных виджетов настройки делаются также
    main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
    # помещаем виджет в окно по принципу один виджет под другим
    main_label.pack()

    # метка для поля ввода имени
    username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
    username_label.pack()

    # поле ввода имени
    username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка для поля ввода пароля
    password_label = Label(window, text='Пароль', font=label_font , **base_padding)
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(window, show='*', width=20, font=font_entry)
    password_entry.pack()

    # кнопка отправки формы
    send_btn = Button(window, text='Войти', command=clicked)
    send_btn.pack(**base_padding)

    # запускаем главный цикл окна
    window.mainloop()
    try:
        #print('username:', username)
        #print('password:', password)
        cor_us_n = 'TFG'
        cor_us_n_nc = 'nc'
# -----------------------------------------
        cor_pass = 'TFG'
        cor_pass_nc = 'nocon'
# -----------------------------------------
        cor_us_n_check = False
        cor_us_n_nc_check =False
# -----------------------------------------
        cor_pass_check = False
        cor_pass_nc_check = False
# -----------------------------------------
        if username == cor_us_n:
            cor_us_n_check = True
            #print('correct')
        elif username == cor_us_n_nc:
            cor_us_n_nc_check = True
        else:
            cor_us_n_check = False
            cor_us_n_nc_check = False
            #print('incorrect')
# -----------------------------------------------------
        if password == cor_pass:
            cor_pass_check = True
            #print('correct')
        elif password == cor_pass_nc:
            cor_pass_nc_check = True
        else:
            cor_pass_check = False
            cor_pass_nc_check = False
            #print('incorrect')
        if cor_pass_check == True and cor_us_n_check == True:
            print(' \n'*2)
            print('--------------------------------------------------------------------- ')
            print('------------------------[ LOGIN SUCCESSFUL ]-------------------------')
            print('--------------------------------------------------------------------- ')
            sl(2.2)
            print(' \n'*20)
            sl(1.65)
        elif cor_pass_nc_check == True and cor_us_n_nc_check == True:
            print(' ')
            print('PASS[nocon]: True!')
            print(' ')
            print(' ')
            print('--------------------------------------------------')
            start_main()
        else:
            while True:
                print(' \n'*50)
                print('LOGIN INCORRECT!')
                print('LOGIN INCORRECT!')
                print('LOGIN INCORRECT!')
                input()
                exit(0)
    except NameError:
        print(' \n'*10)
        print('----------[ LoginError! ]----------')
        sl(1)
        print(' ')
        exit(0)