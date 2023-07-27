import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile

from preprocessing.preprocess import preprocess
from sd_api import inpaint

# Bot token can be obtained via https://t.me/BotFather
#API_TOKEN = os.environ["API_TOKEN"]
API_TOKEN = "1858827137:AAFZVaKOjAhjVyCXfiGgL-SK6dp7_lILZIE"

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(API_TOKEN, parse_mode="HTML")

@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@router.message(F.photo)
async def generate_handler(message: types.Message) -> None:
    photos = message.photo
    if not photos:
        await message.answer_dice("🎯")
        return

    photo_info = photos[-1]
    file_info = await bot.get_file(photo_info.file_id)
    photo = await bot.download_file(file_info.file_path)
    image = photo.read()
    
    # getting mask
    mask = preprocess(image)

    # getting result image
    result_image = await inpaint(image, mask)
    result_image = BufferedInputFile(result_image, "lmao.png")

    await message.answer_photo(result_image)


# Dispatcher is a root router
dp = Dispatcher()
# ... and all other routers should be attached to Dispatcher
dp.include_router(router)

async def main():
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
