import telebot
from telebot import types

# Вставьте сюда свой токен
TOKEN = '7022111070:AAF8HPR4ed4PfFrBMocMxyzAD62_IaQLgDY'
bot = telebot.TeleBot(TOKEN)

# Часто задаваемые вопросы и ответы
FAQ = {
    "Как сделать заказ?": "Чтобы сделать заказ, перейдите на наш сайт и выберите товары, которые вас интересуют.",
    "Какие способы оплаты?": "Мы принимаем оплату через банковские карты, PayPal и Apple Pay.",
    "Как вернуть товар?": "Для возврата товара заполните форму возврата на нашем сайте или свяжитесь с поддержкой."
}

# Список операторов (ID телеграм-аккаунтов)
OPERATORS = [123456789, 987654321]  # Замените на реальные ID операторов


# Команда старт / стартовое меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Часто задаваемые вопросы")
    button2 = types.KeyboardButton("Связаться с оператором")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Добро пожаловать в службу поддержки! Как я могу вам помочь?", reply_markup=markup)

    # Обработка текста

#dfddfьь
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Часто задаваемые вопросы":
        markup = types.InlineKeyboardMarkup()
        for question in FAQ.keys():
            btn = types.InlineKeyboardButton(question, callback_data=question)
            markup.add(btn)
        bot.send_message(message.chat.id, "Выберите вопрос:", reply_markup=markup)
    elif message.text == "Связаться с оператором":
        bot.send_message(message.chat.id, "Ваш запрос отправлен оператору. Ожидайте ответа.")
        notify_operator(message)
    else:
        bot.send_message(message.chat.id, "Извините, я не понимаю этот запрос. Выберите один из доступных вариантов.")

#ответы на FAQ
@bot.callback_query_handler(func=lambda call:True)
def handle_faq(call):
    answer = FAQ.get(call.data,"ответ на этот вопрос пока отсутствует")
    bot.send_message(call.message.chat.id,answer)

#уведомление оператора о запросе клиента
def notify_operator(message):
    for operator_id in OPERATORS:
        bot.send_message(operator_id, f"Запрос от пользователя @{message.chat.username}:\n{message.text}")
    bot.send_message(message.chat.id, "Оператор скоро свяжется с вами.")























    # Запуск бота

bot.polling()