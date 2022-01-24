from pyrogram import Client
from pyrogram.types import (CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message)
from config import ADMINS, FORCE_SUB_CHANNEL, FORCE_SUB_GROUP


def start_button(client: Client, message: Message):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ᴛᴜᴛᴜᴘ •", callback_data="close"
                )
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝗚𝗥𝗢𝗨𝗣", url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ᴛᴜᴛᴜᴘ •", callback_data="close"
                )
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=client.invitelink
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ᴛᴜᴛᴜᴘ •", callback_data="close"
                )
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="𝗚𝗥𝗢𝗨𝗣", url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ᴛᴜᴛᴜᴘ •", callback_data="close"
                )
            ],
        ]
        return buttons
