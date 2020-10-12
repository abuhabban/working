# Importing modules. 
from telegram import Bot
from telegram.ext import Updater, CommandHandler, ConversationHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext import CallbackQueryHandler
from telegram.parsemode import ParseMode
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.callbackquery import CallbackQuery
from telegram.utils import helpers
import logging
import time
import pickle
import datetime
from datetime import timedelta
from datetime import date
import os
PORT = int(os.environ.get('PORT', 5000))

# Logging Setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',                                                  level=logging.INFO)
logger = logging.getLogger(__name__)

# Put Your Token Here.
TOKEN = "1378171996:AAEaihHekAb-We57_jIrHB0SnE1Nm-BDTiA"


####################################

# Start Function setup 
def start(update: Update, context:CallbackContext):
    payload = context.args
    if len(payload) > 0:
        file_user = update.message.from_user.id
        try:
            pickle.load( open(f"{file_user}pay.py", "rb" ) )
        except (OSError, IOError) as e:
            _data = " "
            fti = _data.join(payload)
            nt = (f"{fti}")
            pickle.dump( nt, open(f"{file_user}pay.py", "wb" ) )
            
            pickle.dump( 0, open("Global.py", "wb" ) )
            cxo = pickle.load( open("Global.py", "rb" ) )
            a = 1
            cxo = int(cxo) + int(a)
            pickle.dump( cxo, open("Global.py", "wb" ) )
            
    else:
        file_user = update.message.from_user.id
        try:
            pickle.load( open(f"{file_user}pay.py","rb" ) )
        except (OSError, IOError) as e:
            ct = "you are user"
            pickle.dump( ct, open(f"{file_user}pay.py", "wb" ) )
             
            pickle.dump( 0, open("Global.py", "wb" ) )
            cxo = pickle.load( open("Global.py", "rb" ) )
            a = 1
            cxo = int(cxo) + int(a)
            pickle.dump( cxo, open("Global.py", "wb" ) )
 
    first_msg = "💡To use this bot you must join this channel: @Trontreelaunching"

    kdb_layout = [["✅ joined"]]
    
    kbd = ReplyKeyboardMarkup(kdb_layout,one_time_keyboard=False,resize_keyboard=True)
    
    update.message.reply_text(text=first_msg, reply_markup=kbd)
 
    file_name = update.message.from_user.first_name
    file_user = update.message.from_user.id
    try:
        ae =  pickle.load( open(f"{file_user}b.py", "rb" ) )
        if ae >= 0.00000000:
            pass
    except (OSError, IOError) as e:
        st = 0.00000000
        pickle.dump( st, open(f"{file_user}b.py", "wb" ) )
                                     
    try:
        avt =  pickle.load( open(f"{file_name},{file_user}w.py", "rb" ) )
    except (OSError, IOError) as e:
        st = "not set"
        pickle.dump( st, open(f"{file_name},{file_user}w.py", "wb" ) )
       
    try:
        ytu =  pickle.load( open(f"{file_name},{file_user}bon.py", "rb" ) )
    except (OSError, IOError) as e:
        yt = update.effective_message.date
        tgy = datetime.timedelta(hours=25)
        ytv = yt - tgy
        pickle.dump( ytv, open(f"{file_name},{file_user}bon.py", "wb" ) )
       
    try:
        yte =  pickle.load( open(f"{file_name},{file_user}bonti.py", "rb" ) )
    except (OSError, IOError) as e:
        skt = update.effective_message.date
        thu = datetime.timedelta(hours=25)
        syt = skt - thu
       
        pickle.dump( syt, open(f"{file_name},{file_user}bonti.py", "wb" ) )       

    try:
        dvt =  pickle.load( open(f"{file_user}tol.py", "rb" ) )
    except (OSError, IOError) as e:
        ss = 0
        pickle.dump( ss, open(f"{file_user}tol.py", "wb" ) )
              

# Checking the user is joined the Channel or Not.  
def user_in_chat(chat_id, user_id,context):
    try:
        user_not_in_chat = context.bot.get_chat_member(chat_id, user_id).status == "left"
        if user_not_in_chat:
            return False
    except:
            return False
    return True
    
