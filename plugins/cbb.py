# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER, START_MSG


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    buttons = [
        [InlineKeyboardButton("• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about")],
        [
            InlineKeyboardButton("𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=client.invitelink),
            InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣", url=client.invitelink2),
        ],
        [
            InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close"),
        ],
    ]
    if data == "home":
        await query.message.edit_text(
            text=START_MSG.format(
                first=query.from_user.first_name,
                last=query.from_user.last_name,
                username=None
                if not query.from_user.username
                else "@" + query.from_user.username,
                mention=query.from_user.mention,
                id=query.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
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
