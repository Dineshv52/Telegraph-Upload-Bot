# Copyright ©️ 2024 . All Rights Reserved Modified By ©️ Team SecurityPanda
""""
Security panda is a Telegram Audio and video streaming bot
Copyright (c) 2023 -present Team=Security Panda <https://github.com/dineshv52>

This program is free software: you can redistribute it and can modify
as you want.
"""

import os
import re
import asyncio
import traceback
from data import PandaData
from pyrogram.errors import FloodWait
from telegraph import upload_file, Telegraph, exceptions
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

chat_watcher_group = 10
telegraph = Telegraph()
telegraph.create_account(short_name="Security Panda")
            
## TEXT UPLOAD THIS MODULE IS OFFICIALLY MADE BY Security Panda
## Use credit if you wanna use this in your project : 
## Copyright (c) 2023 -present Team=Security Panda <https://github.com/dineshv52>

@Client.on_message(filters.command("uploadtxt"))
async def upload_text_telegraph(client, message: Message):
    if not message.reply_to_message and len(message.command) == 1:
        await message.reply_text(PandaData.REPLAY_MSG)
        return
    msg = await message.reply_text(PandaData.UPLOAD_MSG)
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    else:
        text = re.sub(r"/\w+ ", "", message.text)
    try:
        telegraph.create_account(short_name='Security Panda')
        author_url = f'https://telegram.dog/{message.from_user.username}' if message.from_user.id else None
        if len(message.command) > 1:
            security_title = ' '.join(message.command[1:])
        else:
            security_title = 'Uploaded By SecurityPanda Upload Bot'
        
        response = telegraph.create_page(title=security_title, html_content=text, author_name=str(message.from_user.first_name), author_url=author_url)
        generated_link = 'https://telegra.ph/{}'.format(response['path'])
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤩 ᴊᴏɪɴ ᴜs", url="https://t.me/PandaSupportgroup"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🐲", url="https://t.me/Panda_bot_update_channel")
                ],
                [
                    InlineKeyboardButton("🌐 ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
                ]
            ]
        )        
        await msg.edit_text(
            f"🖇️ ʟɪɴᴋ - {generated_link}\n\n<center><a href=https://youtube.com/@SecurityInsiders?si=SHli-_QHka6cK62T style=color:red;>sᴜʙsᴄʀɪʙᴇ ᴏɴ ʏᴏᴜᴛᴜʙᴇ</a></center>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    except Exception as e:
        await msg.edit_text(f"Error: {str(e)}")


## UPLOADING FROM GROUP

@Client.on_message(filters.group & filters.command('upload'))
async def upload_to_telegraph(bot, message):
    reply = message.reply_to_message
    TEMP_DICT = 'temp/'
    filesize = 5242880
    if not reply:
        await bot.send_message(
            message.chat.id, 
            text=PandaData.UPLOAD_MSG2, 
            parse_mode="markdown"
        )
    # replied to media
    elif reply.media:
        if (
            reply.photo and reply.photo.file_size <= filesize or  # png, jpg, jpeg
            reply.video and reply.video.file_size <= filesize or  # mp4
            reply.animation and reply.animation.file_size <= filesize or
            reply.sticker and reply.sticker.file_size <= filesize or
            reply.document and reply.document.file_size <= filesize  # [photo, video] document
        ):
            msg = await bot.send_message(
                message.chat.id, 
                text=PandaData.HOLD_MSG, 
                parse_mode="markdown"
            )
            # change ext to png to use convert in link
            if reply.animation or reply.sticker:
                loc = await bot.download_media(
                    reply, file_name=f"{TEMP_DICT}/telegraph.png"
                )
            else:
                loc = await bot.download_media(reply)
            try:
                response = upload_file(loc)
            except Exception as e:
                return await bot.send_message(
                    message.chat.id,
                    text=str(e),
                    parse_mode="markdown"
                )
            generated_link = 'https://telegra.ph/{}'.format(response[0])
            IN_BUTTON = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤩 ᴊᴏɪɴ ᴜs", url="https://t.me/bugbountyhunt"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🐲", url="https://t.me/Panda_bot_update_channel")
                    ],
                    [
                        InlineKeyboardButton("🌐 ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
                    ]
                ]
            )
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=msg.message_id,
                text=f"🖇️ ʟɪɴᴋ - {generated_link}\n\n<center><a href=https://youtube.com/@SecurityInsiders?si=SHli-_QHka6cK62T style=color:red;>sᴜʙsᴄʀɪʙᴇ ᴏɴ ʏᴏᴜᴛᴜʙᴇ</a></center>",
                reply_markup=IN_BUTTON,
                disable_web_page_preview=True,
                parse_mode="html"
            )
            if os.path.exists(loc):
                os.remove(loc)
        else:
            await bot.send_message(
                message.chat.id,
                text=PandaData.ERROR_MSG,
                parse_mode="markdown"
            )
    else:
        # if replied to unsupported media
        await bot.send_message(
            message.chat.id, 
            text=PandaData.FILE_ERROR, 
            parse_mode="markdown"
        )
