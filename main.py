import aiogram
import asyncio
from dotenv import load_dotenv
import os

# Загрузите переменные окружения из файла .env
load_dotenv()

# Получите токен
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
if bot_token is None:
    raise RuntimeError('Не удалось получить токен из переменных окружения')

# Получаем ID администратора
admin_user_id = os.getenv('ADMIN_ID')
if admin_user_id is None:
    raise RuntimeError('Не удалось получить user ID из переменных окружения')

# Инициализируем бот
bot = aiogram.Bot(token=bot_token)

# Инициализируем диспечер
dp = aiogram.Dispatcher(bot)

async def handle_message(message: aiogram.types.Message):
    user_id = message.from_user.id  # Получаем ID пользователя
    # Проверяем, является ли пользователь доверенным
    if str(user_id) != admin_user_id:
        await message.reply("Извините, у вас нет доступа к этому боту.")
        return

    # (Ваш код обработки сообщений здесь, например, эхо-ответ)
    await message.reply(message.text)

# Register the message handler function
dp.register_message_handler(handle_message)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())