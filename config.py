#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6103524529:AAFBCWjbgvZAzPesjPM-dAFvu79NXpGEQyg")
    API_ID = int(os.environ.get("API_ID", "24250238"))
    API_HASH = os.environ.get("API_HASH", "cb3f118ce5553dc140127647edcf3720")
    AUTH_USERS = "6175650047"

