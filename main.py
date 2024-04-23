import telebot

with open("token.txt") as f:
    TOKEN = f.readline()
bot = telebot.TeleBot(TOKEN)


def text_check(text):
    return True


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.reply_to(msg, "Ну здрасте")


@bot.message_handler(commands=['help'])
def send_help(msg):
    bot.reply_to(msg, "Ты мне что-то напишешь, я напишу тебе то же самое. Ну разве я не лучший?")


@bot.message_handler(func=text_check)
def echo_all(msg):
    bot.reply_to(msg, text=msg.text)


bot.infinity_polling()
