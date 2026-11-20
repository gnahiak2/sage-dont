import os
import re

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

slack_app_token = os.getenv("SLACK_APP_TOKEN")
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET")

app = App(
    token=slack_bot_token,
    signing_secret=slack_signing_secret,
)

# Bolt runs only the first matching listener, so all triggers live in one pattern.
# "<!channel>" (an @channel mention) also contains "channel".
TRIGGER = re.compile(r"channel|ping", re.IGNORECASE)


@app.message(TRIGGER)
def channel_ping(event, say, logger):
    logger.info(f"ooo theres a event -> {event}")

    say(text="sage dont")


if __name__ == "__main__":
    SocketModeHandler(app, slack_app_token).start()
