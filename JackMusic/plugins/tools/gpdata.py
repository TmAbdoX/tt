from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from JackMusic import app
from config import OWNER_ID
from JackMusic.misc import SUDOERS
from pyrogram.types import Message
from JackMusic.utils.database import add_served_chat, delete_served_chat
from JackMusic.utils.alina_ban import admin_filter, sudo_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from strings.filters import command





@app.on_message(filters.command(["/pin","ث","تثبيت"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**هذا الامر يعمل فقط في مجموعه!**")
    elif not replied:
        await message.reply_text("**رد علي رساله لتثبيت!**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**تم تثبيت رساله بنجاح!**\n\n**مجموعه:** {chat_title}\n**مسول:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 عرض الرساله", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))



