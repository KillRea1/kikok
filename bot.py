import telebot 
from telebot import types

TOKEN = '511358259:AAHZ1HJ7paJbNH3jnT21kqH4m-nThMMG-LA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,'Добрый день! Это бот Эмиля Усманова. С помощью этого бота вы сможете узнать информацию обо мне и моей общественной деятельности.')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name)for name in ['Обо мне','#фиолетоваясемья','Мои роли']])
    keyboard.add(*[types.KeyboardButton(name)for name in ['#СДОНЧ','Что делать дальше']])
    msg = bot.send_message(m.chat.id, 'Информация',reply_markup=keyboard)
    bot.register_next_step_handler(msg,lol)
    
@bot.message_handler(content_types=['text'])
def lol(m):
    if m.text == 'Обо мне':
        bot.send_message(m.chat.id,'Меня зовут Эмиль. Мне 14 лет,я родился в городе Набережные Челны. Являюсь активистом ДиМТОО "Фиолетовый НЕОН". Из моих интересов могу выделить: плавание,актерское мастерство и общественная деятельность')
    elif m.text == '#фиолетоваясемья':
        bot.send_message(m.chat.id,'Активист "Фиолетового Неона" я являюсь уже 3 года. И за это время я стал редактором нашей официальной группы , в которой освещаю самое интересное и значимые события. Так же за это время я участвовал в таких мероприятиях как: фестиваль"Действующие лица", Интеллектуальные игры "IQ-ZONE -Территория интеллекта" и Форум юных граждан.')
    elif m.text == 'Мои роли':
        bot.send_message(m.chat.id,'')
    elif m.text == '#СДОНЧ':
        bot.send_message(m.chat.id,'В СДО я представляю организацию "Фиолетовый НЕОН". На сборах СДО мы знакомимся с организациями нашего города, а на заседаниях освета мы знакомимся с организациями всей Республики Татарстан')
    elif m.text == 'Что делать дальше':
        keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboards.add(*[types.KeyboardButton(name)for name in ['Актерское мастерство','Общественная деятельность','Графический дизайн']])
        if m.text == 'Актерское мастерство':
            bot.send_message(m.chat.id,'')
        elif m.text == 'Общественная деятельность':
            bot.send_message(m.chat.id,'')
        elif m.text == 'Графический дизайн':
            bot.send_message(m.chat.id,'')
    else:
        bot.send_message(m.chat.id,'Несущестующая команда')
if __name__ == '__main__':
    bot.polling(none_stop=True)
