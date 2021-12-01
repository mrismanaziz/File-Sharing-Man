# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from bot import Bot
from config import CHANNEL, GROUP, OWNER
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>• Owner: @{OWNER}</a>\n• Channel: @{CHANNEL}\n• Group: @{GROUP}</b>\n<b>• Source Code: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>Klik Disini</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
