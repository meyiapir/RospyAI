# import telebot
# TOKEN = '2055316027:AAHPGePwb0mvcJShYEWsLGcPJdQDzRoJxXM'
# bot = telebot.TeleBot(TOKEN)
# joinUsers = '1721373709'
#
#
# @bot.message_handler(commands=['sp'])
# def mess(message):
#     for user in joinUsers:
#         bot.send_message(user, message.text[message.text.find(' '):])
#
#
#
#
# def krasivo1():
#     import random
#     from time import sleep
#     from tqdm import tqdm
#     print('HACKING IN PROCCES...')
#     for i in tqdm(range(100),colour='green'):
#         sleep(random.uniform(0.01, 0.1))
#     print('HACKING... DONE')
#

# ВАЖНО! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import requests
#
# api_token = '1766708402:AAFKvqZo0TGxQ6x9oc-H_FjmbldWcThcW34'
# while True:
#     requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
#        chat_id='1721373709',
#        text='Вроде всё!'
#     ))


# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps
#
# owm = OWM('65eb63798a50845b08c7a2f12f88f871')
# mgr = owm.weather_manager()
#
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather
#
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
import urllib3
try:
    http = urllib3.PoolManager()
    url = 'htt/rospyai.w'
    resp = http.request('GET', url)
    a = resp.status
    if a == 200:
        print(a)
    else:
        print('kaka', a)
except:
    print('404')










































# import tkinter as tk
#
# def toggle_password():
#     if passwd_entry.cget('show') == '':
#         passwd_entry.config(show='*')
#         toggle_btn.config(text='Show Password')
#     else:
#         passwd_entry.config(show='')
#         toggle_btn.config(text='Hide Password')
#
# root = tk.Tk()
#
# passwd_entry = tk.Entry(root, show='*', width=20)
# passwd_entry.pack(side=tk.LEFT)
#
# toggle_btn = tk.Button(root, text='Show Password', width=15, command=toggle_password)
# toggle_btn.pack(side=tk.LEFT)
#
# root.mainloop()


