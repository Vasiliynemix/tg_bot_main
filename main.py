import requests
import random
from config import *
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime
API_URL_CAT: str = "https://aws.random.cat/meow"
API_URL_DOG: str = "https://random.dog/woof.json"
API_URL_FOG: str = "https://randomfox.ca/floof/"
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


async def process_start_help_command(message: Message):
    user_id = message.from_user.id
    print(user_id)
    await message.answer("Напиши мне что-нибудь и я отправлю тебе картинку=)")


async def send_echo(message: Message):

    user_id = message.from_user.id
    print(user_id)

    random_count = random.randint(1, 3)
    current_datetime = datetime.now()

    if random_count == 1:
        cat_link = requests.get(API_URL_CAT).json()['file']

        # начало для леры
        if user_id == lera_id or user_id == my_id:
            if current_datetime.hour == 23 or current_datetime.hour == 00:
                await bot.send_message(lera_id, "Лови котика перед сном=)<3")
            else:
                await bot.send_message(lera_id, "Котик в любое время дня и ночи специально для Леры<3 наслаждайся!")
            await bot.send_sticker(chat_id=lera_id,
                                   sticker=r"CAACAgIAAxkBAAEIQW5kHKQTv3YJ1eLwiTqeBirQHAb9uAACsgAD98zUGN0m4YqZQUzILwQ")
            await bot.send_photo(chat_id=lera_id, photo=cat_link)
            if current_datetime.hour == 23 or current_datetime.hour == 00:
                await bot.send_message(lera_id, "Спи спокойно и сладко, котик присмотрит за тобой=)")
        # конец для леры

        await bot.send_photo(chat_id=message.from_user.id, photo=cat_link)

    elif random_count == 2:
        dog_link = requests.get(API_URL_DOG).json()['url']

        # начало для леры
        if user_id == lera_id or user_id == my_id:
            if current_datetime.hour == 23 or current_datetime.hour == 00:
                await bot.send_message(lera_id, "Лови собачку перед сном=)<3")
            else:
                await bot.send_message(lera_id, "Собачка в любое время дня и ночи специально для Леры<3 наслаждайся!")
            await bot.send_sticker(chat_id=lera_id,
                                   sticker=r"CAACAgIAAxkBAAEIQW5kHKQTv3YJ1eLwiTqeBirQHAb9uAACsgAD98zUGN0m4YqZQUzILwQ")
            await bot.send_photo(chat_id=lera_id, photo=dog_link)
            if current_datetime.hour == 23 or current_datetime.hour == 00:
                await bot.send_message(lera_id, "Спи спокойно и сладко, собачка присмотрит за тобой=)")
        # конец для леры

        await bot.send_photo(chat_id=message.from_user.id, photo=dog_link)

    else:
        fog_link = requests.get(API_URL_FOG).json()['link']

        # начало для леры
        if user_id == lera_id or user_id == my_id:
            if current_datetime.hour == 23 or current_datetime.hour == 00:
                await bot.send_message(lera_id, "Лови лисичка перед сном=)<3")
            else:
                await bot.send_message(lera_id, "Лисичка в любое время дня и ночи специально для Леры<3 наслаждайся!")
            await bot.send_sticker(chat_id=lera_id,
                                   sticker=r"CAACAgIAAxkBAAEIQW5kHKQTv3YJ1eLwiTqeBirQHAb9uAACsgAD98zUGN0m4YqZQUzILwQ")
            await bot.send_photo(chat_id=lera_id, photo=fog_link)
            if current_datetime.hour == 23 or current_datetime.hour == 00:
                await bot.send_message(lera_id, "Спи спокойно и сладко, лисичка присмотрит за тобой=)")
        # конец для леры

        await bot.send_photo(chat_id=message.from_user.id, photo=fog_link)


dp.message.register(process_start_help_command, Command(commands=["start", "help"]))
dp.message.register(send_echo, Command(commands=["img"]))


if __name__ == "__main__":
    dp.run_polling(bot)
