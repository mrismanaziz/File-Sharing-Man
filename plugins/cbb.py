# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from bot import Bot
from config import CHANNEL, GROUP, OWNER, START_MSG


@Bot.on_callback_query()
async def cb_handler(message: Message, query: CallbackQuery):
    message.from_user.id
    "@" + message.from_user.username if message.from_user.username else None
    data = query.data
    if data == "home":
        await query.message.edit_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None
                if not message.from_user.username
                else "@" + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]]
            ),
            disable_web_page_preview=True,
            quote=True,
        )
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n • Owner: @{OWNER}\n • Channel: @{CHANNEL}\n • Group: @{GROUP}\n • Source Code: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>Klik Disini</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴋᴇᴍʙᴀʟɪ", callback_data="home")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
