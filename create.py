
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL


mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client['file_sharing_bot']

users_collection = db['users']


@Client.on_message(filters.private & filters.command('start'))
async def start(bot, update):
    user_id = update.from_user.id
    user_exists = users_collection.find_one({'user_id': user_id})

    # Jika pengguna sudah terdaftar, tidak perlu meminta informasi lagi
    if user_exists:
        bot.send_message(
            chat_id=user_id,
            text="Anda sudah terdaftar sebagai pengguna bot.",
        )
        return

    # Jika pengguna belum terdaftar, meminta informasi pengguna
    bot.send_message(
        chat_id=user_id,
        text="Silakan masukkan informasi Anda untuk mendaftar sebagai pengguna bot."
    )

    # Mengatur parameter untuk mendapatkan informasi pengguna selanjutnya
    bot.set_next_step(
        chat_id=user_id,
        step='APP_ID',
        text="Masukkan API ID Anda:"
    )


# Fungsi untuk memproses langkah-langkah selanjutnya dalam pendaftaran pengguna
@Client.on_message(filters.private & filters.text)
async def process_user_info(bot, update):
    user_id = update.from_user.id
    step = bot.get_current_step(chat_id=user_id)

    if step == 'APP_ID':
        APP_ID = int(update.text)
        bot.set_next_step(
            chat_id=user_id,
            step='API_HASH',
            text="Masukkan API Hash Anda:"
        )
        bot.save_next_step(chat_id=user_id, step_data={'APP_ID': APP_ID})

    elif step == 'API_HASH':
        API_HASH = update.text
        bot.set_next_step(
            chat_id=user_id,
            step='CHANNEL_ID',
            text="Masukkan ID Channel:"
        )
        bot.save_next_step(chat_id=user_id, step_data={'API_HASH': API_HASH})

    elif step == 'CHANNEL_ID':
        CHANNEL_ID = int(update.text)
        bot.set_next_step(
            chat_id=user_id,
            step='TG_BOT_TOKEN',
            text="Masukkan Bot Token:"
        )
        bot.save_next_step(chat_id=user_id, step_data={'CHANNEL_ID': CHANNEL_ID})

    elif step == 'TG_BOT_TOKEN':
        TG_BOT_TOKEN = update.text
        bot.set_next_step(
            chat_id=user_id,
            step='ADMINS',
            text="Masukkan ID Admin (pisahkan dengan spasi jika lebih dari satu):"
        )
        bot.save_next_step(chat_id=user_id, step_data={'TG_BOT_TOKEN': TG_BOT_TOKEN})

    elif step == 'ADMINS':
        ADMINS = update.text.split()
        bot.set_next_step(
            chat_id=user_id,
            step='FORCE_SUB_GROUP',
            text="Masukkan ID Group yang akan dipaksa berlangganan (0 jika tidak ada):"
        )
        bot.save_next_step(chat_id=user_id, step_data={'ADMINS': ADMINS})

    elif step == 'FORCE_SUB_GROUP':
        FORCE_SUB_GROUP = int(update.text)
        bot.set_next_step(
            chat_id=user_id,
            step='FORCE_SUB_CHANNEL',
            text="Masukkan ID Channel yang akan dipaksa berlangganan (0 jika tidak ada):"
        )
        bot.save_next_step(chat_id=user_id, step_data={'FORCE_SUB_GROUP': FORCE_SUB_GROUP})

    elif step == 'FORCE_SUB_CHANNEL':
        FORCE_SUB_CHANNEL = int(update.text)
        bot.set_next_step(
            chat_id=user_id,
            step='DATABASE_URI',
            text="Masukkan informasi DATABASE SQL:"
        )
        bot.save_next_step(chat_id=user_id, step_data={'FORCE_SUB_CHANNEL': FORCE_SUB_CHANNEL})

    elif step == 'DATABASE_URI':
        DB_URI = update.text
        step_data = bot.get_step_data(chat_id=user_id)
        APP_ID = step_data['APP_ID']
        API_HASH = step_data['API_HASH']
        CHANNEL_ID = step_data['CHANNEL_ID']
        TG_BOT_TOKEN = step_data['TG_BOT_TOKEN']
        ADMINS = step_data['ADMINS']
        FORCE_SUB_GROUP = step_data['FORCE_SUB_GROUP']
        FORCE_SUB_CHANNEL = step_data['FORCE_SUB_CHANNEL']

        # Menyimpan informasi pengguna ke dalam database
        save_user_info(
            user_id=user_id,
            APP_ID=APP_ID,
            API_HASH=API_HASH,
            CHANNEL_ID=CHANNEL_ID,
            TG_BOT_TOKEN=TG_BOT_TOKEN,
            ADMINS=ADMINS,
            FORCE_SUB_GROUP=FORCE_SUB_GROUP,
            FORCE_SUB_CHANNEL=FORCE_SUB_CHANNEL,
            DB_URI=DATABASE_URL
        )

        bot.send_message(
            chat_id=user_id,
            text="Anda telah terdaftar sebagai pengguna bot. Terima kasih!"
        )

        # Membuat tombol untuk membuat bot file sharing
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Buat Bot File Sharing",
                        callback_data="create_file_sharing_bot"
                    )
                ]
            ]
        )
        bot.send_message(
            chat_id=user_id,
            text="Klik tombol di bawah untuk membuat bot file sharing.",
            reply_markup=markup
        )


# Fungsi untuk menangani pemilihan tombol "Buat Bot File Sharing"
@Client.on_callback_query(filters.callback_data("create_file_sharing_bot"))
async def create_fileSharing_bot(bot, update):
    query = update.callback_query
    user_id = query.from_user.id
    user_info = users_collection.find_one({'user_id': user_id})

    APP_ID = user_info['APP_ID']
    API_HASH = user_info['API_HASH']
    CHANNEL_ID = user_info['CHANNEL_ID']
    TG_BOT_TOKEN = user_info['TG_BOT_TOKEN']
    ADMINS = user_info['ADMINS']
    FORCE_SUB_GROUP = user_info['FORCE_SUB_GROUP']
    FORCE_SUB_CHANNEL = user_info['FORCE_SUB_CHANNEL']
    database_sql = user_info['database_sql']

    file_sharing_bot_config = {
        'user_id': user_id,
        'APP_ID': APP_ID,
        'API_HASH': API_HASH,
        'CHANNEL_ID': CHANNEL_ID,
        'TG_BOT_TOKEN': TG_BOT_TOKEN,
        'ADMINS': ADMINS,
        'FORCE_SUB_GROUP': FORCE_SUB_GROUP,
        'FORCE_SUB_CHANNEL': FORCE_SUB_CHANNEL,
        'DATABASE_URL': DB_URI
    }
    file_sharing_bot_collection = db['file_sharing_bot']
    file_sharing_bot_collection.insert_one(file_sharing_bot_config)

    bot.send_message(
        chat_id=user_id,
        text="Bot file sharing telah berhasil dibuat!"
)
