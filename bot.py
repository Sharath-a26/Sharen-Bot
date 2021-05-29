from telegram import *
from telegram.ext import *
import matplotlib.pyplot as plt
def start(update,context):

    name = update.message.from_user.first_name                        #gets user's first name
    update.message.reply_text(f"Hi {name}! What can i do for u?")     #Welcomes the user with a text

def about(update,context):
    botinfo = bot.get_me()
    update.message.reply_text(f"{bot.get_me()}")
def talk(update,context):
    text = update.message.text                                        #gets user input
    if text == "hello":
        update.message.reply_text("Can i help u out with something?")
    elif text == "No need":
        update.message.reply_text("Thats ok")
    elif text != "/talk":
        update.message.reply_text(text)
    
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
start1 = CommandHandler('about',about)                #handles commands typed by the user
dispatcher.add_handler(start1)
updater.start_polling()
def test_function2(update:Update,context:CallbackContext):

    bot.send_message(chat_id=update.effective_chat.id,text=f"",)
start2 = MessageHandler(Filters.text,talk)                         #for handling user text
dispatcher.add_handler(start2)
updater.start_polling()

