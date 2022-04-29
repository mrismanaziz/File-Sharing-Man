# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL:
        if not FORCE_SUB_GROUP:
            buttons = [
                [
                    InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                    InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
                ],
            ]
            return buttons
        buttons = [
            [
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐉𝐨𝐢𝐧 𝐛𝐨𝐬𝐐", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐉𝐨𝐢𝐧 𝐛𝐨𝐬𝐐", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝐋𝐚𝐧𝐣𝐮𝐭 𝐁𝐨𝐬𝐐",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝐋𝐚𝐧𝐣𝐮𝐭 𝐁𝐨𝐬𝐐",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
