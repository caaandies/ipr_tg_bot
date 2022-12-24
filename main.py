from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from googletrans import Translator



TOKEN='5903197093:AAEmHeiWFpVdRGGe3b75_BJvXfcGlmtcRog'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
translator = Translator()


@dp.message_handler(commands=['start'])
async def start_message(message):
    text = "Используй /help, чтобы просмотреть функционал"
    await bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(commands=['help'])
async def start_message(message):
    text = "/translate_eng + text чтобы перевести предложение с русского на английский\n" \
           "/translate_spa + text чтобы перевести предложение с русского на испанский\n" \
           "/translate_ita + text чтобы перевести предложение с русского на итальянский\n" \
           "/translate_fra + text чтобы перевести предложение с русского на французский\n" \
           "/translate_ger + text чтобы перевести предложение с русского на немецкий"
    await bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(commands=['translate_eng'])
async def to_eng(message):
    start = len('translate_eng') + 1
    msg = message.text[start::]
    if not msg:
        await bot.send_message(chat_id=message.chat.id, text="введите текст после команды")
    else:
        tr_msg = translator.translate(msg, src='ru', dest='en').text
        await bot.send_message(chat_id=message.chat.id, text=tr_msg)


@dp.message_handler(commands=['translate_spa'])
async def to_eng(message):
    start = len('translate_spa') + 1
    msg = message.text[start::]
    if not msg:
        await bot.send_message(chat_id=message.chat.id, text="введите текст после команды")
    else:
        tr_msg = translator.translate(msg, src='ru', dest='es').text
        await bot.send_message(chat_id=message.chat.id, text=tr_msg)



@dp.message_handler(commands=['translate_ita'])
async def to_eng(message):
    start = len('translate_ita') + 1
    msg = message.text[start::]
    if not msg:
        await bot.send_message(chat_id=message.chat.id, text="введите текст после команды")
    else:
        tr_msg = translator.translate(msg, src='ru', dest='it').text
        await bot.send_message(chat_id=message.chat.id, text=tr_msg)


@dp.message_handler(commands=['translate_fra'])
async def to_eng(message):
    start = len('translate_fra') + 1
    msg = message.text[start::]
    if not msg:
        await bot.send_message(chat_id=message.chat.id, text="введите текст после команды")
    else:
        tr_msg = translator.translate(msg, src='ru', dest='fr').text
        await bot.send_message(chat_id=message.chat.id, text=tr_msg)


@dp.message_handler(commands=['translate_ger'])
async def to_eng(message):
    start = len('translate_ger') + 1
    msg = message.text[start::]
    if not msg:
        await bot.send_message(chat_id=message.chat.id, text="введите текст после команды")
    else:
        tr_msg = translator.translate(msg, src='ru', dest='de').text
        await bot.send_message(chat_id=message.chat.id, text=tr_msg)

executor.start_polling(dp)
