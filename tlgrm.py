import telebot 

from telebot import types

API_token = '6334737276:AAHkkU9eZntjFhrM0VmrJTme5AwjhbdW2rU'

bot = telebot.TeleBot(API_token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    fbutton = types.KeyboardButton('text1')
    sbutton = types.KeyboardButton('text2')
    tbutton = types.KeyboardButton('text3')
    keyboard.add(fbutton, sbutton, tbutton)
    bot.send_message(message.chat.id, text= "Hello, I am a bot", reply_markup=keyboard)

@bot.message_handler(content_types=['photo'])
def picture(message):
        bot.send_message(message.chat.id, text= "Nice picture!")

@bot.message_handler(commands=['pic'])
def photo(message):
    with open ('image.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)

@bot.message_handler(content_types=['photo'])
def picture(message):
    file_id = message.photo[-1].file_id
    print(file_id)
    file_info = bot.get_file(file_id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    with open ('image.png', 'wb') as file:
        file.write(downloaded_file)
    with open ('image.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    bot.send_message(message.chat.id, text= message.text)

bot.polling(non_stop=True)

# make another message handler that will react on any picture and will respound with text, "nice picture!" "looks cool!"