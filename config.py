#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5837810810:AAFuHLLOceME162lDi4OKB5XgGiCUipsdr4")
    API_ID = int(os.environ.get("API_ID", "26435700"))
    API_HASH = os.environ.get("API_HASH", "527cf5174e120a9093611bc69d7b7709")
    AUTH_USERS = "5908818236"

