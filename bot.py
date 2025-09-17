from pyrogram import Client
from flask import Flask
from info import *
import threading
import time
import asyncio


class Bot(Client):
    def init(self):
        super().init(
            name="Auto Cap",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "body"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.force_channel = FORCE_SUB
        if FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB)
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")
                self.force_channel = None
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        await self.send_message(ADMIN, f"{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")


# Create Flask web app
app = Flask(name)

@app.route('/')
def home():
    return "Auto Caption Bot is running! ✨"

@app.route('/health')
def health():
    return {"status": "ok", "message": "Bot is healthy"}

def run_web():
    """Run the web server in a separate thread"""
    app.run(host='0.0.0.0', port=5000, debug=False)

if name == "main":
    # Start web server in a separate thread
    web_thread = threading.Thread(target=run_web, daemon=True)
    web_thread.start()
    
    # Give web server time to start
    time.sleep(2)
    
    # Run bot in main thread (this allows signal handling to work)
    Bot().run()
