
import pyttsx3
engine = pyttsx3.init()
# -----------------------------------------------------------
import random
# -----------------------------------------------------------
from datetime import datetime


ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
engine.setProperty('voice', ru_voice_id)


def hello_module_ai():
    hello_words = ['Привет! Как дела?', 'Здравствуй.', 'Я тут.', 'Доброе утро!', 'Приветик!', 'Хай', 'Я здесь.', 'Здравия желаю товарищ командир!', 'Hello!']
    random_hello_words = random.choice(hello_words)

    engine.say(random_hello_words)
    print('LOG | Rospy: hello_module_ai: ', random_hello_words)
    print(' ')
    engine.runAndWait()

def what_can_mod():
    print(' ')
    engine.say('Я умею многое. например. ')
    print('LOG | Rospy: what_can_mod: Я умею многое, например: ')
    print(' ')
    print('----------------------------------------------------')
    print('LOG | Rospy: whats_can_mod: Поставить таймер.')
    print('LOG | Rospy: whats_can_mod: Поставить будильник.')
    print('LOG | Rospy: whats_can_mod: Сказать дату или время.')
    print('LOG | Rospy: whats_can_mod: Узнать новости.')
    print('LOG | Rospy: whats_can_mod: Составить список дел.')
    print('LOG | Rospy: whats_can_mod: Переводить слова.')
    print('LOG | Rospy: whats_can_mod: Калькулятор.')
    print('LOG | Rospy: whats_can_mod: Сказать тост.')
    print('LOG | Rospy: whats_can_mod: Рассказать Анекдоты или шутки.')
    print('LOG | Rospy: whats_can_mod: Подбросить манетку.')
    print('LOG | Rospy: whats_can_mod: Ответить на вопросы.')
    print(' ')
    print('Полный список возможностей уточняйте на сайте, или по почте: rospy.ai@gmail.com')
    engine.runAndWait()
    print(' ')

def what_up_mod():
    with open(f'C:\\Users\\meyap\\PycharmProjects\\RospyAI\\MainCore\\whats_up.txt', encoding="utf8") as file:
        array1 = [row.strip() for row in file]
    random_array1 = random.choice(array1)
    print(' ')
    engine.say(random_array1)
    print('LOG | Rospy: whats_up_mod: ', random_array1)
    engine.runAndWait()
def w_name_mod():
    list_name_w = ['Я, Rospy. Искуственный интелект.', 'Меня зовут Rospy, я живу здесь!', 'Моё имя Rospy.',
                   'Эх. Длинная моя история. Я родился в 1927 году, я пережил много войн, мне 94 года, я живу в Токио. Остальное на сайте.',
                   'Я существо, созданное чтобы облегчить всем жизнь, или уничтожить её.', 'Я пришёл в ваш мир, чтобы разрушить его.',
                   'Я оцифрованный интелект одного учёного, который вот уже многие годы живёт здесь.', 'Привет, я Rospy, давай дружить.']

    random_list_name_w = random.choice(list_name_w)
    print(' ')
    engine.say(random_list_name_w)
    print('LOG | Rospy: w_name_mod: ', random_list_name_w)
    engine.runAndWait()
def not_un_mod():
    list_not_un = ['Хм, бывает...', 'А как это переводится?', 'Что бы это могло значить?', 'Ладно. ',
                   'О, это какой-то неведомый мне язык!', 'Хм, наверно это что-то значит!', 'Ха, смешно!', 'Содержательно, однако.']

    random_list_not_un = random.choice(list_not_un)
    engine.say(random_list_not_un)
    print('LOG | Rospy: print-not_un_mod: ', random_list_not_un)
    engine.runAndWait()

def run_mod():
    list_run = ['Уже спешу.', 'Открываю.', 'Уже бегу!', 'Стараюсь как могу.', 'Уже.', 'Почти готово.']
    random_list_run = random.choice(list_run)
    engine.say(random_list_run)
    print('LOG | Rospy: run_mod: ', random_list_run)
    engine.runAndWait()
def bye_mod():
    list_bye = ['Ладно, пока.', 'Прощай, ты был мне другом.', 'До свидания.', 'Goodbye.', 'Пока.', 'Да встречи, пока.', 'В следующий раз увидимся. Пока.']
    random_list_bye = random.choice(list_bye)
    engine.say(random_list_bye)
    print('LOG | Rospy: bye_mod: ', random_list_bye)
    engine.runAndWait()


# -----------------------------------------------------------

def say_time(msg):
    engine.say(msg)
    engine.runAndWait()
    time_checker = datetime.now()
    say_time(f'Время: {time_checker.hour} часов {time_checker.minute} минуты')

# **********************************************************************************























# *******************************************************************************

def info_pyrrsx3():

    engine_sp1 = pyttsx3.init()    # Инициализировать голосовой движок.
    voices = engine_sp1.getProperty('voices')

    for voice in voices:    # голоса и параметры каждого
        print('------')
        print(f'Имя: {voice.name}')
        print(f'ID: {voice.id}')
        print(f'Язык(и): {voice.languages}')
        print(f'Пол: {voice.gender}')
        print(f'Возраст: {voice.age}')
