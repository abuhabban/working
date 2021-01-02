from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import pickle
import logging
from telegram import (InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
import random
import smtplib


TOKEN = "1378171996:AAEaihHekAb-We57_jIrHB0SnE1Nm-BDTiA"

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

data = {'OTP'}
dataa = {'email'}

OTP = 1
EMAIL = 1

def call_mat(yy):
    global OTO
    OTO = random.randrange(100000, 1000000);
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    pass0 = "xzbqrizcksjbsdrd"
    server.login("telegrambotapi213@gmail.com",pass0)
    msgg = "Your OTP Sent From Email Varification Bot Is "+ str(OTO)
    server.sendmail("telegrambotapi213@gmail.com",yy,msgg)
    server.quit()

def start(update,context):
    mssg = "🦋Welcome To Email Verification Bot"
    stff =[["Verify Email 📩"]]
    afd = ReplyKeyboardMarkup(stff,one_time_keyboard=False,resize_keyboard=True)
    update.message.reply_text(text=mssg,reply_markup=afd)
    
def emailadr(update,context):
    global dataa
    dataa = {'email':"none"}
    mssg = ("⚡️Please Enter Your Email Address Here⚡️")
    update.message.reply_text(mssg)
    return EMAIL
        
def get_email(update,context):
        global data
        data = {'OTP':"none"}
        file_user = update.message.from_user.id
        if "@gmail.com" in update.message.text:
            b = update.message.text
            if b != "none":
                update.message.reply_text("Email Accepted Please Wait")
                call_mat(yy=b)
                update.message.reply_text("Please Enter The Otp Sent To Your Email❗️")

                return OTP
        else:
            update.message.reply_text("Please Enter Correct Email⚠️")  
        

def get_title(update, context):
        b = update.message.text
        if OTO == int(b):
            update.message.reply_text("✨Congratulations Your email is verified✨")
        else:
            update.message.reply_text(f"Wrong Otp Please Enter OTP Again⚠️")

def cancel(update, context):
    update.message.reply_text('canceled')
    return ConversationHandler.END

# --- create conversation ---
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.regex('^Verify Email 📩$'),emailadr))
my_conversation_handler = ConversationHandler(
   entry_points=[MessageHandler(Filters.text,get_email)],
states={
       OTP: [MessageHandler(Filters.text, get_title)
       ]
   },
fallbacks=[ CommandHandler("cancel",cancel) ])
dispatcher.add_handler(my_conversation_handler)

dispatcher.add_handler(MessageHandler(Filters.text,get_title))

# --- run bot ---

updater.start_polling()
print('Running... [Press Ctrl+C to stop]')
updater.idle()
print('Stoping...')
updater.stop()