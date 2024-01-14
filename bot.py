from telebot import types
from parser_log import Products, Lostitems, Founditems
from decouple import config
import telebot

BOT_API = telebot.TeleBot((config('BOT_TOKEN')))
URL = config('URL')

product = Products()
lost_items = Lostitems()
found_items = Founditems()


def LostItem_bot(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_all_post = types.KeyboardButton("Получить все посты")
        item_lost_items = types.KeyboardButton("Получить всe потеряшки")
        item_found_items = types.KeyboardButton("Получить все найденные вещи")
        markup.add(item_all_post, item_lost_items, item_found_items)
        bot.send_message(message.chat.id, "Для получения всех постов нажмите кнопку:", reply_markup=markup)
        bot.send_message(message.chat.id, "Для получения всех потерянных вещей нажмите кнопку:", reply_markup=markup)
        bot.send_message(message.chat.id, "Для получения всех найденных вещей нажмите кнопку:", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Получить все посты')
    def get_all_posts(message):
        posts = product.get_all_post(URL)
        for post in posts.get('results'):
            title = post['title']
            desc = post['description']
            image = post['image']
            status = post['status']
            bot.send_message(message.chat.id, f'Заголовок: {title}\nОписание: {desc}\nИзображение: {image}\nСтатус: {status}')

    @bot.message_handler(func=lambda message: message.text == 'Получить всe потеряшки')
    def get_all_lost_items(message):
        l_items = lost_items.get_lost_items(URL)
        for item in l_items.get('results'):
            title = item['title']
            desc = item['description']
            image = item['image']
            status = item['status']
            bot.send_message(message.chat.id, f'Заголовок: {title}\nОписание: {desc}\nИзображение: {image}\nСтатус: {status}')

    @bot.message_handler(func=lambda message: message.text == "Получить все найденные вещи")
    def get_all_found_items(message):
        f_items = found_items.get_found_items(URL)
        for item in f_items.get('results'):
            title = item['title']
            desc = item['description']
            image = item['image']
            status = item['status']
            bot.send_message(message.chat.id, f'Заголовок: {title}\nОписание: {desc}\nИзображение: {image}\nСтатус: {status}')

    bot.polling(none_stop=True)

LostItem_bot(BOT_API)



        
