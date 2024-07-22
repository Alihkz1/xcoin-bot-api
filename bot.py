from telegram.ext import Updater, CommandHandler
import os

def start(update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    
    # Construct the URL with the user ID
    url = f"https://xcoin.liara.run?userId={user_id}"
    
    # Send the URL to the user
    context.bot.send_message(chat_id=chat_id, text=f"Click here to view your data: {url}")

def main():
    TOKEN = os.getenv("7253380306:AAGTAZGbHLduXfN-Wvjq7mQVAqFRgCUk6kk")
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
