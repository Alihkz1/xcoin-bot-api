from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import httpx

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id

    url = f"https://xcoin.liara.run?userId={user_id}"
    button = InlineKeyboardButton(text="Click to View Your Data", url=url)
    keyboard = [[button]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=chat_id, text="Click the button below to view your data:", reply_markup=reply_markup)

async def main():
    TOKEN = "7253380306:AAGTAZGbHLduXfN-Wvjq7mQVAqFRgCUk6kk"
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    async with httpx.AsyncClient(timeout=30) as client:
        application.request = lambda *args, **kwargs: client.request(*args, **kwargs)
        await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
