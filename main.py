from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

TOKEN = 'bot token from BotFather in TG'
TARGET_USER_ID = 123456789
STICKER_ID = 'sticker id from other bots in TG'

async def send_sticker(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id

    if user_id == TARGET_USER_ID:
        await update.message.reply_sticker(sticker=STICKER_ID, reply_to_message_id=update.message.message_id)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, send_sticker))
    application.run_polling()


if __name__ == '__main__':
    main()
