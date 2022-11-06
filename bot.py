import logging
import parser
import env_loader
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = env_loader.get('API_TOKEN')
PROXY_URL = env_loader.get('PROXY_URL')

logging.basicConfig(level=logging.INFO)

if PROXY_URL != "":
    bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
else:
    bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я умею качать видео из статей на kp.ru.\n"
                         "Отправь мне ссылку на статью, а я пришлю видео.")


@dp.message_handler()
async def send_video(message: types.Message):
    video = parser.get_video(message.text)
    if not video.is_exists():
        await message.answer("В статье нет видео")
    else:
        await message.answer("Подожди, видео загружается")
        await bot.send_video(message.chat.id, video.stream())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
