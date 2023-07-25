# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строки
# 'telebot'
import telebot
import random
from telebot import types

# Токен вашего бота, который вы получили от BotFather
TOKEN = 'TOKEN'

# Список мотивирующих сообщений
motivational_messages = [
    "Ты сможешь все, во что поверишь!",
    "Никогда не сдавайся, потому что успех находится за углом!",
    "Ты уникален и способен на великие дела!",
    "Твои возможности безграничны, просто поверь в себя!",
    "Каждый день - новая возможность стать лучше!",
    "Успех - это способность идти от поражения к поражению без потери энтузиазма. - Уинстон Черчилль",
    "Сделай сегодня то, что другие не хотят, чтобы завтра получить то, чего другие не смогут. - Чак Джонсон",
    "Твой будущий успех зависит от сегодняшних решений и действий. - Билл Косби",
    "Только тот, кто считает возможным, то что невозможно, может добиться невозможного. - Альберт Эйнштейн",
    "Если ты можешь мечтать, то можешь и достичь своих целей. - Зиг Зиглар",
    "Никогда не сдавайся, потому что успех находится за следующим поворотом. - Аноним",
    "Только начав движение, мы обнаруживаем ресурсы, которые нам необходимы. - Уильям Джеймс",
    "Секрет успеха в том, чтобы делать обычные вещи необычно хорошо. - Джон Рокфеллер",
    "Не откладывай на завтра то, что можно сделать сегодня. - Бенджамин Франклин",
    "Если хочешь, чтобы что-то было сделано правильно, сделай это сам. - Наполеон Бонапарт",
    "Смелость — это когда страшно, но делаешь все равно. - Аристотель",
    "Каждая мечта начинается с маленького шага вперед. - Лао Цзы",
    "Если ты не можешь лететь, беги. Если не можешь бежать, иди. Если не можешь идти, ползи, но продолжай двигаться вперед. - Мартин Лютер Кинг мл.",
    "Мечты сбываются, когда вы внедряете в них сердце. - Антуан де Сент-Экзюпери",
    "Начинай делать то, что нужно, потом то, что возможно, и вдруг обнаружишь, что ты делаешь невозможное. - Франциск Ассизский",
    "Будь смелым и сильным; не смейся над собой, не забывай, что смеяться над собой — всегда значит смеяться над Богом. - Антон Павлович Чехов",
    "Ничто так не укрепляет характер, как возможность сказать: я справился с трудностями. - Альберт Швейцер",
    "Успех - это способность двигаться от неудачи к неудаче без потери энтузиазма. - Уинстон Черчилль",
    "Жизнь — это 10% того, что с вами происходит, и 90% того, как вы на это реагируете. - Чарльз Р. Суиндолл",
    "Если вы можете мечтать, вы можете и достичь своей мечты. - Зиг Зиглар",
    "Поставь перед собой невозможные задачи и ты достигнешь невероятных результатов. - Грег С. Рид",
    "Жизнь — это просто игра, будь счастлив внутри себя и будешь счастлив вовне. - Сантьяго Рамирес",
    "Возможности появляются у тех, кто ищет способы, а не у тех, кто ищет оправдания. - Наполеон Хилл",
    "Неудача — это просто возможность начать снова, но уже более мудро. - Генри Форд",
    "Без муки нет победы. - Эмиль Золя",
    "Не ждите. Время никогда не будет подходящим. | Наполеон Хилл",
    "Неисследованная жизнь не стоит того, чтобы ее жить. | Сократ",
    "Усердно работайте, мечтайте по-крупному.",
    "Я не потерпел неудачу. Я просто нашел 10 000 способов, которые не работают. | Томас Эдисон",
    "Мотивация - это то, что заставляет вас начать. Привычка - это то, что заставляет вас продолжать. | Джим Рюн",
    "Вы должны выучить правила игры. А затем вы должны играть лучше, чем кто-либо другой. | Альберт Эйнштейн",
    "Если вы потратите свою жизнь на то, чтобы быть лучшим во всем, вы никогда не станете великим ни в чем. | Том Рат",
    "Сначала они не замечают тебя, затем смеются над тобой, потом борются с тобой, а потом ты побеждаешь. | Махатма Ганди",
    "Мечтатели - это спасители мира. | Джеймс Аллен",
    "Чем больше вы преодолеваете, тем сильнее вы становитесь. - Неизвестный",
    "Поставь перед собой цель и двигайся к ней, шаг за шагом, без отступлений. - Лес Браун",
    "Всегда есть выбор. Мы всегда можем решить, что делать дальше. - Оливия Бишоп",
    "Если вам кажется, что что-то возможно, то вы правы, если кажется, что невозможно — вы тоже правы. - Генри Форд",
    "Будь смелее, чем ты думаешь, сильнее, чем кажешься, и умнее, чем думаешь. - Неизвестный",
]

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_motivational_message(message):
    # Создаем пользовательскую клавиатуру с кнопкой "Щепоточку хороших слов"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Щепоточку хороших слов")
    markup.add(item)

    # Отправляем приветственное сообщение с клавиатурой
    bot.reply_to(message, "Привет! Я мотивационный бот. Нажми кнопку 'Щепоточку хороших слов', чтобы получить мотивацию.", reply_markup=markup)

# Обработчик кнопки "Щепоточку хороших слов"
@bot.message_handler(func=lambda message: message.text == "Щепоточку хороших слов")
def send_random_motivational_message(message):
    # Выбираем случайное мотивирующее сообщение из списка
    random_message = random.choice(motivational_messages)
    # Отправляем сообщение пользователю
    bot.reply_to(message, random_message)

# Запуск бота
bot.polling()