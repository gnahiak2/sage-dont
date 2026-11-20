import os
import re

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.context import say
from slack_sdk.errors import SlackApiError

load_dotenv()

slack_app_token = os.getenv("SLACK_APP_TOKEN")
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
slack_signing_secret = os.getenv("SLACK_SINING_SECRET")

app = App(
    token = slack_bot_token,
    signing_secret = slack_signing_secret
)

@app.message(re.compile(r'<!channel>', re.IGNORECASE))
def channel_ping(event, say, logger):
    logger.info(f"ooo theres a event -> {event}")

    say(text='sage dont', thread_ts=event.get(thread_ts))

@app.message(re.compile(r'channel ping', re.IGNORECASE))
def channel_ping1(event, say, logger):
    logger.info(f"ooo theres a event -> {event}")

    say(text='sage dont', thread_ts=event.get(thread_ts))

@app.message(re.compile(r'ping', re.IGNORECASE))
def channel_ping2(event, say, logger):
    logger.info(f"ooo theres a event -> {event}")

    say(text='sage dont', thread_ts=event.get(thread_ts))

@app.message(re.compile(r'channel', re.IGNORECASE))
def channel_ping3(event, say, logger):
    logger.info(f"ooo theres a event -> {event}")

    say(text='sage dont', thread_ts=event.get(thread_ts))