# All Action Here.    
def joined(update,context):
    mychatid = "@Trontreelaunching"
    userid = update.message.from_user.id
    in_chat = user_in_chat(chat_id=mychatid, user_id=userid, context=context)
    #Home layout 
    first_msg1 = (f"🍫<b>Hello</b> {update.message.from_user.mention_html()} <b>Welcome to the python py3 bot.</b>")
    
    ydb_layout = [["💰 Balance"],["👬Referral","🎁 Bonus","Withdraw 💳"],     ["📊 Statistic","♻️ Extra"]]
    
    #balance variable
    file_name = update.message.from_user.first_name
    dif_bal = update.message.from_user.id
    i = pickle.load( open(f"{dif_bal}b.py", "rb" ) )
    d = "{:.8f}".format(i)
    
    #Account Info Layout
    global first_msg3
    first_msg3 = (f"💰 <b>Your Account Balance:</b>     {d}<b> Litecoin.</b>")
           
    acc_layout = [["💼 Wallets","☎️ Help"],["⬅️ Returns"]]
    global acc
    acc = ReplyKeyboardMarkup(acc_layout,one_time_keyboard=False,resize_keyboard=True)
    
    print(f"{in_chat}")

    # [Action] If the user in chat 
    if in_chat:
       # if the user press  the joined Button.    
       if (update.message.text == "✅ joined"):
           file_user = update.message.from_user.id
           cvi = pickle.load( open(f"{file_user}pay.py", "rb" ) )
           if cvi == "you are user":
               pass
           else:
               if cvi != "you are user":
                   cve = pickle.load( open(f"{file_user}pay.py", "rb" ) )
                   btl = pickle.load( open(f"{cve}b.py","rb") )
                   rtl = 0.00000450
                   btl = float(btl) + float(rtl)
                   pickle.dump( btl, open(f"{cve}b.py", "wb" ) )
                   file_user = update.message.from_user.id
                   ct = "you are user"
                   pickle.dump( ct, open(f"{file_user}pay.py", "wb" ) )
                   dc = pickle.load( open(f"{cve}tol.py", "rb" ) )
                   dcl = 1
                   dc = int(dc) + int(dcl)
                   pickle.dump( dc, open(f"{cve}tol.py", "wb" ) )
                   ttext = ("🦋 <i>New Referral on your link you received</i> <b>0.00000450 LTC</b>")
                   context.bot.send_message(chat_id=cve,text=ttext,parse_mode=ParseMode.HTML)
                   
           
           ydb = ReplyKeyboardMarkup(ydb_layout,one_time_keyboard=False,resize_keyboard=True)
           
           update.message.reply_text(text=first_msg1,parse_mode=ParseMode.HTML,reply_markup=ydb)
    else:
            # [Action] for the user not in chat.
            if (update.message.text == "✅ joined"):
                update.message.reply_text("💡 To use this bot you must join this channel: @Trontreelaunching")
    
    # Action for the user. If the user press the Account Info Button.
    if (update.message.text == "💰 Balance"):
            
            update.message.reply_text(text=first_msg3,parse_mode=ParseMode.HTML,reply_markup=acc)
       
        
    if (update.message.text == "⬅️ Return"):
        update.message.reply_text(text=first_msg3,parse_mode=ParseMode.HTML,reply_markup=acc)
        
    # Reply For Return Button    
    if (update.message.text == "⬅️ Returns"):
        
        ydb = ReplyKeyboardMarkup(ydb_layout,one_time_keyboard=False,resize_keyboard=True)
           
        update.message.reply_text(text="🔭 <b>Main Menu</b>",parse_mode=ParseMode.HTML,reply_markup=ydb)
        
    if (update.message.text == "👬Referral"):
        
        bot = context.bot
        url = helpers.create_deep_linked_url(bot.get_me().username,str(update.message.chat.id))
        file_user = update.message.from_user.id
        bfgj = pickle.load( open(f"{file_user}tol.py", "rb" ) )
        text = (f"👥 <b>Refferrals System</b>\n\n<b>1 Level:</b>\n🥇 <b>1° Level:</b> 0.00000100")
        text1 = (f"👨‍👨‍👦‍👦 <b>Invite direct bot url:</b> {url}")
        text2 = (f"📑 <b>Referrals Statistics</b>\n<i>Track your referrals count and earnings</i>\n\n<b>1° Level:</b> {bfgj} users\n\n")
        detail_rep = [[InlineKeyboardButton("📑 Detailed Report 📑",callback_data="2")]]
        deil_rep = InlineKeyboardMarkup(detail_rep)
          
        update.message.reply_text(text=text,parse_mode=ParseMode.HTML)
        update.message.reply_text(text=text1,parse_mode=ParseMode.HTML)
        update.message.reply_text(text=text2,parse_mode=ParseMode.HTML,reply_markup=deil_rep)

    if (update.message.text == "📊 Statistic"):
        now = datetime.datetime.now(datetime.timezone.utc)
        ytt = now.strftime("%d/%m/%Y %H:%M")
        cxo = pickle.load( open("Global.py", "rb" ) )
        statext = (f"📉 <b>Bot Statistic</b>\n\n<b>📔 Total Users:</b> {cxo}\n\n<b>➖ Total Withdrawls:</b> 0.00000000\n\n<b>🕧 Server time:</b> <code>{ytt}</code>")
        update.message.reply_text(text=statext,parse_mode=ParseMode.HTML)
             
                        
