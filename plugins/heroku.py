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

import asyncio
import os
import socket
from base64 import b64decode
from datetime import datetime

import aiohttp
import dotenv
import heroku3
import urllib3
from bot import Bot
from config import ADMINS, HEROKU_API_KEY, HEROKU_APP_NAME, UPSTREAM_BRANCH
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
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


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def Paste(text):
    resp = await post(f"https://batbin.me/api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link


@Bot.on_message(filters.command("get_var") & filters.user(ADMINS))
async def varget_(client: Bot, message: Message):
    if len(message.command) != 2:
        configvars = heroku_config.to_dict()
        msg = "".join(f"<code>{item}</code> = <code>{configvars[item]}</code>\n" for item in configvars)
        await message.reply_text(msg)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"<b>{check_var}:</b> <code>{heroku_config[check_var]}</code>"
            )
        else:
            return await message.reply_text("Unable to find any such var.")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env file not found.")
        output = dotenv.get_key(path, check_var)
        if not output:
            await message.reply_text("Unable to find any such var.")
        else:
            return await message.reply_text(f"<b>{check_var}:</b> <code>{str(output)}</code>")


@Bot.on_message(filters.command("del_var") & filters.user(ADMINS))
async def vardel_(client: Bot, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("<b>Usage:</b>\n/del_var [Var Name]")
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            await message.reply_text(f"{check_var} Deleted.")
            del heroku_config[check_var]
        else:
            return await message.reply_text("Unable to find any such var.")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env file not found.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text("Unable to find any such var.")
        else:
            await message.reply_text(f"{check_var} Deleted.")
            os.system(f"kill -9 {os.getpid()} && bash start")


@Bot.on_message(filters.command("set_var") & filters.user(ADMINS))
async def set_var(client: Bot, message: Message):
    if len(message.command) < 3:
        return await message.reply_text("<b>Usage:</b>\n/set_var [Var Name] [Var Value]")
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = HAPP.config()
        if to_set in heroku_config:
            await message.reply_text(f"{to_set} has been updated successfully")
        else:
            await message.reply_text(f"{to_set} has been added successfully")
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env file not found.")
        dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            await message.reply_text(f"{to_set} has been updated successfully")
        else:
            await message.reply_text(f"{to_set} has been added successfully")
        os.system(f"kill -9 {os.getpid()} && bash start")


@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_(client: Bot, message: Message):
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
    response = await message.reply_text("Checking for available updates...")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("Git Command Error")
    except InvalidGitRepositoryError:
        return await response.edit("Invalid Git Repsitory")
    to_exc = f"git fetch origin {UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]
    for checks in repo.iter_commits(f"HEAD..origin/{UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("Bot is up-to-date!")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ Commited on:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n<b><u>Updates:</u></b>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await Paste(updates)
        nrs = await response.edit(
            f"<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n<b><u>Updates:</u></b>\n\n[Click Here to checkout Updates]({url})"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")
    if await is_heroku():
        try:
            await response.edit(
                f"{nrs.text}\n\nBot was updated successfully on Heroku! Now, wait for 2 - 3 mins until the bot restarts!"
            )
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(
                f"{nrs.text}\n\nSomething went wrong while initiating reboot! Please try again later or check logs for more info."
            )
            return await client.send_message(
                client.db_channel,
                f"AN EXCEPTION OCCURRED AT #UPDATER DUE TO: <code>{err}</code>",
            )
    else:
        await response.edit(
            f"{nrs.text}\n\nBot was updated successfully! Now, wait for 1 - 2 mins until the bot reboots!"
        )
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start")
        exit()
