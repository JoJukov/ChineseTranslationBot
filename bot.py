import logging

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from correct_google_translation import get_translated_text
from your_token import your_personal_token

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_translated_text("чинг чонг"))


def echo(update, context):
    if update.message['chat']['type'] == 'private':
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_translated_text(update.message.text))
        return
    if update.message['reply_to_message'] is not None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_translated_text(update.message
                                                                                            ['reply_to_message'][
                                                                                                'text']))
        return
    for i in update.message.entities:
        if i['type'] == 'mention' and (
                update.message.text[i['offset']: i['offset'] + i['length']]) == '@correct_chinese_bot':
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=get_translated_text(update.message.text[len('@correct_chinese_bot')::]))


def unknown_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="You posted cringe")


bot = telegram.Bot(token=your_personal_token)
updater = Updater(token=your_personal_token, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

unknown_handler = MessageHandler(Filters.command, unknown_command)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
