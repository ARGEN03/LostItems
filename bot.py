from telebot import types
from parser_log import Products, Lostitems
from decouple import config
import telebot

BOT_API = telebot.TeleBot((config('BOT_TOKEN')))
URL = config('URL')

product = Products()
lost_items = Lostitems()
is_user_login_in = False

def LostItem_bot(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_all_post = types.KeyboardButton("Получить все посты")
        item_lost_items = types.KeyboardButton("Получить всe потеряшки")
        markup.add(item_all_post, item_lost_items)
        bot.send_message(message.chat.id, "Для получения всех постов нажмите кнопку:", reply_markup=markup)
        bot.send_message(message.chat.id, "Для получения всех потерянных вещей нажмите кнопку:", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Получить все посты')
    def get_all_posts(message):
        posts = product.get_all_post(URL)
        for post in posts['results']:
            title = post["title"]
            desc = post['description']
            image = post['image']
            status = post['status']
            bot.send_message(message.chat.id, f'Заголовок: {title}\nОписание: {desc}\nИзображение: {image}\nСтатус: {status}')

    @bot.message_handler(func=lambda message: message.text == 'Получить всe потеряшки')
    def get_all_lost_items(message):
        l_items = lost_items.get_lost_items(URL)
        for item in l_items['results']:
            title = item["title"]
            desc = item['description']
            image = item['image']
            status = item['status']
            bot.send_message(message.chat.id, f'Заголовок: {title}\nОписание: {desc}\nИзображение: {image}\nСтатус: {status}')

    # print(type(lost_items.get_lost_items(URL)))
    # Запуск бота
    bot.polling(none_stop=True)

LostItem_bot(BOT_API)
# posts = product.get_all_post(URL)
# for post in posts['results']:
#     if post['image'] is not None:
#         print(post['image'][29:])
#     else:
#         print(None)

# posts = product.get_all_post(URL)
# for post in posts['results']:
     
#     print(post['title'])

#
        
