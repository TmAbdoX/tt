import random

from pyrogram import filters
from pyrogram.types import Message

from JackMusic  import app
from JackMusic.misc import db
from JackMusic.utils.decorators import AdminRightsCheck
from JackMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["shuffle", "cshuffle"]) & ~filters.private & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    user_mention = message.from_user.mention if message.from_user else "𝖠𝖽𝗆𝗂𝗇"
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_16"].format(user_mention), reply_markup=close_markup(_)
    )
