# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import pyromod.listen
import sys

from pyrogram import Client, enums

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys.exit()

        if FORCE_SUB_1:
            try:
                info = await self.get_chat(FORCE_SUB_1)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = info.invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_1 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} "
                    "menjadi Admin di FORCE_SUB_1\n\n"
                )
                sys.exit()
        if FORCE_SUB_2:
            try:
                info = await self.get_chat(FORCE_SUB_2)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_2)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_2 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} "
                    "menjadi Admin di FORCE_SUB_2\n\n"
                )
                sys.exit()
        if FORCE_SUB_3:
            try:
                info = await self.get_chat(FORCE_SUB_3)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = info.invite_link
                self.invitelink3 = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_3 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} "
                    "menjadi Admin di FORCE_SUB_3\n\n"
                )
                sys.exit()
        if FORCE_SUB_4:
            try:
                info = await self.get_chat(FORCE_SUB_4)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_4)
                    link = info.invite_link
                self.invitelink4 = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_4 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} "
                    "menjadi Admin di FORCE_SUB_4\n\n"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message", disable_notification=True)
            await test.delete()
            self.LOGGER(__name__).info(
                f"CHANNEL_ID Database detected!\n┌ Title: {db_channel.title}\n└ Chat ID: {db_channel.id}\n——"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan @{self.username} adalah admin di Channel DataBase anda, CHANNEL_ID Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys.exit()

        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\n\nBOT Dibuat oleh @{OWNER}\nJika @{OWNER} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/SharingUserbot"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
