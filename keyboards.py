from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



teacher = InlineKeyboardButton('Загрузить дз')
student = InlineKeyboardButton('Посмотреть дз')
raspisanie = InlineKeyboardButton('Посмотреть расписание')
zvonki = InlineKeyboardButton('Посмотреть звонки')
back = InlineKeyboardButton('Вернуться')
delete = InlineKeyboardButton('Удалить дз')

start_keyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(student, raspisanie, zvonki)
start4adm_keyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(teacher, student, delete, raspisanie, zvonki)

pon = InlineKeyboardButton('Понедельник')
vtor = InlineKeyboardButton('Вторник')
sred = InlineKeyboardButton('Среда')
chet = InlineKeyboardButton('Четверг')
pyat = InlineKeyboardButton('Пятница')

nedelya_keyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(pon, vtor, sred, chet, pyat, back)
otmena_keyboard = ReplyKeyboardMarkup(resize_keyboard= True).add(back)
