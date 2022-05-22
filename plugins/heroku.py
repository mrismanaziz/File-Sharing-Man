#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
# Ported by @mrismanaziz
# FROM File-Sharing-Man < https://github.com/mrismanaziz/File-Sharing-Man/ >
# t.me/Lunatic0de & t.me/SharingUserbot
#

import os
import socket

import dotenv
import heroku3
import urllib3
from bot import Bot
from config import ADMINS, HEROKU_API_KEY, HEROKU_APP_NAME
from pyrogram import filters
from pyrogram.types import Message

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    HAPP = Heroku.app(HEROKU_APP_NAME)
    heroku_config = HAPP.config()
else:
    HAPP = None

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


async def is_heroku():
    return "heroku" in socket.getfqdn()


@Bot.on_message(filters.command("getvar") & filters.user(ADMINS))
async def varget_(client: Bot, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("<b>Usage:</b>\n/getvar [Var Name]")
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
            )
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"<b>{check_var}:</b> <code>{heroku_config[check_var]}</code>"
            )
        else:
            return await message.reply_text(f"Tidak dapat menemukan var {check_var}")
    else:
        path = dotenv.find_dotenv("config.env")
        if not path:
            return await message.reply_text(".env file not found.")
        if output := dotenv.get_key(path, check_var):
            return await message.reply_text(
                f"<b>{check_var}:</b> <code>{str(output)}</code>"
            )
        else:
            await message.reply_text(f"Tidak dapat menemukan var {check_var}")


@Bot.on_message(filters.command("delvar") & filters.user(ADMINS))
async def vardel_(client: Bot, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("<b>Usage:</b>\n/delvar [Var Name]")
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
            )
        heroku_config = HAPP.config()
        if check_var not in heroku_config:
            return await message.reply_text(f"Tidak dapat menemukan var {check_var}")
        await message.reply_text(f"Berhasil Menghapus var {check_var}")
        del heroku_config[check_var]
    else:
        path = dotenv.find_dotenv("config.env")
        if not path:
            return await message.reply_text(".env file not found.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text(f"Tidak dapat menemukan var {check_var}")
        await message.reply_text(f"Berhasil Menghapus var {check_var}")
        os.system(f"kill -9 {os.getpid()} && bash start")


@Bot.on_message(filters.command("setvar") & filters.user(ADMINS))
async def set_var(client: Bot, message: Message):
    if len(message.command) < 3:
        return await message.reply_text("<b>Usage:</b>\n/setvar [Var Name] [Var Value]")
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
            )
        heroku_config = HAPP.config()
        if to_set in heroku_config:
            await message.reply_text(f"Berhasil Mengubah var {to_set} menjadi {value}")
        else:
            await message.reply_text(
                f"Berhasil Menambahkan var {to_set} menjadi {value}"
            )
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv("config.env")
        if not path:
            return await message.reply_text(".env file not found.")
        dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            await message.reply_text(f"Berhasil Mengubah var {to_set} menjadi {value}")
        else:
            await message.reply_text(
                f"Berhasil Menambahkan var {to_set} menjadi {value}"
            )
        os.system(f"kill -9 {os.getpid()} && bash start")
