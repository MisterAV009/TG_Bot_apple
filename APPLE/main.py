import telebot
import random
from telebot.types import Message, ReplyKeyboardMarkup as rlm, ReplyKeyboardRemove as rkr
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
clear = rkr()
resources = ["Железо", "Золото", 'Уголь', "Уран", "Медь", "Титан", "Марганец", "Колчедан", "Цинк",
             "Хром", "Алмазы", 'редстоун', 'лазурит', "Изумруд", "радий", 'камень', 'дерево', 'кости', 'глина', 'песок',
             'корень', 'метеорит', 'гранит', 'сапфир', 'бриллиант', 'скелет', 'торф', 'Игорь']


@bot.message_handler(commands=["start"])
def start(m: Message):
    kb = rlm(resize_keyboard=False)
    kb.row("Копать")
    bot.send_message(m.chat.id, 'Привет, хочешь со мной покопать сокровища? жми копать!', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def text(m: Message):
    if m.from_user.is_bot:
        return
    if m.text == 'Копать':
        res = random.choice(resources)
        bot.send_message(m.chat.id, f'Вот что ты добыл своим тяжким трудом благодаря мне: {res}')
        chance = random.randint(1, 100)
        print(chance)
        if chance in range(1, 6):
            bot.send_message(m.chat.id, 'Ты раскопал сокровище,ПРОМОКОД - "SuperPromo2024"', reply_markup=clear)


bot.infinity_polling()
