from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import asyncio
import telethon
import os

import random
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from telethon import TelegramClient

users=[]
API_TOKEN = 'dyour_token_dudev3Q8'
try:
    f=open("ids.txt",mode="r",encoding="utf-8")
    f.close()
except Exception as e:
    print(e)
    f = open("ids.txt", mode="w", encoding="utf-8")
    f.close()

file_base=[string.strip('\n') for string in open("ids.txt",mode="r",encoding="utf-8").readlines()]

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Спарсить чат'))
greet_kb.add(KeyboardButton('Справка'))
class OrderFood(StatesGroup):
    parse = State()
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

client = TelegramClient("namers12", 1508153, "e840817be5fdbf4efd169e9d0a7773ad", device_model="Xiaomi MI A1",
                                system_version="5.10.0", app_version="10 P (27)")
client.start()
@dp.message_handler(state=OrderFood.parse)
async def process_name(message: types.Message, state: FSMContext): # обратите внимание, есть второй аргумент
    print(message.from_user.id)
    print("sss")
    try:
        await bot.send_message(message.from_user.id,"Ну, погнали!\nНачинаю собирать юзернеймы пользователей!\nДонать чтобы я работал быстрее :D",reply_markup=greet_kb)
        unideco=str(random.randint(0,392193912))
        file=open("{}.txt".format(unideco),mode="w",encoding="utf-8")
        async for i in client.iter_participants(message.text,aggressive=True):
            if i.is_self == False and i.deleted == False and i.bot == False and i.username!=None:
                file.write("@"+i.username+"\n")
        file.close()
        with open("{}.txt".format(unideco), "rb") as res:
         await bot.send_document(message.from_user.id,caption="Ваш список юзеров с чата {}\nРазработчик - https://t.me/LarryBrackdown\nhttps://t.me/tlscripts".format(message.text),document=res,reply_markup=greet_kb)
        os.remove("{}.txt".format(unideco))
    except Exception as e:
        print(e)
        print(message.from_user)
        await bot.send_message(message.from_user.id,"Ошибка что-то пошло не так!\nКод ошибки сообщите разработчику.\n{}\nhttps://t.me/LarryBrackdown\n@Zubrilka90".format(e),reply_markup=greet_kb)
        await state.finish()
    await state.finish()




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    try:
        if str(message.from_user.id) not in file_base:
            f = open("ids.txt", mode="a+", encoding="utf-8")
            f.write(str(message.from_user.id)+"\n")
            f.close()
        await message.reply("Добро пожаловать, я Парсер Бот.\nПомогу спарсить людей с открытых чатов.\nЕСТЬ ПРИВАТНАЯ ЛИЧНАЯ ВЕРСИЯ ПАРСЕРА ПРИВАТНЫХ И ПУБЛИЧНЫХ ЧАТОВ.\n\nРазработчик:\nhttps://t.me/LarryBrackdown\nhttps://t.me/tlscripts",reply_markup=greet_kb)
    except Exception as e:
        print("e")
        print(message)

@dp.message_handler()
async def cats(message: types.Message):
   try:
     if message.text=="Спарсить чат":
         await OrderFood.parse.set()
         await bot.send_message(message.from_user.id,"Пришли мне юзернейм открытого чата, который нужно спарсить!\nВ таком виде: @nickchata или же https://t.me/nickchata .\n\nСоздано при поддержке : https://t.me/tlscripts",reply_markup=greet_kb)
     if message.text=="Справка":
         await bot.send_message(message.from_user.id,"Нажми на кнопку спарсить чат и пришли ссылку на свой чат.\nБот создан за 20 минут поэтому могут быть баги или глюки.\nРазработчик - https://t.me/LarryBrackdown\nhttps://t.me/tlscripts\nЗанимаюсь под заказ разработкой других ботов,софта и т.д",reply_markup=greet_kb)
   except Exception as e:
       print("e")
       print(message)
       
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
