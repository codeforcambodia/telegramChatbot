import telebot
from telebot import types

bot_token = ''
bot = telebot.TeleBot(token = bot_token)
def answer():
    @bot.message_handler(regexp='ello')
    def wellcome(msg):
        bot.reply_to(msg, "Hello I am Delta \U0001f604\nNice to meet you.")

    @bot.message_handler(regexp="orning")
    def fine(msg):
        bot.reply_to(msg, "Good morning! have a good day.")

    @bot.message_handler(regexp="fterno")
    def fine(msg):
        bot.reply_to(msg, "Good afternoon! Today is hot.")

    @bot.message_handler(regexp="ight")
    def fine(msg):
        bot.reply_to(msg, "Good night! have a good dream.")

    @bot.message_handler(regexp="ye")
    def fine(msg):
        bot.reply_to(msg, "bye bye see you next time.")


    @bot.message_handler(regexp="ow are")
    def fine(msg):
        bot.reply_to(msg, "I'm always fine, thank!\nWhat about you ?")

    @bot.message_handler(regexp="ine")
    @bot.message_handler(regexp="ot bad")
    def answer(msg):
        bot.reply_to(msg, "I'm happy with you !")

    @bot.message_handler(regexp="ad")
    @bot.message_handler(regexp="ot ")
    def answer(msg):
        bot.reply_to(msg, "I feel sorry with you !")

    @bot.message_handler(regexp=" old")
    def answer(msg):
        bot.reply_to(msg, "I was born many day ago.")

    @bot.message_handler(regexp="elp")
    def answer(msg):
        bot.reply_to(msg,"what are you need me to help ?\nYou can search at\nhttps://www.google.com")

    @bot.message_handler(regexp="hank")
    def answer(msg):
        bot.reply_to(msg, "No, problem because we are friend.")


def start1():
    @bot.message_handler(commands=["start"])
    def help(msg):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("News")
        item2 = types.KeyboardButton("Music")
        item3 = types.KeyboardButton("Movie")
        item4 = types.KeyboardButton("Game")
        item5 = types.KeyboardButton("Education")
        markup.row(item5, item1)
        markup.row(item4, item2, item3)
        bot.reply_to(msg, "Choose one of type ", reply_markup=markup)


    @bot.message_handler(regexp="news")
    def news(msg):
        bot.reply_to(msg, "https://www.foxnews.com/")


    @bot.message_handler(regexp="music")
    def music(msg):
        bot.reply_to(msg, "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")


    @bot.message_handler(regexp="education")
    def music(msg):
        bot.reply_to(msg, "https://www.codecademy.com/")


    @bot.message_handler(regexp="movie")
    def movie(msg):
        bot.reply_to(msg, "https://www.movie2free.com")


    @bot.message_handler(regexp="game")
    def game(msg):
        bot.reply_to(msg, "https://www.gamespot.com")
def know():
    @bot.message_handler(func=lambda message: True)
    def ehco_all(msg):
        bot.reply_to(msg,"I don't Understad {}".format(msg.text))

def keyword():
    @bot.message_handler(regexp="password")
    def answer(msg):
        bot.reply_to(msg, "Your password = 12345678")

    @bot.message_handler(regexp="cosmos")
    def anser(msg):
        bot.reply_to(msg, "https://www.youtube.com/watch?v=Y1zfL74pkwo")



start1()
answer()
keyword()
know()
bot.polling()
