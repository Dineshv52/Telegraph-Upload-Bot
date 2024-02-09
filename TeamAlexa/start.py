""""
Panda upload bot is a Telegram Audio and video streaming bot
Copyright (c) 2024 -present Team=Security Panda <https://github.com/dineshv52>

This program is free software: you can redistribute it and can modify
as you want
"""

from env import LOG_ID
import asyncio
from pyrogram import Client, filters
from data import PandaData
from TeamAlexa.database.AlexaDB import add_telegraph_user
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    if query.data == "ABOUT_CMD":
        await query.message.edit(
            text=PandaData.ABOUT_STRING,
            reply_markup=InlineKeyboardMarkup(PandaData.HELP_BACK),
        )
    elif query.data == "CMDS_CMD":
        await query.message.edit(
            text=PandaData.CMDS_STRING,
            reply_markup=InlineKeyboardMarkup(PandaData.HELP_BACK),
        )
    elif query.data == "TEAM_CMD":
        await query.message.edit(
            text=PandaData.TEAM_STRING,
            reply_markup=InlineKeyboardMarkup(PandaData.HELP_BACK),
            disable_web_page_preview=True
        )
    elif query.data == "HELP_BACK":
        await query.message.edit(
            text=PandaData.HELP_STRING,
            reply_markup=InlineKeyboardMarkup(PandaData.H_BUTTON),
        )


@Client.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await add_telegraph_user(message.from_user.id)
    alexamusic = await message.reply("🤭🤏✌️")
    await asyncio.sleep(2)
    await alexamusic.edit("**sᴛᴀʀᴛɪɴɢ ʙᴏᴛ**")
    await asyncio.sleep(2)
    await alexamusic.edit("**ɪ ᴀᴍ ᴅᴏɪɴɢ ᴍʏ ʟᴏᴠᴇ 💕**")
    await asyncio.sleep(2)    
    await alexamusic.delete()
    umm = await message.reply_sticker("CAACAgIAAxkBAAEForNjAykaq_efq4Wd-9KZv-nNxJRn3AACIgMAAm2wQgO8x8PfoXC1eCkE")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/763a553cc63fd471085f6.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ Security Panda ᴘʀᴏᴊᴇᴄᴛ ғᴏʀ ᴜᴘʟᴏᴀᴅɪɴɢ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [Security Pana](https://t.me/bugbountyhunt)
┣★ ᴜᴘᴅᴀᴛᴇs : [ʙᴏᴛ updates channel](https://t.me/Panda_bot_update_channel)
┣★ sᴜᴘᴘᴏʀᴛ : [Bot related sᴜᴘᴘᴏʀᴛ](https://t.me/PandaSupportgroup)
┣★ ʀᴜɴ ➛  : /help ᴛᴏ sᴇᴇ ʜᴇʟᴘ ᴍᴇɴᴜ
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/bugbountyhunt) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 ❰ ᴊᴏɪɴ ʜᴇʀᴇ ❱ 🌹", url=f"https://t.me/PandaSupportgroup")
                ]
                
           ]
        ),
    )                       
    sender_id = message.from_user.id
    sender_name = message.from_user.username
    return await client.send_message(LOG_ID, f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** @{sender_name}")

@Client.on_message(filters.command("help") & filters.private)
async def help(client, message):
    lamao = await message.reply_text(
        text=PandaData.HELP_STRING,
        reply_markup=InlineKeyboardMarkup(PandaData.H_BUTTON),
    )