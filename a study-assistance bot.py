from operator import truediv

import telebot
from telebot import types
from urllib3 import disable_warnings

bot = telebot.TeleBot('') # Ваш токен, который вам присвоеили для работы с ботом

@bot.message_handler(commands=['start']) # Реагирование на команду /start
def start(message):
 markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Кнопки будут подгоняться под размер экрана
 btn1 = types.KeyboardButton('💻 Расписание') # кнопки
 btn2 = types.KeyboardButton('💾 Работы прошлых курсов')
 btn3 = types.KeyboardButton('👥 Разделение на подгруппы')
 btn4 = types.KeyboardButton('📚 Полезные ссылки')
 markup.add(btn1,btn2,btn3,btn4)
 bot.send_message(message.chat.id, 'Приветствую тебя в моем телеграмм боте, {0.first_name}!'.format(message.from_user), reply_markup=markup) # Ответ на команду старт

# реагирование на кнопки
@bot.message_handler(content_types=['text'])
def bot_message(message):
 if message.chat.type == 'private':
  if message.text == '💻 Расписание': # действия в кнопке расписание
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   bot.send_document(message.chat.id, document=open('files for studu-assistance bot/raspisanie_osen_3k.pdf', 'rb'), caption='Расписание занятий на 5 семестр!')
  elif message.text == '💾 Работы прошлых курсов': # действия в кнопке Работы прошлых курсов
   markup = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('📗 Все готово', callback_data="btn1")
   btn2 = types.InlineKeyboardButton('📙 Шоколадный торт', callback_data="btn2")
   markup.add(btn1,btn2)
   bot.send_message(message.chat.id, 'Выберите ссылку на диск:', reply_markup=markup)
  elif message.text == '👥 Разделение на подгруппы':
   bot.send_message(message.chat.id, 'Введи, пожалуйста, свою фамилию'.format(message.from_user))
  elif message.text == '📚 Полезные ссылки':
   markup = types.InlineKeyboardMarkup()  # Кнопки будут подгоняться под размер экрана
   btn3 = types.InlineKeyboardButton('🔒 Samsung Inovation campus', callback_data="btn3")  # кнопки
   btn4 = types.InlineKeyboardButton('📝 БРС', callback_data="btn4")
   btn5 = types.InlineKeyboardButton('📰 Sfedu.ru', callback_data="btn5")
   btn6 = types.InlineKeyboardButton('📬 Outlook', callback_data="btn6")
   btn7 = types.InlineKeyboardButton('📅 ИВТиПТ', callback_data="btn7")
   btn8 = types.InlineKeyboardButton('🔙 Назад', callback_data="btn8")
   markup.add(btn3, btn4, btn5, btn6, btn7, btn8)
   bot.send_message(message.chat.id,
                    'Тут представленны все полезные ссылки для 5 семестра'.format(message.from_user),
                    reply_markup=markup)







@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
 if call.data == "btn1":
  bot.send_message(call.message.chat.id, 'https://drive.google.com/drive/folders/1JZf84wDl7W4UMbO_g_WKje1RnbFinPOn?sort=13&direction=a', disable_web_page_preview=True)
 elif call.data == "btn2":
  bot.send_message(call.message.chat.id, 'https://drive.google.com/drive/folders/1JZf84wDl7W4UMbO_g_WKje1RnbFinPOn', disable_web_page_preview=True)
 elif call.data == "btn3":
  bot.send_message(call.message.chat.id, 'https://innovationcampus.ru/lms/login/index.php', disable_web_page_preview=True)
 elif call.data == "btn4":
  bot.send_message(call.message.chat.id, 'https://grade.sfedu.ru',disable_web_page_preview=True)
 elif call.data == "btn5":
  bot.send_message(call.message.chat.id, 'https://sfedu.ru', disable_web_page_preview=True)
 elif call.data == "btn6":
  bot.send_message(call.message.chat.id, 'https://outlook.office.com/mail/', disable_web_page_preview=True)
 elif call.data == "btn7":
  bot.send_message(call.message.chat.id, 'https://ivtipt.ru', disable_web_page_preview=True)
 elif call.data == "btn8":
  bot.send_message(call.message.chat.id, '', disable_web_page_preview=True)
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Кнопки будут подгоняться под размер экрана
  btn1 = types.KeyboardButton('💻 Расписание') # кнопки
  btn2 = types.KeyboardButton('💾 Работы прошлых курсов')
  btn3 = types.KeyboardButton('👥 Разделение на подгруппы')
  btn4 = types.KeyboardButton('📚 Полезные ссылки')
  markup.add(btn1,btn2,btn3,btn4)
  
bot.polling(non_stop=True)
