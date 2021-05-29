from telegram import *
from telegram.ext import *
import matplotlib.pyplot as plt
import numpy
def sub(update,context):
    update.message.reply_text('Type something')
    first_name = update.message.from_user
    update.message.reply_text('hello')

bot = Bot("1826479712:AAEJy4VtHb1ZOQEHImoO2xzNRE6dtkwMR00")
#print(bot.get_me())
updater = Updater("1826479712:AAEJy4VtHb1ZOQEHImoO2xzNRE6dtkwMR00",use_context=True)
dispatcher = updater.dispatcher
#print(dispatcher)
def test_function(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text="tutorial link: https://youtu.be/7qJFtGi0hNQ",)
start = CommandHandler('motion_detection',test_function)
dispatcher.add_handler(start)
updater.start_polling()
def test_function1(update:Update,context:CallbackContext):

    bot.send_message(chat_id=update.effective_chat.id,text=f"{sub()}",)
start1 = CommandHandler('start',sub)
dispatcher.add_handler(start1)
updater.start_polling()
def test_function2(update:Update,context:CallbackContext):

    bot.send_message(chat_id=update.effective_chat.id,text=f"{sub()}",)
start2 = CommandHandler('ststt',test_function2)
dispatcher.add_handler(start2)
updater.start_polling()

