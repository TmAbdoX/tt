from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from unidecode import unidecode
from strings.filters import command
from JackMusic import app
from JackMusic.misc import SUDOERS
from JackMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(command(["/ac","/av","المكالمات"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(f"<b>✫ المكالمات النشطه :</b>\n\n<b>صوت : {ac_audio}\nفيديو : {ac_video}</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('✯ مسح ✯', callback_data=f"close")]]))
