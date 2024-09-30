from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from JackMusic import app
from JackMusic.core.call import Alina
from JackMusic.utils.database import set_loop
from JackMusic.utils.decorators import AdminRightsCheck
from JackMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    command(["stop", "end", "cstop", "cend", "انهاء", "/end", "/stop", "ايقاف", "/cend", "/cstop"]) & ~filters.private & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Alina.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    user_mention = message.from_user.mention if message.from_user else "𝖠𝖽𝗆𝗂𝗇"
    await message.reply_text(
        _["admin_5"].format(user_mention), reply_markup=close_markup(_)
    )
