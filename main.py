import requests
import random
from config import *
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
API_URL_CAT: str = "https://aws.random.cat/meow"
API_URL_DOG: str = "https://random.dog/woof.json"
API_URL_FOG: str = "https://randomfox.ca/floof/"

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start', 'help']))
async def process_start_help_command(message: Message):
    user_id = message.from_user.id
    print(user_id)
    await message.answer("Напиши мне что-нибудь и я отправлю тебе картинку=)")


@dp.message()
async def send_cat(message: Message):
    user_id = message.from_user.id
    print(user_id)
    random_count = random.randint(1, 3)
    if random_count == 1:
        cat_link = requests.get(API_URL_CAT).json()['file']
        if user_id == lera_id:
            await bot.send_message(lera_id, "Картинка котика специально для Леры <3 наслаждайся!")
            await bot.send_sticker(chat_id=lera_id,
                                   sticker=r"CAACAgIAAxkBAAEIQW5kHKQTv3YJ1eLwiTqeBirQHAb9uAACsgAD98zUGN0m4YqZQUzILwQ")
        await bot.send_photo(chat_id=lera_id, photo=cat_link)
        await bot.send_photo(chat_id=message.from_user.id, photo=cat_link)
    elif random_count == 2:
        dog_link = requests.get(API_URL_DOG).json()['url']
        if user_id == lera_id or user_id == my_id:
            await bot.send_message(lera_id, "Картинка котика специально для Леры <3 наслаждайся!")
            await bot.send_sticker(chat_id=lera_id,
                                   sticker=r"CAACAgIAAxkBAAEIQW5kHKQTv3YJ1eLwiTqeBirQHAb9uAACsgAD98zUGN0m4YqZQUzILwQ")
        await bot.send_photo(chat_id=lera_id, photo=dog_link)
        await bot.send_photo(chat_id=message.from_user.id, photo=dog_link)
    else:
        fog_link = requests.get(API_URL_FOG).json()['link']
        if user_id == lera_id or user_id == my_id:
            await bot.send_message(lera_id, "Картинка котика специально для Леры <3 наслаждайся!")
            await bot.send_sticker(chat_id=lera_id,
                                   sticker=r"CAACAgIAAxkBAAEIQW5kHKQTv3YJ1eLwiTqeBirQHAb9uAACsgAD98zUGN0m4YqZQUzILwQ")
        await bot.send_photo(chat_id=lera_id, photo=fog_link)
        await bot.send_photo(chat_id=message.from_user.id, photo=fog_link)


if __name__ == "__main__":
    dp.run_polling(bot)
