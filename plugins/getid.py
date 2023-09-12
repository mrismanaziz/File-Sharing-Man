"""Get id of the replied user
Syntax: /id"""

from pyrogram import filters
from pyrogram.types import Message

from bot import Bot


@Bot.on_message(filters.command("id") & filters.private)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(
            f"<b>User ID anda adalah:</b> <code>{user_id}</code>", quote=True
        )
