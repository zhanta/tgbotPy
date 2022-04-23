from aiogram import types
from dispatcher import dp
import config

@dp.message_handler(is_owner=True, commands=["setlink"])
async def setlink_command(message: types.Message):
    with open("link.txt", "w+") as f:
        f.write(message.text.replace("/setlink ", "").strip())
        f.close()
    await message.answer("Link has been saved")

@dp.message_handler(is_owner=True, commands=["getlink"])
async def getlink_command(message: types.Message):
    with open("link.txt", "r") as f:
        content = f.readlines()
        f.close()
    await message.answer("Link is: {}".format(content[0].strip()))
