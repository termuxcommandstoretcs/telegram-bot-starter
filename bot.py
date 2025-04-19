from telethon import TelegramClient, events

api_id = 25754901
api_hash = '654ca43112b0299d4ac77179cd4b0ffe'
bot_token = '7842890698:AAEFWG4T24wUDd7XnRqe7UWAMEL6etba0Ng'

# Replace with your actual channel IDs (e.g., -100xxxxxxxxxx)
source_channel = -1002457829171
target_channel = -1002447743194

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await bot.send_message(target_channel, event.message)

print("Bot is running and listening for new messages...")
bot.run_until_disconnected()
