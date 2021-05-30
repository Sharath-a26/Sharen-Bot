from telegram import *
from telegram.ext import *
import datetime
import re
import pywhatkit as kit
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
    elif text[0] != "/" and text[0]:
        update.message.reply_text(text)
def send(update,context):
    text = update.message.text
    if text == "whatsapp":
        update.message.reply_text(
            f"Hey {update.message.from_user.first_name} welcome to the feature of automating whatsapp.")
        update.message.reply_text(
            "Please enter the whatsapp number you want to send message, the message that you wanna send,"
            " the time at which your message has to be sent in 24 hour format")
        text2 = update.message.text
        a = text2.split()
        update.message.reply_text(a)
def schedule(update,context):
    def change_date_format(b):                                 
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', b)
    b = datetime.date.today()
    b = str(b)
    a = change_date_format(b)
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.datetime.strptime(a, '%d-%m-%Y').weekday()
    if day_name[day] == "Sunday":
        update.message.reply_text(f"Its {day_name[day]} so just netflix and chill!")  #schedule for sunday.
    elif day_name == "Monday":
        update.message.reply_text(f"Its {}")



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
start1 = CommandHandler('about',about)                #handles commands typed by the user --> here it displays bot info.
dispatcher.add_handler(start1)
updater.start_polling()

day_schedule = CommandHandler('schedule',schedule)           #command to print the schedule for the day
dispatcher.add_handler(day_schedule)
updater.start_polling()
def test_function2(update:Update,context:CallbackContext):

    bot.send_message(chat_id=update.effective_chat.id,text=f"",)
start2 = MessageHandler(Filters.text,talk)                         #for handling user text
dispatcher.add_handler(start2)
updater.start_polling()

