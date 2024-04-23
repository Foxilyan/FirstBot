import telebot

with open("token.txt") as f:
    TOKEN = f.readline()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, "У меня выходной")


@bot.message_handler(content_types=['photo'])
def handle_image(msg):
    bot.reply_to(msg, "Это определенно картинка")


@bot.message_handler(regexp="SOME_REGEXP")
def handle_message_by_regexp(msg):
    bot.reply_to(msg, "Не дай боже придется с этим работать...")


@bot.message_handler(func=lambda msg: msg.text == "биба")
def handle_biba(msg):
    bot.reply_to(msg, "боба")


def check_pupa(msg):
    return msg.text == "пупа"


@bot.message_handler(func=check_pupa)
def handle_pupa(msg):
    bot.reply_to(msg, "лупа")


bot.infinity_polling()
