import telebot
import requests

BOT_TOKEN = "8211745235:AAGO_Yc5spImOZrk9-uuZ5PGIGBf5p-G7m8"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

    r = requests.get("https://catbox.moe/user/api.php", params={
        "reqtype": "urlupload",
        "url": file_url
    })

    bot.reply_to(message, f"✅ Uploaded!\n🔗 Link:\n{r.text}")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 ছবি পাঠাও, আমি Catbox link দেবো")

print("Bot is running...")
bot.infinity_polling()