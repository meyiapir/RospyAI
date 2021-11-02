#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from time import sleep as sl
from config import TOKEN

def mainbot():
    print('STARTING: TGbot: bot.py: mainbot()')
    print(' ')
    sl(1)
    # Объект бота
    bot = Bot(token=TOKEN)
    # Диспетчер для бота
    dp = Dispatcher(bot)
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)


    text_a = '1'

    # Хэндлер на команду /test1
    @dp.message_handler(commands="start")
    async def cmd_test1(message: types.Message):
        await bot.send_message(message.chat.id, f'Привет {message.chat.username}, добро пожаловать!')
        await message.answer("Напишите /help чтобы получить помощь!")
#        await message.answer("")

    # Хэндлер на команду /test1
    @dp.message_handler(commands="help")
    async def cmd_test2(message: types.Message):
        await message.answer("/help - команда помощи.")
        await message.answer("Для дополнительной помощи и связи пишите info@meyapir.ru или rospy.ai@gmail.com")

    @dp.message_handler()
    async def echo_message(msg: types.Message):
        await bot.send_message(msg.from_user.id, msg.text)
        global text_a
        text_a = msg.text           # взятие текста  от пользователя.
        print(text_a)




#    if __name__ == "__main__":
        # Запуск бота

    executor.start_polling(dp, skip_updates=True)

mainbot()
# texting_rep = text_a
# print('aaaaaaaaaaaa', texting_rep)


