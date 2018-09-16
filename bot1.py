from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings



# error_logger= logging.getLogger()
# error_logger.setLevel(logging.INFO)
# handler = logging.FileHandler('bot1_stat.log', 'w', 'utf-8')
# handler.setFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# error_logger.addHandler(handler)


formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


def setup_logger(name, log_file, level):

    handler = logging.FileHandler(log_file, 'w', 'utf-8')        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def greet_user(bot, update):
    greet_text = "Вызван /start"
    logging.error(greet_text)
    update.message.reply_text(greet_text)


def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал {}".format(update.message.chat.username, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    my_bot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info("Бот запускается")

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    my_bot.start_polling()
    my_bot.idle()


info_logger = setup_logger("info_logger","bot1_info.log", logging.INFO)
err_logger = setup_logger("err_logger","bot1_err.log", logging.ERROR)

main()