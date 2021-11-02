# -*- coding: utf8 -*-
import webbrowser
import urllib3
#from maincode import *
import os

# ------------------------------------------------------------------------------------
def web_com_mod():
    main_in_web = input('SITE: ')
    print('__________________________________________________________________')

# ********************************************************************************************
    try:
        http = urllib3.PoolManager()
        url = 'http://' + main_in_web + '.com'
        resp = http.request('GET', url)
        #	print(resp.status)
        webbrowser.open('http://' + main_in_web + '.com')
        #	print('.com - sec')
        global k_er
        k_er = 1
    except:
        #print('.com - error 404')
        k_er = 0
# **************************************************************
    if k_er == 0:
        try:
            print(' ')
            http = urllib3.PoolManager()
            url = 'http://' + main_in_web + '.ru'
            resp = http.request('GET', url)
            #	print('CODE: ', resp.status)
            webbrowser.open('http://' + main_in_web + '.ru')
        #	print('.ru - sec')
        except:
            pass
    else:
        #	print('.ru - error 404')
        k_er = 2
# **************************************************************
    if k_er == 2:
        try:
            print(' ')
            http = urllib3.PoolManager()
            url = 'http://' + main_in_web + '.net'
            resp = http.request('GET', url)
            #	print(resp.status)
            webbrowser.open('http://' + main_in_web + '.net')
        #	print('.net - sec')
        except:
            pass
    else:
        print('')
        #print('.net - error 404')















# def app_open_mod(main_input):
#     #main_in_app = input('APP: ')
#     passwd_gen_list = ['генератор', 'Генератор', 'паролей', 'пароля', 'пароль', 'Пароль', 'Пароля', 'Паролей',
#                        'Открой генератор', 'открой генератор', 'Запусти генератор', 'запусти генератор', 'passgen',
#                        'pg']
#
#     whatsApp_list = ['Открой whatsapp', 'открой whatsapp', 'whatsapp', 'Запусти whatsapp',
#                      'ватсапп', 'запусти whatsapp', 'открой ватсапп', 'запусти ватсапп', 'ватсап',
#                      'переписка в ватсаппе', 'ватсапе', 'ватсаппе', 'wa']
#     datagrip_list = ['Открой datagrip', 'открой datagrip', 'datagrip', 'Запусти datagrip',
#                      'датагрип', 'запусти datagrip', 'открой датагрип', 'запусти датагрип',
#                      'датагрип', 'базы данных', 'датагрипе', 'датагрибе', 'dg']
#     firefox_list = ['Открой firefox', 'открой firefox', 'firefox', 'Запусти firefox',
#                     'фаерфокс', 'фаирфокс', 'запусти firefox', 'открой фаерфокс', 'запусти фаерфокс',
#                     'искать в фаерфокс', 'фаерфоксе', 'фаирфоксе', 'ff']
#     vpn_list = ['Открой vpn', 'открой vpn', 'vpn', 'Запусти vpn', 'впн', 'запусти vpn',
#                 'открой впн', 'запусти впн', 'protonvpn', 'защита с впн', 'впне', 'впэне', 'pv']
#     telegram_list = ['Открой telegram', 'открой telegram', 'telegram', 'Запусти telegram',
#                      'телеграм', 'запусти telegram', 'открой телеграм', 'запусти телеграм', 'телега',
#                      'переписка в телеграме', 'телеграме', 'телеге', 'tg', 'телегу']
#
#     if any(element in main_input for element in passwd_gen_list):
#         print('Запускается: passgen.exe')
#         file_path = r'C:\Users\meyap\OneDrive\Desktop\python\PYexe\dist\passgen.exe'
#         os.system("start " + file_path)
#
#     elif any(element in main_input for element in whatsApp_list):
#         print('Запускается: WhatsApp')
#         file_path = r'C:\Users\meyap\AppData\Local\WhatsApp\WhatsApp.exe'
#         os.system("start " + file_path)
#
#     elif any(element in main_input for element in datagrip_list):
#         print('Запускается: DataGrip')
#         file_path = r'C:\Users\meyap\AppData\Local\JetBrains\Toolbox\apps\datagrip\ch-0\212.5457.41\bin\datagrip64.exe'
#         os.system("start " + file_path)
#
#     elif any(element in main_input for element in firefox_list):
#         print('Запускается: FireFox')
#         file_path = r'C:\Users\meyap\PycharmProjects\RospyAI\firefox'
#         os.system("start " + file_path)
#
#     elif any(element in main_input for element in vpn_list):
#         print('Запускается: ProtonVPN')
#         file_path = r'C:\Users\meyap\PycharmProjects\RospyAI\ProtonVPN'
#         os.system("start " + file_path)
#
#     elif any(element in main_input for element in telegram_list):
#         print('Запускается: Telegram')
#         file_path = r'C:\Users\meyap\PycharmProjects\RospyAI\Telegram'
#         os.system("start " + file_path)
#     else:
#         print(' ')
#         print('Такое приложение ещё не добавлено.')
#         print('Что бы внести предложение обратитесь по этой почте: rospy.ai@gmail.com')
#         print(' ')

# app_open_mod()