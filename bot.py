from parser_log import Products, Login
from decouple import config
import telebot

BOT_API = telebot.TeleBot((config('BOT_TOKEN')))
URL = config('URL')

product = Products()
login_manager = Login() 
is_user_login_in = False

def LostItem_bot(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}! \n Для начала работы введите логин и пароль:')

    @bot.message_handler(content_types='text')
    def process_login(message):
        global is_user_login_in
        if is_user_login_in == False:
            req = login_manager.login(URL, message.text.split()[0], message.text.split()[1])
            if req == 'Неверный логин или пароль':
                bot.send_message(message.chat.id, 'Неверный логин или пароль')
            else:
                bot.send_message(message.chat.id, 'Вы вошли в аккаунт')
                is_user_login_in = True
        
    @bot.message_handler(commands=['get_all_posts'])
    def get_all_posts(message):
        global is_user_login_in
        if is_user_login_in:
            posts = product.get_all_post(URL)
            print(posts)
            bot.send_message(message.chat.id, f'Все посты:\n{posts}')
            
        else:
            bot.send_message(message.chat.id, 'Вы не вошли в аккаунт. Введите логин и пароль с помощью команды /start.')

    bot.polling()

LostItem_bot(BOT_API)

# print(product.get_all_post(URL))
# print(login.login(URL, 'bilal@gmail.com', '12345'))