#---------------- Take input and save input ---------------#
        
#---structure for data
data = {'title'}
TITLE = 1
def save_wallet(update, context):
    global data # to assign new dictionary to external/global variable

    # create new empty dictionary
    data = {'title':""}
    wallet_inl = [[InlineKeyboardButton("💼Set / Change Wallet",callback_data="1")]]
    wallet_markup = InlineKeyboardMarkup(wallet_inl)
    file_name = update.message.from_user.first_name
    file_user = update.message.from_user.id
    global vv
    vv = pickle.load( open(f"{file_name},{file_user}w.py", "rb" ) )
    msg_wwal = (f"💡 <b>Your currently set TRX wallet is:  \n</b><code>{vv}</code>\n\n💹 It will be used for <b>all future withdrawals.</b>")
    msg_wwal1 = (f"💡 <b>Your currently set TRX wallet is:  \n</b>{vv}\n\n💹 It will be used for <b>all future withdrawals.</b>")
    if vv != "not set":
        global del1
        del1 = update.message.reply_text(text=msg_wwal1,parse_mode=ParseMode.HTML,reply_markup=wallet_markup)
    else:
        global del2
        del2 = update.message.reply_text(text=msg_wwal,parse_mode=ParseMode.HTML,reply_markup=wallet_markup)
# Next state in conversation
def button_wall(update,context):
    query = update.callback_query
    if query.data == "1":
        if vv != "not set":
            del1.delete()
        else:
            del2.delete()
        itext=("✏️ Send now your TRX Address to use it in future withdrawals!")
        addd_res = [["⬅️ Return"]]
        ad_rs = ReplyKeyboardMarkup(addd_res,one_time_keyboard=False,resize_keyboard=True)
        update.effective_chat.send_message(text=itext, reply_markup=ad_rs)
        return TITLE
    
def get_title(update, context):
    if update.message.text != "⬅️ Return":
        file_name = update.message.from_user.first_name
        file_user = update.message.from_user.id
        data['title'] = update.message.text
        bgh = data['title']

        pickle.dump( bgh, open(f"{file_name},{file_user}w.py", "wb" ) )
        with open(f"{file_name},{file_user}w.py", "rb") as f :
            ais = pickle.load(f)
            mvg = (f"🦋 Done: Your wallet is <b>{ais}</b>")
            update.message.reply_text(text=mvg,parse_mode=ParseMode.HTML)     
    else:
        update.message.reply_text(text=first_msg3,parse_mode=ParseMode.HTML,reply_markup=acc)       
        return ConversationHandler.END 
 
def cancel(update, context):
    update.message.reply_text('canceled')
    # end of conversation
    return ConversationHandler.END 
    
#---------------------  Support Button  --------------------------
#-----structure for data
data1 = {'typing'}
TYPING = 1
def supp(update,context):
        global data1 # to assign new dictionary to external/global variable
    # create new empty dictionary
        data1 = {'typing':""}
        help_msg = (f"<b>📞 You are now in direct contact with our Administrator</b>\nSend here any message you want to submit, you will receive the answer directly here in chat!")
        
        help_layout = [["⬅️ Return"]]
        
        help = ReplyKeyboardMarkup(help_layout,one_time_keyboard=False,resize_keyboard=True)
        
        update.message.reply_text(text=help_msg, parse_mode=ParseMode.HTML,reply_markup=help)
        return TYPING
        
