import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from JackMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)
from JackMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/tmjack1/12",
        caption=f"- 𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐌𝐮𝐬𝐢𝐜 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                   "𝗚𝗥𝗼𝘂𝗽", url=f"https://t.me/Q_W_Q_V"), 
                 InlineKeyboardButton(
                   "𝗧𝗲𝗺 𝗘𝘃𝗮",  url=f"https://t.me/s_u_s_l"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "𝗘𝘃𝗮", url=f"https://t.me/SO_AM0"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text="𖥻 𝐀𝐝𝐃 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐔𝐫 𝐆𝐫𝐎𝐮𝐏 .",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )


@app.on_message(filters.command(["مطور السورس","ايفا"], ""), group=73) 
async def deev(client: Client, message: Message):
     user = await client.get_chat(chat_id="SO_AM0")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"هناك شخص بالحاجه اليك عزيزي المطور\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝙽𝚊𝚖𝚎 : {name} \n𝚍𝚎𝚟 𝚞𝚜𝚎𝚛 𝚗𝚊𝚖𝚎 : @{username}\n{bio}",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
