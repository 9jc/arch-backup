from ast import parse
from cgitb import html
from email import message
from pydoc import classname
from re import L
from _secrets import API_KEY_TELEGRAM
from telebot import *
from telebot import custom_filters
import os
import time
import subprocess
import requests
import json
import datetime

from _wallpaper import wallpaper_fun
import random
from _keyboardButton import *

# Date Time in human readble - d/m/y format
e = datetime.now()
date1 = ("%s/%s/%s" % (e.day, e.month, e.year))
time1 = ("%s:%s:%s" % (e.hour, e.minute, e.second))

# Bot APi Key - dont forget its to set it .env var
bot = telebot.TeleBot(API_KEY_TELEGRAM) 


# SimpleCustomFilter is for boolean values, such as is_admin=True
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        bot.get_chat_member(message.chat.id,message.from_user.id)
        sender_id = message.chat.id
        if sender_id == 1339103454:
            return True
        else:
            return False
# User Dict Class -- move this shit somewhre else ?
user_dict = {}

#----------------
@bot.message_handler(content_types=["text"])
def content_0(message):
    xm1 = message
    button_k_msg(message=xm1)

#getting quote thinge
response = requests.get("https://zenquotes.io/api/random")
json_data = json.loads(response.text)
quote = json_data[0]['q']
auth = json_data[0]['a']

# class user - starting shit
class User:
    def __init__(self, name):
        self.name = name
        self.ipadress  = None
        self.cmdline = None

#stating message -----------------------------------------------[ 1 ]
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    msg_id1 = message.message_id
    msg_id = int(msg_id1) + 1
    bot.send_message(message.chat.id, """
--------------------------------------------------
🤝<b>Thank you, for checking out this bot... </b>
--------------------------------------------------
""", parse_mode="html")
    time.sleep(1.5)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text="""
--------------------------------------------------
🤝 <b>Thank you, for checking out this bot...
🗒️ <u>Note</u>:This Bot is still in the early stages of development </b>
--------------------------------------------------
""", parse_mode="html")
    time.sleep(1.5)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text="""
--------------------------------------------------
🤝 <b>Thank you, for checking out this bot...
🗒️ <u>Note</u>:This Bot is still in the early stages of development, 
🏗️ If you encounter any bugs feel free to contact - @Nitroplexx </b>
--------------------------------------------------
""", parse_mode="html")
    time.sleep(2)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text=f"""
--------------------------------------------------
🤝 <b>Thank you, for checking out this bot...
🗒️ <u>Note</u>:This Bot is still in the early stages of development, </b> 
🏗️ <i>If you encounter any bugs feel free to contact</i> - @Nitroplexx
--------------------------------------------------
<b>✅ - To get list of Avaliable Commands type - /help </b>
--------------------------------------------------
""", parse_mode="html")


    
#stating message -----------------------------------------------[ 1 ]
@bot.message_handler(commands=['start', 'help'])
def start(message):
    print(message.text)
#    startmsg = f"Hello <b> {message.from_user.first_name}</b> ! How are you doing? ✌️"
    startmsg = (f"""
✅ <b>This are the availible commands</b>

<b>Normal Commands</b>
 /start /help  -> <i>Gets Avalible Command</i>

<b>Server Commands</b>
 /server_side  -> <i>Lets you control the server</i>

<b>Cool Commands</b>
 /ip  /dox     -> <i>IP lookup Tool</i>
 id            -> <i>Gets your account info</i>

<b>Extra Commands</b>
 /quote        -> <i>Random Quote</i>
 /contact      -> <i>Owners Contact</i>

🗒️<b>Note:</b><u>This is a personal bot and
is not accessible to the public.</u>
<b>✌️Thank you nd Get lost ^_^</b>
    """)
    bot.send_message(message.chat.id, startmsg , parse_mode='html')


#contact message------------------------------------------------[ 2 ]
@bot.message_handler(commands=['contact'])
def contact_owner(message):
    bot.send_message(message.chat.id,f"<b>Message @Nitroplexx - Dont Spam!!</b>", parse_mode='html')

