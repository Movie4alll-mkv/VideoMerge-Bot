# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID","6534707")
    API_HASH = os.environ.get("API_HASH","4bcc61d959a9f403b2f20149cbbe627a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5442493323:AAGE585VqW2Rjn8p7fTamBdyiSsg9dktdgE")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","animedualaudiozippercartoonist")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL","-1001843564893")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI","mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1430593323"))

    START_TEXT = """
Hi Unkil, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.


"""
    CAPTION = "@animedualaudiozippercartoonist"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
