import asyncio
import time
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

from JackMusic import app
from JackMusic.core.call import Alina
from JackMusic.misc import db
from JackMusic.utils.database import get_assistant, get_authuser_names, get_cmode
from JackMusic.utils.decorators import ActualAdminCB, AdminActual, language
from JackMusic.utils.formatters import alpha_to_int, get_readable_time
from config import BANNED_USERS, adminlist, lyrical
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
from dotenv import load_dotenv

rel = {}


@app.on_message(
    filters.command(["admincache", "reload", "refresh", "ريلود"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        if message.chat.id not in rel:
            rel[message.chat.id] = {}
        else:
            saved = rel[message.chat.id]
            if saved > time.time():
                left = get_readable_time((int(saved) - int(time.time())))
                return await message.reply_text(_["reload_1"].format(left))
        adminlist[message.chat.id] = []
        async for user in app.get_chat_members(
            message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if user.privileges.can_manage_video_chats:
                adminlist[message.chat.id].append(user.user.id)
        authusers = await get_authuser_names(message.chat.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[message.chat.id].append(user_id)
        now = int(time.time()) + 180
        rel[message.chat.id] = now
        await message.reply_text(_["reload_2"])
    except:
        await message.reply_text(_["reload_3"])


@app.on_message(filters.command(["reboot"]) & filters.group & ~BANNED_USERS)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(_["reload_4"].format(app.mention))
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await DAXX.stop_stream_force(message.chat.id)
    except:
        pass
    userbot = await get_assistant(message.chat.id)
    try:
        if message.chat.username:
            await userbot.resolve_peer(message.chat.username)
        else:
            await userbot.resolve_peer(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            got = await app.get_chat(chat_id)
        except:
            pass
        userbot = await get_assistant(chat_id)
        try:
            if got.username:
                await userbot.resolve_peer(got.username)
            else:
                await userbot.resolve_peer(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await DAXX.stop_stream_force(chat_id)
        except:
            pass
    return await mystic.edit_text(_["reload_5"].format(app.mention))



    

