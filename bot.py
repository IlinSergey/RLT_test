import logging

from telegram import Update
from telegram.ext import (ApplicationBuilder, ContextTypes, MessageHandler,
                          filters)

from config import TG_API_KEY
from utils import answer

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot.log',
    level=logging.INFO,
)


async def salary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info('Вызвана команда /salary')
    await update.message.reply_text(
        answer(update.message.text)
        )


def main():
    mybot = ApplicationBuilder().token(TG_API_KEY).build()
    logging.info('Бот стартовал')

    mybot.add_handler(MessageHandler(filters.TEXT, salary))

    mybot.run_polling()


if __name__ == '__main__':
    main()
