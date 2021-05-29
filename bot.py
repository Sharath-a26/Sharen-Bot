from telegram import *
from telegram.ext import *
import matplotlib.pyplot as plt
def start(update,context):

    name = update.message.from_user.first_name
    update.message.reply_text(f"Hi {name}!")
def about(update,context):
    botinfo = bot.get_me()
    update.message.reply_text(f"{bot.get_me()}")
bot = Bot("1826479712:AAEJy4VtHb1ZOQEHImoO2xzNRE6dtkwMR00")
#print(bot.get_me())
updater = Updater("1826479712:AAEJy4VtHb1ZOQEHImoO2xzNRE6dtkwMR00",use_context=True)
dispatcher = updater.dispatcher

def welcome(update:Update,context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,text=f"{sub()}",)
start = CommandHandler('start',start)

dispatcher.add_handler(start)

updater.start_polling()
def test_function1(update:Update,context:CallbackContext):

    bot.send_message(chat_id=update.effective_chat.id,text=f"",)
start1 = CommandHandler('about',about)
dispatcher.add_handler(start1)
updater.start_polling()
def test_function2(update:Update,context:CallbackContext):

    bot.send_message(chat_id=update.effective_chat.id,text=f"",)
start2 = CommandHandler('ststt',test_function2)
dispatcher.add_handler(start2)
updater.start_polling()

