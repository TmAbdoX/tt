import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message
from JackMusic import app

@app.on_message(command(["/link","لینک","لینك"]) & ~filters.bot & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("**ويت يحب**")
    await message.reply_text(f"**رابط :**\n\n {invitelink}")
