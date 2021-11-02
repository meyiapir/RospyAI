from time import sleep as sl
from speechs import *
import pyttsx3                  # Модуль импортов
from commands_mods import *
import urllib3
# ###########################################################################

def starting_mod():                # starting output module
    global cycle_proc
    print(' ')
    print(' ')
    print('STARTING: FILE: maincode.py')
    sl(1)
    print('STARTING: MODULE: starting_mod')
    sl(0.7)
    print('STARTING: RospyAI')
    try:
        http = urllib3.PoolManager()
        url = 'https://rospyai.wixsite.com/rospy-ai/con-check'
        resp = http.request('GET', url)
        a = resp.status
        if a == 200:
            print('CODE:', a)
            en_ch = True
        else:
            print(a)
            en_ch = False
    except:
        print('ERROR: 404')
        en_ch = False
    if en_ch:
        sl(1)
        print(' \n'*2)
        def cycle_proc():
            for i in range(30):
                print('Loading...', i, '%')
                sl(0.1)
            for p in range(40, 101):
                print('Loading...', p, '%')
                sl(0.1)
            print(' ')
        print('STARTED...')
        print(' ')
    else:
        print(' ')
        print('There is no connection to the database, check the network connection!')
        print(' ')
        print('Отсутствует соединение с базой данных, проверьте подключение к сети!')
        print(' ')
        input()
        exit(0)
#    cycle_proc()

class ai:
    def __init__(self):
        print('STARTED: CLASS ai.__init__() ')
        print(' \n'*5)

    @staticmethod
    def test():
        print('STARTED: CLASS: ai.__test__() ')
        print(' \n'*3)

    @staticmethod
    def main():
        print('RospyAi: CLASS: main: ')
        print('STARTED...')
        print(' \n'*3)


alias_h = ['привет', 'Привет', 'Прувет', 'Здравствуй', 'здраствуй', 'здарова', 'Здарова', 'Здрасте',
           'хай', 'Хай', 'хэй', 'Хэй', 'h_mod', 'Прив', 'прив', 'здравстуйте', 'Здравстуйте', 'вет',
           'туйте', 'твуйте', 'туй', 'твуй', 'Здар', 'здар', 'при', 'RospyAi', 'Rospy', 'rospy', 'Распи', 'распи', 'Роспи',
           'роспи', 'Росп', 'росп', 'Расп', 'расп', 'Максик', 'максик', 'ало', 'Ало', 'Алё', 'алё']

alias_wh = ['Чё как', 'чё как', 'чё как?', 'Чё как?', 'Как дела?', 'как дела?', 'Как дела', 'как дела', 'чо как?', 'Чо как?',
            'чо как', 'Чо как', 'Как сам', 'как сам', 'Че как', 'че как', 'Че как?', 'Че как?', 'Какие дела?', 'Какие дела', 'дела', 'Дела']

alias_wc = ['Что умеешь?', 'что умеешь?', 'что умеешь', 'что умееш', 'шо умеешь', 'Шо умеешь?', 'шо могёш', 'Шо могёшь?', 'На что способен?', 'на что способен?', 'на что способен',
            'Шо ты робишь?', 'шо ты робишь', 'твои умения', 'Способности', 'способности', 'Чо можешь', 'чо могёш', 'Чо могёш', 'чо можешь', 'Что ты умеешь делать?',
            'что ты умеешь делать', 'что ты можешь делать?', 'умеешь', 'делать', 'функции', 'Что ты можешь', 'что ты можешь', 'Что ты можешь?', 'что ты можешь?', 'можешь', 'можеш']

alias_web = ['Открой сайт', 'открой сайт', 'Запусти сайт', 'запусти сайт', 'сайт', 'Сайт', 'покажи сайт', 'Покажи сайт', 'web', 'открой ка сайт', 'Найди сайт', 'найди сайт']

alias_bye = ['Пока', 'пока', 'До свидания', 'до свидания', 'досвидания', 'досвидание', 'Досвидания', 'Досвидание',
             'прощай', 'Прощай', 'гудбай', 'Покеда', 'покеда', 'пок', 'Всё', 'всё', 'я ухожу', 'Я ухожу', 'я пошёл',
             'Я пошёл', 'До встречи', 'до встречи', 'bye', 'goodbye', 'Exit', 'exit', 'ex', 'Выход', 'выход', 'прощаться',
             'Прощаться', 'Прощатся', 'прощатся', 'видания', 'досв', 'пок', 'Досв', 'Пок']

alias_rep = ['Повторялка', 'повторялка', 'павторялка', 'Павторялка', 'Повтори', 'повтори', 'Павтори', 'павтори',
             'Repeat', 'repeat', 'rep', 'повт', 'повторяй', 'Повторяй', 'Павторяй', 'павторяй']

# *******************************************************************************************************************************************************************************************

passwd_gen_list = ['генератор', 'Генератор', 'паролей', 'пароля', 'пароль', 'Пароль', 'Пароля', 'Паролей',
                   'Открой генератор', 'открой генератор', 'Запусти генератор', 'запусти генератор', 'passgen',
                   'pg']

whatsApp_list = ['Открой whatsapp', 'открой whatsapp', 'whatsapp', 'Запусти whatsapp',
                 'ватсапп', 'запусти whatsapp', 'открой ватсапп', 'запусти ватсапп', 'ватсап',
                 'переписка в ватсаппе', 'ватсапе', 'ватсаппе', 'wa']

