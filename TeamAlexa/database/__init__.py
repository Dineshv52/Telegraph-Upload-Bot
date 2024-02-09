# Copyright ©️ 2024 Security Panda. All Rights Reserved Modified, Enhanced And Database Added By ©️ Team Security Panda
""""
Panda telegraph upload bot is a Telegram Audio and video streaming bot
Copyright (c) 2024 -present Team=Security Panda <https://github.com/dineshv52>

This program is free software: you can redistribute it and can modify
as you want.
"""

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from env import MONGO_DB_URI


MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb
