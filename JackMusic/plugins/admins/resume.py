from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from JackMusic import app
from JackMusic.core.call import Alina
from JackMusic.utils.database import is_music_playing, music_on
from JackMusic.utils.decorators import AdminRightsCheck
from JackMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(command(["resume", "cresume","/resume","/cresume","كملي","كمل"]) & ~filters.private & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    user_mention = message.from_user.mention if message.from_user else "𝖠𝖽𝗆𝗂𝗇"
    await Alina.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(user_mention), reply_markup=close_markup(_)
    )
