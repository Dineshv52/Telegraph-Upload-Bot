# Copyright ©️ 2024 Security Panda. All Rights Reserved Modified By ©️ Team Security Panda
""""
Panda telegraph upload bot is a Telegram Audio and video streaming bot
Copyright (c) 2023 -present Team=Security Panda <https://github.com/dineshv52>

This program is free software: you can redistribute it and can modify
as you want.
"""

import os
import re
import asyncio
import traceback
from data import PandaData
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TeamAlexa.database.AlexaDB import get_telegraph_users, get_telegraph_chats, add_telegraph_chat



chat_watcher_group = 10

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(bot: Client, message):
    chat_id = message.chat.id
    await add_telegraph_chat(chat_id)

@Client.on_message(filters.command(["stats", "status", "gstats"]))
async def stats(bot, message):
    await message.delete()
    alexaai = await message.reply("**ᴡᴀɪᴛ**️")
    await asyncio.sleep(1)
    await alexaai.edit("**ɪ ᴀᴍ ᴄᴏʟʟᴇᴄᴛɪɴɢ sᴛᴀᴛᴜs**")
    await asyncio.sleep(1)
    await alexaai.delete()    
    copypast_lawdey = len(await get_telegraph_users())
    matlabi_jhanto = len(await get_telegraph_chats())
    await message.reply(PandaData.STATS.format(copypast_lawdey, matlabi_jhanto, pyrover))
    