datagrip_list = ['Открой datagrip', 'открой datagrip', 'datagrip', 'Запусти datagrip',
                 'датагрип', 'запусти datagrip', 'открой датагрип', 'запусти датагрип',
                 'датагрип', 'базы данных', 'датагрипе', 'датагрибе', 'dg']

firefox_list = ['Открой firefox', 'открой firefox', 'firefox', 'Запусти firefox',
                'фаерфокс', 'фаирфокс', 'запусти firefox', 'открой фаерфокс', 'запусти фаерфокс',
                'искать в фаерфокс', 'фаерфоксе', 'фаирфоксе', 'ff']

vpn_list = ['Открой vpn', 'открой vpn', 'vpn', 'Запусти vpn', 'впн', 'запусти vpn',
            'открой впн', 'запусти впн', 'protonvpn', 'защита с впн', 'впне', 'впэне', 'pv']

telegram_list = ['Открой telegram', 'открой telegram', 'telegram', 'Запусти telegram',
                 'телеграм', 'запусти telegram', 'открой телеграм', 'запусти телеграм', 'телега',
                 'переписка в телеграме', 'телеграме', 'телеге', 'tg', 'телегу']

discord_list = ['Открой discord', 'открой discord', 'discord', 'Запусти discord', 'дискорд', 'запусти discord',
                'открой дискорд', 'запусти дискорд', 'дискорт', 'дизкорд', 'дискорде',
                'дискорте', 'ds', 'дизкорде', 'Discord', 'Дискорд', 'Дискорде']

my_name_list = ['Ты кто?', 'ты кто?', 'Кто ты?', 'кто ты?', 'Ты кто', 'ты кто', 'Кто ты', 'кто ты', 'Зовут',
                'зовут', 'Как тебя завут?', 'Хто ты?', 'как звать тебя?', 'кто такой?', 'Имя', 'имя', 'кто такой?', 'кто такой',
                'name', 'хто ты', 'Кто же ты такой?', 'кто же ты такой', 'Как тебя звать', 'звать', 'Кто же ты']


# *********************************************************************************************************************************
def in_main_ai_mod():
    print(' ')
    print('------------------------------------------------')
    print(' ')
    global main_input
    main_input = input('I: ')
#    print(' ')

def commands_mod():
    if any(element in main_input for element in alias_h):
        hello_module_ai()

    elif any(element in main_input for element in alias_wh):
        what_up_mod()

    elif any(element in main_input for element in my_name_list):
        print(' ')
        w_name_mod()
# ----------------------------------------------
    elif any(element in main_input for element in alias_rep):
        engine_sp = pyttsx3.init()
        while True:
            pov_im = input('Повторялка(для выхода введите Exit): ')
            if pov_im == 'Exit':
                break
                print(' \n'*5)
            engine_sp.say(pov_im)
            print(' ')
            print('LOG | Rospy: commands_mod: ', pov_im)
            print(' ')
            engine_sp.runAndWait()

    elif any(element in main_input for element in alias_wc):
        print(' ')
        what_can_mod()

    elif any(element in main_input for element in alias_bye):
        bye_mod()
        print(' ')
        print('*****************************************')
        print('                 Exit')
        print('*****************************************')
        print(' ')
        input('PRESS ENTER FOR CONTINUE: \n')
        exit(0)
    elif any(element in main_input for element in alias_web):
        print(' ')
        print('WEB: sec: start')
        web_com_mod()
        run_mod()
# ***********************************************************************************************************
# ***************************************************************************


    elif any(element in main_input for element in passwd_gen_list):
        print('Запускается: passgen.exe')
        run_mod()
        file_path = r'C:\Users\meyap\OneDrive\Desktop\python\PYexe\dist\passgen.exe'
        os.system("start " + file_path)

    elif any(element in main_input for element in whatsApp_list):
        print('Запускается: WhatsApp')
        run_mod()
        file_path = r'C:\Users\meyap\AppData\Local\WhatsApp\WhatsApp.exe'
        os.system("start " + file_path)

    elif any(element in main_input for element in datagrip_list):
        print('Запускается: DataGrip')
        run_mod()
        file_path = r'C:\Users\meyap\AppData\Local\JetBrains\Toolbox\apps\datagrip\ch-0\212.5457.41\bin\datagrip64.exe'
        os.system("start " + file_path)

    elif any(element in main_input for element in firefox_list):
        print('Запускается: FireFox')
        run_mod()
        file_path = r'C:\Users\meyap\PycharmProjects\RospyAI\firefox'
        os.system("start " + file_path)

    elif any(element in main_input for element in vpn_list):
        print('Запускается: ProtonVPN')
        run_mod()
        file_path = r'C:\Users\meyap\PycharmProjects\RospyAI\ProtonVPN'
        os.system("start " + file_path)

    elif any(element in main_input for element in telegram_list):
        print('Запускается: Telegram')
        run_mod()
        file_path = r'C:\Users\meyap\PycharmProjects\RospyAI\Telegram'
        os.system("start " + file_path)
    elif any(element in main_input for element in discord_list):
        print('Запускается: Discord')
        run_mod()
        file_path = r'C:\Users\meyap\AppData\Local\Discord\app-1.0.9003\Discord.exe'
        os.system("start " + file_path)

# ***************************************************************************
# ***********************************************************************************************************
    else:
        not_un_mod()

def start_main():
    starting_mod()
    sl(1.5)
    print(' \n'*50)
    print('------------------[ RospyAI ]-------------------')
    while True:
        in_main_ai_mod()
        commands_mod()
        if main_input == 'Exit':
            exit(0)
# start_main()
