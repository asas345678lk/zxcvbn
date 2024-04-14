from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import config

# Инициализация бота и диспетчера
bot = Bot(token=config.TOK)
dp = Dispatcher(bot)

# ID чата администратора (замените на реальный ID чата администратора)
ADMIN_CHAT_ID = config.myID

# Ссылка на ваш веб-сайт
WEBSITE_URL = "https://example.com/order_form.html"

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Добро пожаловать! Вы можете оформить заказ, перейдя по ссылке <a href='{WEBSITE_URL}'>здесь</a>.",
                        parse_mode=types.ParseMode.HTML)


# Обработчик команды /order
@dp.message_handler(commands=['order'])
async def place_order(message: types.Message):
    await message.answer(f"Чтобы оформить заказ, перейдите по ссылке <a href='{WEBSITE_URL}'>здесь</a>.",
                         parse_mode=types.ParseMode.HTML)


# Обработчик входящих заказов
@dp.message_handler(content_types=['text'])
async def process_order(message: types.Message):
    order = message.text
    await bot.send_message(ADMIN_CHAT_ID, f"Новый заказ:\n{order}")
    await message.answer("Ваш заказ успешно размещен! Администратор был уведомлен.")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
