#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anurag Maheshwari | Modifieded By : @AnuragB8_Bot

import os
from config import Config
from pyrogram import Client as Clinton

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Clinton("@Uploader_Extra_bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Warrior.run()
