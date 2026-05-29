import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "8047245006:AAHKIqzHA1MGOv5BpopeYEJlDz5AVnpzQ24"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Fun jokes list
JOKES = [
    "Why don’t programmers like nature? Too many bugs 🐛",
    "I told my computer I needed a break… it said ‘No problem, I’ll go to sleep’ 😴",
    "Why do Java developers wear glasses? Because they don’t C# 👓",
]

# Inline keyboard
def fun_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="😂 Joke", callback_data="joke")],
        [InlineKeyboardButton(text="🎲 Dice", callback_data="dice")]
    ])


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Hello! I'm a fun bot!\nChoose something 👇",
        reply_markup=fun_keyboard()
    )


@dp.message(Command("joke"))
async def joke_cmd(message: Message):
    await message.answer(random.choice(JOKES))


@dp.message(Command("dice"))
async def dice_cmd(message: Message):
    value = random.randint(1, 6)
    await message.answer(f"🎲 You rolled: {value}")


@dp.callback_query(F.data == "joke")
async def callback_joke(call: CallbackQuery):
    await call.message.answer(random.choice(JOKES))
    await call.answer()


@dp.callback_query(F.data == "dice")
async def callback_dice(call: CallbackQuery):
    value = random.randint(1, 6)
    await call.message.answer(f"🎲 You rolled: {value}")
    await call.answer()


@dp.message()
async def echo(message: Message):
    await message.answer(f"😄 You said: {message.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())