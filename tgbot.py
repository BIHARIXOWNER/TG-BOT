
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '7323010488:AAEE1ALJG-NGjl97qqyNEhCb5qLj8vsvKDM'

def start(update, context):
    context.bot.send_message(chat_id=(link unavailable), text="Hello! Send 'code' to get your chat ID.")

def get_code(update, context):
    chat_id = (link unavailable)
    context.bot.send_message(chat_id=chat_id, text=f"Your chat ID is: {chat_id}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & Filters.regex('code'), get_code))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
 assistance!
