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

        await bot.send_photo(chat_id=message.from_user.id, photo=cat_link)

    elif random_count == 2:
        dog_link = requests.get(API_URL_DOG).json()['url']

        await bot.send_photo(chat_id=message.from_user.id, photo=dog_link)

    else:
        fog_link = requests.get(API_URL_FOG).json()['link']

        await bot.send_photo(chat_id=message.from_user.id, photo=fog_link)


dp.message.register(process_start_help_command, Command(commands=["start", "help"]))
dp.message.register(send_echo, Command(commands=["img"]))


if __name__ == "__main__":
    dp.run_polling(bot)
