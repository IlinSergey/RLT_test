import logging

from config import TG_API_KEY
from main import answer

from telegram.ext import (ApplicationBuilder, MessageHandler,
                          filters, ContextTypes)

from telegram import Update


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot.log',
    level=logging.INFO,
)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info('Вызвана команда /echo')
    await update.message.reply_text(
        answer(update.message.text)
        )


def main():
    mybot = ApplicationBuilder().token(TG_API_KEY).build()
    logging.info('Бот стартовал')

    mybot.add_handler(MessageHandler(filters.TEXT, echo))

    mybot.run_polling()


if __name__ == '__main__':
    main()