def typ(update,context):
    data1['typing'] = update.message.text
    bgh = data1['typing']
    txct = (f"<b>Message sent to the administrator:</b>\n{bgh}")
    na_me = update.message.from_user.mention_html()
    us_er = update.message.from_user.name
    usr_id =update.message.from_user.id
    suyp = (f"✉️<b>Message sent from the user:</b>\n🖌<b>Name:-</b> {na_me}\n<b>Username:-</b> {us_er}\n<b>User-ID:-</b> {usr_id}\n\n<b>-------Message Of The User-------</b>\n{bgh}")
    if bgh != "⬅️ Return":
        context.bot.send_message(chat_id=1033291787,text=suyp,parse_mode=ParseMode.HTML)
        update.message.reply_text(text=txct,parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(text=first_msg3,parse_mode=ParseMode.HTML,reply_markup=acc)
        return ConversationHandler.END
    
#-------------------   BONUS_BUTTON   ----------------------#
#------Structure for data  
def bonadd(update, context):
    file_name = update.message.from_user.first_name
    file_user = update.message.from_user.id
    c = 0.00000100
    j = pickle.load( open(f"{file_user}b.py", "rb" ) )
    bl = "{:.8f}".format(j)
    
    now = datetime.datetime.now(datetime.timezone.utc)
    tem = datetime.timedelta(hours=23,minutes=50,seconds=36)
    #defined variables and data ---|---
    with open(f"{file_name},{file_user}bonti.py", "rb") as f:
        hdk = pickle.load(f)
    if hdk+tem < now:
        bl = float(bl) + float(c)
        pickle.dump( bl, open(f"{file_user}b.py", "wb"))

        bonus_msg = (f"<b>✨ Congratulations!</b> \n\n✅ You received 0.00000100 LTC. Come Back in 24 hours !")
        update.message.reply_text(text=bonus_msg, parse_mode=ParseMode.HTML)
        bonti = update.effective_message.date
        pickle.dump(bonti, open(f"{file_name},{file_user}bonti.py", "wb" ) )
 
                
  
def record(update, context):
    file_name = update.message.from_user.first_name
    file_user = update.message.from_user.id
    date = update.effective_message.date
    pickle.dump( date, open(f"{file_name},{file_user}bon.py", "wb" ) )

def bonus(update, context):
    file_name = update.message.from_user.first_name
    file_user = update.message.from_user.id
    tim = datetime.timedelta(hours=23,minutes=50, seconds=36)
    chk = datetime.timedelta(minutes=8,seconds=60)
    with open(f"{file_name},{file_user}bon.py", "rb") as f:
        hok = pickle.load(f)
    now = datetime.datetime.now(datetime.timezone.utc)
    if hok+tim > now:
        cal = hok+tim
        gtiu = cal-now+chk
        ix = str(gtiu).split(".")[0]
        
        wait_msg = (f"❌ <b>Sorry ,you have received your Bonus today.</b>\n\n⚡ <code>You can receive your next bonus :</code>\n⏱ {ix} Left")
        update.message.reply_text(text=wait_msg,parse_mode=ParseMode.HTML)
    else:
        if hok+tim < now:
            time.sleep(1)
            bonadd(update=update,context=context)
            record(update=update,context=context)

#-----------------------Withdraw Button------------------------#









        
def main():
       updater = Updater(TOKEN, use_context=True)
       #get the dispatcher to register handler
       dispatcher = updater.dispatcher
       dispatcher.add_handler(CommandHandler("start", start))
       dispatcher.add_handler(MessageHandler(Filters.regex('^💼 Wallets$'),save_wallet))
       dispatcher.add_handler(MessageHandler(Filters.regex('^🎁 Bonus$'),bonus))
             
       my_conversation_handler = ConversationHandler(entry_points=[CallbackQueryHandler(button_wall, pattern='^' + str(TITLE) + '$')],states={TITLE: [MessageHandler(Filters.text & ~Filters.command, get_title)]},fallbacks=[CommandHandler("caaancel",cancel)])
       #------Second Conversation
       my_conversation_handlor = ConversationHandler(entry_points=[MessageHandler(Filters.regex('^☎️ Help$'),supp)],states={TYPING: [MessageHandler(Filters.text,typ)]},fallbacks=[CommandHandler("caaancel",cancel)])
       
       
       dispatcher.add_handler(my_conversation_handler)
       dispatcher.add_handler(my_conversation_handlor)
       dispatcher.add_handler(MessageHandler(Filters.text,joined))
       
       updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
       updater.bot.setWebhook('https://working-bot-python.herokuapp.com/' + TOKEN)
       
       print('Running... [Press Ctrl+C to stop]')
       updater.idle()
       update.stop()

if __name__ ==  '__main__':
    main()
    
