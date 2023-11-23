import telebot
from telebot import types
from anecAPI import anecAPI


bot = telebot.TeleBot('6890710062:AAH8sioeespVNKiGwR2MCIBLcUZYITEXfL0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здрав будь, славный покоритель озоновских пунктов!')


def markup_menu(for_buttons):
    mark = types.InlineKeyboardMarkup()
    sp = []
    for y, x in enumerate(for_buttons):
        if x[1] == 'callback':
            but = types.InlineKeyboardButton(text=x[0], callback_data=x[2])
        else:
            but = types.InlineKeyboardButton(text=x[0], url=x[2])
        sp.append(but)
        if len(sp) > 1:
            mark.row(sp[0], sp[1])
            sp.clear()
        if sp and y == 0:
            mark.row(sp[0])
            sp.clear()
    if sp:
        mark.row(sp[0])
    return mark


@bot.message_handler(['menu'])
def menu(message):
    buts = [['ШУТКА', 'callback', 'ШУТКА']]
    bot.send_message(message.chat.id,
                     'Привет, сладкий!',
                     reply_markup=markup_menu(buts))


@bot.callback_query_handler(func=lambda callback: True)
def joke(callback):
    if callback.data == 'ШУТКА':
        bot.send_message(callback.message.chat.id, anecAPI.random_joke())


bot.polling(none_stop=True, interval=0)