#quote message------------------------------------------------[ 2.1 ]
def emoji_randomizer(e):
    if e == 1:
        emoji_list = ["🐉","🦈","🐬","🐋","🐠","🐡","🦑","🐙","🦞","🦀","🦅","🕊️","🦢","🦜","🦩","🦚","🦉","🦤","🐦"]
        emoji_random = random.choice(emoji_list)
        return emoji_random
    else:
        print("🕊️")

@bot.message_handler(commands=['quote'])
def quote_api(message):
    user_id = message.chat.id
    msg_id1 = message.message_id
    msg_id = int(msg_id1) + 1
    bot.send_message(message.chat.id,f'<b>{emoji_randomizer(e=1)} "{quote}" \n\n ✏️ - {auth}</b>', parse_mode='html')
    time.sleep(2)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text=f'<b>{emoji_randomizer(e=1)} "{quote}" \n\n ✏️ - {auth}</b>', parse_mode='html')
    time.sleep(2)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text=f'<b>{emoji_randomizer(e=1)} "{quote}" \n\n ✏️ - {auth}</b>', parse_mode='html')
    time.sleep(2)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text=f'<b>{emoji_randomizer(e=1)} "{quote}" \n\n ✏️ - {auth}</b>', parse_mode='html')
    time.sleep(2)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text=f'<b>{emoji_randomizer(e=1)} "{quote}" \n\n ✏️ - {auth}</b>', parse_mode='html')


# Handle '/excute_cmd line' and '/excute_cmd' - server intraction tool---------------------------------------------------[ 3 ]
@bot.message_handler(is_admin=True, commands=['excute_cmd'])
#@bot.message_handler(func=lambda message: message.from_user.username == "Nitroplexx")
def server_cmd(message):
    msg1 = bot.reply_to(message, "<b>🐧Enter a linux server command to continue:</b>", parse_mode='html')
    bot.register_next_step_handler(msg1, process_name_step_1)

def process_name_step_1(message):      
    chat_id = message.chat.id
    cmd = message.text
    user = User(cmd)
    user_dict[chat_id] = user
    command_server = subprocess.getoutput(cmd)
    file = open("command_output.txt", ("a"))
    file.write(command_server)
    bot.send_message(message.chat.id,f"{command_server}")
        # except:
        #     bot.send_message(message.chat.id,f"<b>⚠️Error, command not found </b>")

@bot.message_handler(is_admin=False, commands=['excute_cmd']) # If user is not admin
def not_admin(message): 
    user_id = message.chat.id
    msg_id1 = message.message_id
    msg_id = int(msg_id1) + 1
    bot.send_message(message.chat.id, "🟢 <b>Checking if user is authorized in database. </b>", parse_mode="html")
    time.sleep(1)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text="🟡 <b>Checking if user is authorized in database.. </b>", parse_mode="html")
    time.sleep(1)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text="🟠 <b>Checking if user is authorized in database... </b>", parse_mode="html")
    time.sleep(1)
    bot.edit_message_text(message_id=msg_id, chat_id=user_id, text="❌ <b>Your not authorized for query on admin.commands </b>", parse_mode="html")


# Deleting past 300 messages
@bot.message_handler(commands=['clear'])
def clearing(message):
    user_id = message.chat.id
    msg_id1 = message.message_id
    msg_num_del = msg_id1 - 500
    for m in range(msg_id1, msg_num_del, -1):
        bot.delete_message(message_id=m, chat_id=user_id)

#------------------------------------------------------------------------[ 3 ] server handler
# debugin stuff msg
@bot.message_handler(commands=['debug_msg'])
def ip_tool(message):
    bot.send_message(message.chat.id, message)

