from gc import callbacks

import telebot
from telebot import types
from urllib3 import disable_warnings

bot = telebot.TeleBot('') # Ваш токен, который вам присвоеили для работы с ботом
@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Участники проекта')
    btn2 = types.KeyboardButton('Упражнения для активного образа жизни')
    btn3 = types.KeyboardButton('Рецепты')
    btn4 = types.KeyboardButton('Полезные статьи')
    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.chat.id, 'Приветствуем вас с телеграмм-боте, {0.first_name}!'.format(message.from_user), reply_markup=markup) # Ответ на команду старт
@bot.message_handler(content_types=['text'])
def bot_message(message):
 if message.chat.type == 'private':
  if message.text == 'Участники проекта': # действия в кнопке расписание
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      bot.send_photo(message.chat.id, photo=open('wypisy0t.upa_..png', 'rb'),
                     caption='Над проектом работали:\n1. Лысунова Анастасия - собирала информацию о полезном питании, упражнениях для поддержания активного образа жизни!\n'
                             ' 2. Павлова София: Проявляла творческий подход к дизайну и интерфейсу бота, делая его более привлекательным и удобным в использовании.'
                             ' - \n3. Жиенко Алина: Разработала структуру и логику бота, обеспечивая плавную и интуитивную навигацию.  \n'
                             '4. Себелева Анна: Провела тщательное тестирование бота и отладила его работу, чтобы он был стабильным и безошибочным.')
  elif message.text == 'Упражнения для активного образа жизни':
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Полезные карточки с упражнениями', callback_data ="btn1")
    btn2 = types.InlineKeyboardButton('Видео тренировок', callback_data ="btn2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'С каким видом информации вы готовы ознакомиться ?:', reply_markup=markup)
  elif message.text == 'Рецепты':
      markup = types.InlineKeyboardMarkup(row_width=1)
      btn1 = types.InlineKeyboardButton('Рецепт1', callback_data="btn3")
      btn2 = types.InlineKeyboardButton('Рецепт2', callback_data="btn4")
      btn3 = types.InlineKeyboardButton('Рецепт3', callback_data="btn5")
      btn4 = types.InlineKeyboardButton('Рецепт4', callback_data="btn6")
      btn5 = types.InlineKeyboardButton('Рецепт5', callback_data="btn7")
      btn6 = types.InlineKeyboardButton('Рецепт6', callback_data="btn8")
      btn7 = types.InlineKeyboardButton('Рецепт7', callback_data="btn9")
      btn8 = types.InlineKeyboardButton('Рецепт8', callback_data="btn10")
      btn9 = types.InlineKeyboardButton('Рецепт9', callback_data="btn11")
      btn10 = types.InlineKeyboardButton('Рецепт10', callback_data="btn12")
      btn11 = types.InlineKeyboardButton('Рецепт11', callback_data="btn13")
      btn12 = types.InlineKeyboardButton('Рецепт12', callback_data="btn14")
      btn13 = types.InlineKeyboardButton('Рецепт13', callback_data="btn15")
      btn14 = types.InlineKeyboardButton('Рецепт14', callback_data="btn16")
      btn15 = types.InlineKeyboardButton('Рецепт15', callback_data="btn17")
      btn16 = types.InlineKeyboardButton('Рецепт16', callback_data="btn18")
      markup.add(btn1, btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16)
      bot.send_message(message.chat.id, 'Здесь представлен список полезных рецоптов с подсчетом калорий:', reply_markup=markup)
  elif message.text == 'Полезные статьи':
      markup = types.InlineKeyboardMarkup(row_width=1)  # Добавляем row_width=1 для отдельной строки для каждой кнопки
      btn100 = types.InlineKeyboardButton('1', callback_data="btn19")  # кнопки
      btn101 = types.InlineKeyboardButton('2', callback_data="btn20")
      btn102 = types.InlineKeyboardButton('3', callback_data="btn21")
      markup.row(btn100)  # Добавляем первую строку
      markup.row(btn101)  # Добавляем вторую строку
      markup.row(btn102)  # Добавляем третью строку
      bot.send_message(message.chat.id, 'Полезные статьи о питании и образе жизни', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "btn1":
        handle_button_1(call)
    elif call.data == "btn2":
        handle_button_2(call)
    elif call.data == "btn3":
        handle_button_3(call)
    elif call.data == "btn4":
        handle_button_4(call)
    elif call.data == "btn5":
        handle_button_5(call)
    elif call.data == "btn6":
        handle_button_6(call)
    elif call.data == "btn7":
        handle_button_7(call)
    elif call.data == "btn8":
        handle_button_8(call)
    elif call.data == "btn9":
        handle_button_9(call)
    elif call.data == "btn10":
        handle_button_10(call)
    elif call.data == "btn11":
        handle_button_11(call)
    elif call.data == "btn12":
        handle_button_12(call)
    elif call.data == "btn13":
        handle_button_13(call)
    elif call.data == "btn14":
        handle_button_14(call)
    elif call.data == "btn15":
        handle_button_15(call)
    elif call.data == "btn16":
        handle_button_16(call)
    elif call.data == "btn17":
        handle_button_17(call)
    elif call.data == "btn18":
        handle_button_18(call)
    elif call.data == "btn19":
        handle_button_19(call)
    elif call.data == "btn20":
        handle_button_20(call)
    elif call.data == "btn21":
        handle_button_21(call)
def handle_button_1(call):
    bot.send_photo(call.message.chat.id, photo=open('pict324-400343865.png', 'rb'), caption= 'Физические упражнения в домашних условиях' )
    bot.send_photo(call.message.chat.id, photo=open('696219e00d4c2f3950fece5b94843ce3.png', 'rb'), caption= 'Физические упражнения в домашних условиях' )

def handle_button_2(call):
    bot.send_message(call.message.chat.id, 'https://yandex.ru/video/preview/6197581116549940461',
                      disable_web_page_preview=True)
    bot.send_message(call.message.chat.id, 'https://yandex.ru/video/preview/18314911023323209007',
                      disable_web_page_preview=True)
    bot.send_message(call.message.chat.id,'https://yandex.ru/video/preview/985221726708820505',
                      disable_web_page_preview=True)

def handle_button_3(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_4(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_5(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_6(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_7(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_8(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_9(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_10(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_11(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_12(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_13(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_14(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_15(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_16(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_17(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')

def handle_button_18(call):
    bot.send_photo(call.message.chat.id, photo=open('ovsyanoblin-dlya-pravilnogo-pitaniya_1490091929_6_max.jpg', 'rb'), caption='[Ингридиенты для приготовления блюда]:\n - Овсяные хлопья - 1.5 стол.л\n '
                                                                                                                           '- Молоко - 15 мл\n - Яйца - 1 шт\n - Соль - по вкусу\n - Моцарелла - 15 гр\n - Огурцы - 0.3 шт\n - Салат айсберг - 25 гр\n - Растительное масло - 0.3 стол.л\n [БЖУ]:\n Белки - 14 гр\n Жиры - 16 гр\n Углеводы - 14 гр')


def handle_button_19(call):
    bot.send_message(call.message.chat.id, 'https://www.who.int/ru/news-room/fact-sheets/detail/healthy-diet',
                     disable_web_page_preview=True)  # Замените на вашу ссылку


def handle_button_20(call):
    bot.send_message(call.message.chat.id, 'https://cgon.rospotrebnadzor.ru/naseleniyu/zdorovyy-obraz-zhizni/chto-takoe-zdorovoe-pitanie/',
                     disable_web_page_preview=True)  # Замените на вашу ссылку


def handle_button_21(call):
    bot.send_message(call.message.chat.id, 'https://04.rospotrebnadzor.ru/index.php/press-center/press-reliz/18879-02112023.html', disable_web_page_preview = True)


bot.polling(non_stop=True)

