# Импорты
import sqlite3
import re
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboards as kb

# Переменные
TOKEN = "BOT_TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
con = sqlite3.connect("database.db")
cur = con.cursor()

# Id админов
sveta_id = 535400200
sveta2_id = 1933711136
gordey_id = 778322817
anton_id = 428627854
pasha_id = 874137486

# Создание базы данных
def create_database():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS database(dz TEXT);')

# Функиция записывания информации в базу
async def info_writer(database):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    mass = []
    mass.append(database)
    cur.execute('INSERT INTO database VALUES(?)', mass)
    con.commit()
    cur.close()

# Фильтр лишних символов + \n + отправка
async def send_base():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    query = 'SELECT * FROM database'
    cur.execute(query)
    data = cur.fetchall()
    clear_list=[]
    for i in data:
        clear_list.append(i[0])
        info="\n".join(str(e) for e in clear_list)
    return info

# Старт
@dp.message_handler(commands=['start'])
async def show_menu(message: types.Message):
    if message.from_user.id == sveta_id:
        await message.answer('Здравствуйте, выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == gordey_id:
        await message.answer('Здравствуйте, выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == anton_id:
        await message.answer('Здравствуйте, выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == pasha_id:
        await message.answer('Здравствуйте, выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == sveta2_id:
        await message.answer('Здравствуйте, выберите категорию', reply_markup=kb.start4adm_keyboard)
    else:
        await message.answer('Здравствуйте, выберите категорию', reply_markup=kb.start_keyboard)

# Вернуться
@dp.message_handler(text='Вернуться')
async def back(message: types.Message):
    if message.from_user.id == sveta_id:
        await message.answer('Выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == pasha_id:
        await message.answer('Выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == gordey_id:
        await message.answer('Выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == anton_id:
        await message.answer('Выберите категорию', reply_markup=kb.start4adm_keyboard)
    elif message.from_user.id == sveta2_id:
        await message.answer('Выберите категорию', reply_markup=kb.start4adm_keyboard)
    else:
        await message.answer('Выберите категорию', reply_markup=kb.start_keyboard)

# Загрузить дз
@dp.message_handler(text='Загрузить дз')
async def adm_download(message: types.Message):
    await message.answer(
        'Напишите команду /add, предмет и дз, чтобы добавить домашку.\nПример: /add Алгебра : упражнения 1,2,3.\nНужна помощь? Напишите @kejszn.',
        reply_markup=kb.otmena_keyboard)

# Расписание звонков
@dp.message_handler(text='Посмотреть звонки')
async def zvonki(message: types.Message):
    text = "Держи"
    photo = open("raspisaniezvonkov.png", "rb")
    await bot.send_photo(caption=text, chat_id=message.chat.id, photo=photo, reply_markup=kb.otmena_keyboard)

# Расписание
@dp.message_handler(text='Посмотреть расписание')
async def raspisanie(message: types.Message):
    await message.answer('Выберите день недели: ', reply_markup=kb.nedelya_keyboard)

# Понедельник
@dp.message_handler(text='Понедельник')
async def ponedelnik(message: types.Message):
    await message.answer(
        '<a href="url.com/mHGZgw">1. Мистецтво</a>\n<a href="url.com/D8-g-U">2. Биология</a>\n<a href="url.com/WA7y5m">3. География</a>\n<a href="url.com/U6pdLJ">4. Алгебра</a>\n<a href="url.com/IFPjun">5. Экономика</a>\n<a href="url.com/1kqOaJ">6. Укр лит</a>', 
        parse_mode="HTML")

# Вторник
@dp.message_handler(text='Вторник')
async def vtornik(message: types.Message):
    await message.answer(
        '0. Физика\n<a href="url.com/U6pdLJ">1. Алгебра</a>\n<a href="url.com/U6pdLJ">2. Геометрия</a>\n<a href="url.com/Vbg_f7">3. Химия</a>\n<a href="url.com/1kqOaJ">4. Укр мова</a>\n<a href="url.com/1kqOaJ">5. Укр лит</a>\n<a href="url.com/fMywI6">6. Право</a>\n<a href="url.com/1kqOaJ">7. Рос мова</a>',
        parse_mode="HTML")

# Среда
@dp.message_handler(text='Среда')
async def sreda(message: types.Message):
    await message.answer(
        '<a href="url.com/1kqOaJ">1. Укр мова</a>\n<a href="url.com/U6pdLJ">2. Алгебра</a>\n<a href="url.com/1kqOaJ">3. Зар лит</a>\n<a href="url.com/SX4Bhr">4. Физ-ра</a>\n<a href="url.com/SX4Bhr">5. Физ-ра</a>\n<a href="url.com/SX4Bhr">6. Физ-ра</a>\n<a href="url.com/3MrRsS">7. Ист Украины</a>',
        parse_mode="HTML")

# Четверг
@dp.message_handler(text='Четверг')
async def chetverg(message: types.Message):
    await message.answer(
        '<a href="url.com/Vbg_f7">0. Химия</a>\n<a href="url.com/U6pdLJ">1. Геометрия</a>\n2. Английский\n3. Информатика\n4. Информатика\n<a href="url.com/IFPjun">5. География</a>\n<a href="url.com/D8-g-U">6. Биология</a>\n<a href= "url.com/5PNXFj">7. Французский</a>\n<a href= "url.com/5PNXFj">8. Французский</a>',
        parse_mode="HTML")

# Пятница
@dp.message_handler(text='Пятница')
async def pyatnica(message: types.Message):
    await message.answer(
        '1. Английский\n<a href="url.com/D8-g-U">2. Основы</a>\n<a href="url.com/1kqOaJ">3. Зар лит</a>\n4. Физика\n5. Физика\n<a href="url.com/3MrRsS">6. Ист Всемир</a>\n<a href= "url.com/P8HFl0">7. Немецкий</a>\n<a href= "url.com/P8HFl0">8. Немецкий</a>',
        parse_mode="HTML")

# Для группы
@dp.message_handler(commands=['s'])
async def process_group(message: types.Message):
    predm = ' '.join(message.text.split(" ")[1:])
    if predm == "биология":
        await bot.send_message(message.chat.id, '<a href="url.com/D8-g-U">Биология</a>', parse_mode="HTML")
    if predm == "основы":
        await bot.send_message(message.chat.id, '<a href="url.com/D8-g-U">Основы</a>', parse_mode="HTML")
    if predm == "осн здор":
        await bot.send_message(message.chat.id, '<a href="url.com/D8-g-U">Основы</a>', parse_mode="HTML")
    if predm == "основы здоровья":
        await bot.send_message(message.chat.id, '<a href="url.com/D8-g-U">Основы</a>', parse_mode="HTML")
    if predm == "укр мова":
        await bot.send_message(message.chat.id, '<a href="url.com/1kqOaJ">Укр мова</a>', parse_mode="HTML")
    if predm == "укр лит":
        await bot.send_message(message.chat.id, '<a href="url.com/1kqOaJ">Укр лит</a>', parse_mode="HTML")
    if predm == "зар лит":
        await bot.send_message(message.chat.id, '<a href="url.com/1kqOaJ">Зар лит</a>', parse_mode="HTML")
    if predm == "рос мова":
        await bot.send_message(message.chat.id, '<a href="url.com/1kqOaJ">Рос мова</a>', parse_mode="HTML")
    if predm == "русский":
        await bot.send_message(message.chat.id, '<a href="url.com/1kqOaJ">Рос мова</a>', parse_mode="HTML")
    if predm == "мистецтво":
        await bot.send_message(message.chat.id, '<a href="url.com/mHGZgw">Мистецтво</a>', parse_mode="HTML")
    if predm == "исскуство":
        await bot.send_message(message.chat.id, '<a href="url.com/mHGZgw">Мистецтво</a>', parse_mode="HTML")
    if predm == "география":
        await bot.send_message(message.chat.id, '<a href="url.com/WA7y5m">География</a>', parse_mode="HTML")
    if predm == "алгебра":
        await bot.send_message(message.chat.id, '<a href="url.com/U6pdLJ">Алгебра</a>', parse_mode="HTML")
    if predm == "алг":
        await bot.send_message(message.chat.id, '<a href="url.com/U6pdLJ">Алгебра</a>', parse_mode="HTML")
    if predm == "геометрия":
        await bot.send_message(message.chat.id, '<a href="url.com/U6pdLJ">Геометрия</a>', parse_mode="HTML")
    if predm == "геом":
        await bot.send_message(message.chat.id, '<a href="url.com/U6pdLJ">Геометрия</a>', parse_mode="HTML")
    if predm == "економика":
        await bot.send_message(message.chat.id, '<a href="url.com/WA7y5m">Экономика</a>', parse_mode="HTML")
    if predm == "эконом":
        await bot.send_message(message.chat.id, '<a href="url.com/WA7y5m">Экономика</a>', parse_mode="HTML")
    if predm == "економ":
        await bot.send_message(message.chat.id, '<a href="url.com/WA7y5m">Экономика</a>', parse_mode="HTML")
    if predm == "экономика":
        await bot.send_message(message.chat.id, '<a href="url.com/WA7y5m">Экономика</a>', parse_mode="HTML")
    if predm == "химия":
        await bot.send_message(message.chat.id, '<a href="url.com/Vbg_f7">Химия</a>', parse_mode="HTML")
    if predm == "право":
        await bot.send_message(message.chat.id, '<a href="url.com/fMywI6">Право</a>', parse_mode="HTML")
    if predm == "физра":
        await bot.send_message(message.chat.id, '<a href="url.com/SX4Bhr">Физ-ра</a>', parse_mode="HTML")
    if predm == "физ-ра":
        await bot.send_message(message.chat.id, '<a href="url.com/SX4Bhr">Физ-ра</a>', parse_mode="HTML")
    if predm == "физкультура":
        await bot.send_message(message.chat.id, '<a href="url.com/SX4Bhr">Физ-ра</a>', parse_mode="HTML")
    if predm == "история":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">История</a>', parse_mode="HTML")
    if predm == "ист":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">История</a>', parse_mode="HTML")
    if predm == "история Украины":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">Ист Украины</a>', parse_mode="HTML")
    if predm == "история украины":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">История Украины</a>', parse_mode="HTML")
    if predm == "история укр":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">Ист Украины</a>', parse_mode="HTML")
    if predm == "история всемирная":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">История Всемир</a>', parse_mode="HTML")
    if predm == "история всем":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">История Всемир</a>', parse_mode="HTML")    
    if predm == "история всемир":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">История Всемир</a>', parse_mode="HTML")   
    if predm == "история Укр":
        await bot.send_message(message.chat.id, '<a href="url.com/3MrRsS">Ист Украины</a>', parse_mode="HTML")
    if predm == "франц":
        await bot.send_message(message.chat.id, '<a href="url.com/5PNXFj">Французский</a>', parse_mode="HTML")   
    if predm == "французский":
        await bot.send_message(message.chat.id, '<a href="url.com/5PNXFj">Французский</a>', parse_mode="HTML")
    if predm == "немецкий":
        await bot.send_message(message.chat.id, '<a href="url.com/P8HFl0">Немецкий</a>', parse_mode="HTML")
    if predm == "нем":
        await bot.send_message(message.chat.id, '<a href="url.com/P8HFl0">Немецкий</a>', parse_mode="HTML")

# Удаление
@dp.message_handler(text='Удалить дз')
async def process_delete(message: types.Message):
    if message.from_user.id == sveta_id:
        cur.execute('DELETE FROM database')
        con.commit()
        await bot.send_message(message.chat.id, "Дз успешно удалено из базы")
    elif message.from_user.id == sveta2_id:
        cur.execute('DELETE FROM database')
        con.commit()
        await bot.send_message(message.chat.id, "Дз успешно удалено из базы")
    elif message.from_user.id == pasha_id:
        cur.execute('DELETE FROM database')
        con.commit()
        await bot.send_message(message.chat.id, "Дз успешно удалено из базы")
    elif message.from_user.id == gordey_id:
        cur.execute('DELETE FROM database')
        con.commit()
        await bot.send_message(message.chat.id, "Дз успешно удалено из базы")
    elif message.from_user.id == anton_id:
        cur.execute('DELETE FROM database')
        con.commit()
        await bot.send_message(message.chat.id, "Дз успешно удалено из базы")
    else:
        await bot.send_message(message.chat.id, "Вы не можете вносить изменения в базу")

# Добавление
@dp.message_handler(commands=['add'])
async def process_add(message: types.Message):
    result = ' '.join(message.text.split(" ")[1:]) # добавляем дз с 1 слова (/add не учитываем)
    if message.from_user.id == sveta_id:
        await info_writer(result)
        await bot.send_message(message.chat.id, "Дз успешно добавлено в базу")
    elif message.from_user.id == pasha_id:
        await info_writer(result)
        await bot.send_message(message.chat.id, "Дз успешно добавлено в базу")
    elif message.from_user.id == gordey_id:
        await info_writer(result)
        await bot.send_message(message.chat.id, "Дз успешно добавлено в базу")
    elif message.from_user.id == anton_id:
        await info_writer(result)
        await bot.send_message(message.chat.id, "Дз успешно добавлено в базу")
    elif message.from_user.id == sveta2_id:
        await info_writer(result)
        await bot.send_message(message.chat.id, "Дз успешно добавлено в базу")
    else:
        await bot.send_message(message.chat.id, "Вы не можете вносить изменения в базу")


# Просмотр
@dp.message_handler(text='Посмотреть дз')
async def process_show(message: types.Message):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute(f"SELECT dz FROM database")
    data = cur.fetchone()
    if data is None:
        await bot.send_message(message.chat.id, "Дз еще не успели добавить")
    else:
        await bot.send_message(message.chat.id, await send_base())

# Заключение
if __name__ == '__main__':
    create_database()
    executor.start_polling(dp)