# Handle '/ip' and '/dox' - iptool-------------------------------[ 4 ]
@bot.message_handler(commands=['ip', 'dox'])
def ip_tool(message):
    msg = bot.reply_to(message, "<b>📡Please enter your target IP:</b>", parse_mode='html')
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
        try:
            chat_id = message.chat.id
            ipadress = message.text
            user = User(ipadress)
            user_dict[chat_id] = user
            response = requests.get(url=f'http://ip-api.com/json/{ipadress}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,hosting,query').json()
                    # print(response)
                    #         
            data = {
                '[🌐IP]': response.get('query'),
                '[📠Int prov]': response.get('isp'),
                '[📧Org]': response.get('org'),
                '[🏳️Country]': response.get('country'),
                '[🎌Region Name]': response.get('regionName'),
                '[🏙️City]': response.get('city'),
                '[⌚Time Zone]': response.get('timezone'),
                '[🗃️ZIP]': response.get('zip'),
                '[📍Latitude]': response.get('lat'),
                '[📍Longitude]': response.get('lon'),
                '[💲Currency]': response.get('currency'),
                '[📡AS-Name]': response.get('as'),
                '[📱Mobile]': response.get('mobile'),
                '[🛸Proxy]': response.get('proxy'),
                '[🏬Hosting]': response.get('hosting'),
            }
           
            for k, v in data.items():
                ipinfo = (f'<b>{k}</b> : <i>{v}</i>')
#                   bot.send_message(message.chat.id,f"<b>{k} </b> : <i>{v}</i>", parse_mode='html')
                bot.send_message(message.chat.id, ipinfo, parse_mode='html')

        except:
#            print('[⚠️] Please give Valid IP Adress!') 
            bot.send_message(message.chat.id,"<b>[⚠️] Please give Valid IP Adress!</b>", parse_mode='html')



# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

#rejecting unwanted messages
@bot.message_handler(content_types=["photo", "gif", "sticker", "documents", "audio"])
def bad_msg(message):
    bot.reply_to(message, "<i>Bruh! now what am I supposed to do with dis</i> 😂", parse_mode="html")

# #rejecting unknown commands
# @bot.message_handler(commands=['lol'])
# @bot.message_handler(func=lambda message: message.from_user.id == message.chat.id)
# def unknown_msg(message):
#     bot.reply_to(message, "<i>lmao! no such command exist</i> 😂", parse_mode="html")

#catching edited messages
@bot.edited_message_handler(commands=['lol'])
def edited_msg(message):
    bot.send_message(message.chat.id, text="<i>Hehehe! I saw that..</i> 😂", parse_mode="html")

#normal message responder-------------------------------------------[ N ]
@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, f"Hello <b> {message.from_user.first_name}</b> ! How are you doing? ✌️", parse_mode='html')
    elif message.text == "myid":
        bot.send_message(message.chat.id, f'''
👻 - <b><u>Account Information</u></b>

◾- <b>Username: @{message.chat.username}</b>
◾- <b>Name: {message.chat.first_name}</b>
◾- <b>UserID:</b><code> {message.chat.id}</code>
◾- <b>Account:</b> {message.chat.type}
◾- <b>Language:</b> {message.from_user.language_code}
◾- <b>Bio:</b> {message.chat.bio}
◾- <b>Photo:</b> {message.chat.photo}
◾- <b>Date: {date1}</b>
◾- <b>Time: {time1}</b>
''', parse_mode='html')
    elif message.text == "sfw":
        try:
            bot.send_photo(message.chat.id, wallpaper_fun(k=1))
        except:
            bot.send_message(message.chat.id, f"Sorry <b> {message.from_user.first_name}</b>! Api under cooldown", parse_mode='html') 
    elif message.text == "nsfw":
        try:
            bot.send_photo(message.chat.id, wallpaper_fun(k=2))
        except:
            bot.send_message(message.chat.id, f"Sorry <b> {message.from_user.first_name}</b>! Api cooldown for 1min", parse_mode='html')


# logging
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

#keeps the bot alive-------------------------------------------[ Done ]
bot.add_custom_filter(IsAdmin())
bot.polling(none_stop=True)