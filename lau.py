import telebot

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def send_response(message):
        if message.text == "Buongiorno":
            bot.send_message(message.chat.id, "Buongiorno, come posso aiutarla?")
        elif message.text == "Ho un problema con il mio ordine":
            bot.send_message(message.chat.id, "Ha inserito correttamente il codice promozionale?")
        elif message.text == "Si, voglio parlare con un operatore":
            bot.send_message(message.chat.id, "Ok, adesso verrai contattato da un operatore. A presto!")

bot.infinity_polling()
