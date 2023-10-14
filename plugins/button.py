#CodeXBotz #mrismanaziz

from config import(
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
)
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if (
        not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1 
        and not FORCE_SUB_2 
        and not FORCE_SUB_3 
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2 
        and not FORCE_SUB_1 
        and not FORCE_SUB_3 
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_3
        and not FORCE_SUB_1 
        and not FORCE_SUB_2 
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_4 
        and not FORCE_SUB_1 
        and not FORCE_SUB_2
        and not FORCE_SUB_3 
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and not FORCE_SUB_2
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_4
        and not FORCE_SUB_2
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Bantuan",
                    callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 4",
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data="Tutup"
                ),
            ],
        ]
        return buttons


def fsub_button(client, message):
    if (
        FORCE_SUB_1
        and not FORCE_SUB_2 
        and not FORCE_SUB_3 
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and not FORCE_SUB_1 
        and not FORCE_SUB_3 
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink2
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_3
        and not FORCE_SUB_1 
        and not FORCE_SUB_2 
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_4
        and not FORCE_SUB_1 
        and not FORCE_SUB_2 
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and not FORCE_SUB_2
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_4
        and not FORCE_SUB_2
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="Join 1",
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="Join 2",
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Join 3",
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="Join 4",
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons