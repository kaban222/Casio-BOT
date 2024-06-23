import asyncio
import requests

from aiogram import *
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import random
import time
import datetime
from datetime import timedelta
from datetime import datetime
import threading
from threading import Thread
import math
from operator import itemgetter
from Chat_all import get_chat_members

import projectSettings

if projectSettings.host:
    PROXY_URL = "http://proxy.server:3128"
    bot = Bot(projectSettings.tok, parse_mode="HTML", disable_web_page_preview=True, proxy=PROXY_URL)
    dp = Dispatcher(bot)
else:
    bot = Bot(projectSettings.tok, parse_mode="HTML", disable_web_page_preview=True)
    dp = Dispatcher(bot)

#///////////////////         GAME STTIC
GLAVA = projectSettings.id_vladelec
group_logs = projectSettings.Logs
kurs = projectSettings.kurs
LIMIT = projectSettings.limit
link = ""

#chat_members = await get_chat_members(message.chat.id)
chanel_id = "-1002031836075"
Chat_id = "-1002042398001"

#///////////////////      BD
BD = {}
PF = {}
CHAT = {}
DONAT = {}
BANK = {}
REF = {}
CHAT_USERS = {}
BAN = {}
WORK = {}

chat_link = "https://t.me/CasioWorldl"
chanel_link = "https://t.me/Trychanel_casino"
partner_chat_link = "https://t.me/+YLp4WG_OAhdmOTAy"


#//    GAME Lists
chat_ruletka = {}
List_Of_Time = {}
ruletka_in = {}
Lot = {}
Drive = {}
BlackJack = {}

def load():
    global BD, PF, CHAT, DONAT, BANK, REF, Lot, CHAT_USERS, BAN, WORK
    try:
        f1 = open("BD/Persons.json", "r")
        BD = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #1 \nBD/Persons.json")

    try:
        f1 = open("BD/Performers.json", "r")
        PF = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #2 \nBD/Performers.json")

    try:
        f1 = open("BD/Chats.json", "r")
        CHAT = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #3\nBD/Chats.json")

    try:
        f1 = open("BD/DONAT.json", "r")
        DONAT = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #4\nBD/DONAT.json")

    try:
        f1 = open("BD/BANK.json", "r")
        BANK = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #5\nBD/BANK.json")

    try:
        f1 = open("BD/REFERAL.json", "r")
        REF = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #6\nBD/REFERAL.json")

    try:
        f1 = open("BD/Lotery.json", "r")
        Lot = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #7\nBD/Lotery.json")

    try:
        f1 = open("BD/users_chat.json", "r")
        CHAT_USERS = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #8\nBD/users_chat.json")

    try:
        f1 = open("BD/BAN.json", "r")
        BAN = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #9\nBD/BAN.json")

    try:
        f1 = open("BD/WORK.json", "r")
        WORK = json.load(f1)
        f1.close()
    except:
        print("Ошибка загрузки Файла #10\nBD/WORK.json")

def save():
    global BD
    f1 = open("BD/Persons.json", "w")
    json.dump(BD, f1, ensure_ascii=False)
    f1.close()

def save_PF():
    global PF
    f1 = open("BD/Performers.json", "w")
    json.dump(PF, f1, ensure_ascii=False)
    f1.close()

def save_CHAT():
    global CHAT
    f1 = open("BD/Chats.json", "w")
    json.dump(CHAT, f1, ensure_ascii=False)
    f1.close()

def save_DONAT():
    global DONAT
    f1 = open("BD/DONAT.json", "w")
    json.dump(DONAT, f1, ensure_ascii=False)
    f1.close()

def save_BANK():
    global BANK
    f1 = open("BD/BANK.json", "w")
    json.dump(BANK, f1, ensure_ascii=False)
    f1.close()

def save_REF():
    global REF
    f1 = open("BD/REFERAL.json", "w")
    json.dump(REF, f1, ensure_ascii=False)
    f1.close()

def save_LOT():
    global Lot
    f1 = open("BD/Lotery.json", "w")
    json.dump(Lot, f1, ensure_ascii=False)
    f1.close()

def save_chat_users():
    global CHAT_USERS
    f1 = open("BD/users_chat.json", "w")
    json.dump(CHAT_USERS, f1, ensure_ascii=False)
    f1.close()

def save_Ban():
    global BAN
    f1 = open("BD/BAN.json", "w")
    json.dump(BAN, f1, ensure_ascii=False)
    f1.close()

def save_WORK():
    global WORK
    f1 = open("BD/WORK.json", "w")
    json.dump(WORK, f1, ensure_ascii=False)
    f1.close()

async def registration(kkk):
    global BD
    if kkk not in BD.keys():
        BD[kkk] = {
            "balance":10000,
            "lose":0,
            "win":0,
            "limit": {"much":0, "time":0},
            "take":0,
            "give":0,
            "max_win":0,
            "max_stavka":0,
            "name":"Игрок",
            "admin": False,
        }
        save()
        print(f"Новая регистрация {datetime.now()} \nid:{kkk}")
        await bot.send_message(group_logs, f"Новая регестрация: {datetime.now()} \nid:{kkk}\n\ntg://openmessage?user_id={kkk}")

async def users_in_chat(chat_id, msg):
    global CHAT_USERS
    if chat_id not in CHAT_USERS.keys():
        if msg.chat.type == "private":
            CHAT_USERS[chat_id] = [msg.from_user.id]
            save_chat_users()
        else:
            try:
                chat_members = await get_chat_members(int(chat_id))
                CHAT_USERS[chat_id] = chat_members
                save_chat_users()
            except:
                pass

async def chek_user_in_chat(chat_id, user_id, msg):
    if chat_id not in CHAT_USERS.keys():
        if msg.chat.type == "private":
            CHAT_USERS[chat_id] = [int(user_id)]
        else:
            await users_in_chat(chat_id, msg)
    else:
        if user_id not in CHAT_USERS[chat_id]:
            CHAT_USERS[chat_id].append(int(user_id))

    save_chat_users()

async def chat_registration(chat_id, msg):
    try:
        chat_link = msg.chat.invite_link
    except:
        chat_link = "None"

    if chat_id not in CHAT.keys():
        try:
            chat_link = msg.chat.invite_link
        except:
            chat_link = "None"

        CHAT[chat_id] = {
            "link": chat_link,
            "soo": 0,
            "cmd": 0,
            "max_win": 0,
            'win': 0,
        }
        await bot.send_message(group_logs, f"Регестрация нового чата. ID: {chat_id}")

    if str(CHAT[chat_id]['link']) == "None":
        if str(msg.chat.type) == "private":
            CHAT[chat_id]['link'] = str("tg://openmessage?user_id=" + str(msg.from_user.id))
        else:
            q = await bot.create_chat_invite_link(chat_id=chat_id, name=str(chat_id))
            CHAT[chat_id]['link'] = str(q['invite_link'])

    CHAT[chat_id]['soo'] += 1
    if CHAT[chat_id]['soo'] % 200 == 0:
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("Забрать", callback_data="takeBonus"))
        await bot.send_message(msg.chat.id, f"💸Каждые 200 сообщений в чате приходит магическая кнопка. \n\n💪Успей забрать по ней 10 миллионов!\n\n😎Актуальность: Ещё никто не забрал!", reply_markup=kb)

    save_CHAT()

def Life():
    q = requests.get(link)
    tim = random.randint(30, 50)
    try:
        print(f"\n\n************\nОживительная функция! \n  1.Next: {tim} сек.\n  2.Status: {q.status_code}\n************\n")
    except:
        print(f"Оживительная функция! \n  1.Next: {tim} сек.")

    threading.Timer(tim, Life).start()

#///////////////////        DONAT

async def DepDonat(msg, kol):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    lst_inf = {"1":"2", "2":"4", "3":"6", "4":"8"}
    lst_buy = {"1":1000, "2":1250, "3": 1500, "4":2000}
    if kol not in lst_inf.keys():
        txt_maga = f"{mention}, введите номер покупки:\n" \
                   f"\n" \
                   f"*Из донат магазина\n" \
                   f"1️⃣ Депозит 2% - 1000 spirit🌀\n" \
                   f"2️⃣ Депозит 4% - 1250 spirit🌀\n" \
                   f"3️⃣ Депозит 6% - 1500 spirit🌀\n" \
                   f"4️⃣ Депозит 8% - 2000 spirit🌀\n"
        await bot.send_message(msg.chat.id, txt_maga)
    else:
        if BANK[kkk]['procent'] > int(lst_inf[kol]):
            await bot.send_message(msg.chat.id, f"{mention}, Ваш процент в копилке выше покупаемого.")
        elif BANK[kkk]['procent'] == int(lst_inf[kol]):
            await bot.send_message(msg.chat.id, f"{mention}, Процент в копилке равен покупаемому. Выберите в магазине более высокй процент")
        else:
            if kkk not in DONAT.keys():
                DONAT[kkk]['donat'] = 0

            if DONAT[kkk]['donat'] < lst_buy[kol]:
                await bot.send_message(msg.chat.id, f"{mention}, вам не хватило spirit Coin🌀 :(")
            else:
                BANK[kkk]['procent'] = int(lst_inf[kol])
                DONAT[kkk]['donat'] -= lst_buy[kol]
                save_DONAT()
                save_BANK()
                await bot.send_message(msg.chat.id, f"{mention}, услуга оказана✅ \n"
                                                    f"Теперь проент в копилке: {lst_inf[kol]}")

async def ObmDonat(msg, kol):
    global kurs
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    kol = money(kol, kkk)
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"Введите число!")
    else:
        kol = int(kol['txt'])
        if kkk not in DONAT.keys():
            DONAT[kkk]['donat'] = 0

        if DONAT[kkk]['donat'] < kol:
            await bot.send_message(msg.chat.id, f"{mention}, вам не хватило spirit Coin🌀 :(")
        else:
            DONAT[kkk]['donat'] -= kol
            BD[kkk]['balance'] += kurs * kol
            await bot.send_message(msg.chat.id, f"{mention}, Вы обменяли {kol} spirit Coin🌀. По курсу: {kurs}\n\n🚀Итог: +{kol * kurs}")
        save_DONAT()
        save()
        await bot.send_message(group_logs, f"Обмен доната: tg://openmessage?user_id={kkk}\n\nKOL: {kol}#donat_obmen")


async def send_donat_list(msg):
    global kurs
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("Показать цены", callback_data="DONAT_LIST"))
    txt = f"<b><i>{mention},   ДОНАТНЫЙ МАГАЗИНЧИК </i></b>\n" \
          f"\n" \
          f"💸 Обмен: 1spirit🌀 = {kurs} Монеткам🪙 \n" \
          f"🪙Обмен Spirit: Обменять (Количество)\n" \
          f"\n" \
          f"🏆<b><i> Привилегии:</i></b>\n" \
          f" 1️⃣ GOLD VIP[100 000]🌀\n" \
          f" 2️⃣ DIMOND VIP[300 000]🌀\n" \
          f"\n" \
          f"🔝Покупка: /buyvip\n" \
          f"\n" \
          f"⚡<b><i>Буст Копилки:</i></b>\n" \
          f"  1️⃣ Депозит 2% - 1000 spirit🌀\n" \
          f"  2️⃣ Депозит 4% - 1250 spirit🌀\n" \
          f"  3️⃣ Депозит 6% - 1500 spirit🌀\n" \
          f"  4️⃣ Депозит 8% - 2000 spirit🌀\n" \
          f"\n" \
          f"🔝️Покупка: !Депозит (номер)\n" \
          f"\n" \
          f"🎈<b><i>промокоды</i></b>\n" \
          f"  <i>Особенность: активация за подписку на ваш канал</i>\n" \
          f"\n" \
          f"<b>🔝Подробнее</b> - /promokod\n" \
          f"\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"<b><i>Донат Осуществляется:</i></b>\n" \
          f"👤По донату можно обратиться к Владельцам:\n" \
          f"<b>[1]</b> @Trykaban (Рубли)\n" \
          f"<b>[2]</b> @Ttypok (др. валюта)\n" \
          f"\n" \
          f"Ссылка на оплату рублями(@Trykaban):\n " \
          f"https://yoomoney.ru/to/4100118520230407\n" \
          f""
    await bot.send_message(msg.chat.id, txt, reply_markup=kb)


async def donat_buy(chat_id, kol, buyer, admin):
    global DONAT
    if buyer not in DONAT.keys():
        DONAT[buyer] = {
            "donat": 0
        }
    try:
        kol = int(kol)
        DONAT[buyer]['donat'] += kol
        save_DONAT()
        try:
            mention = "<a href='tg://user?id=" + buyer + "'>" + BD[buyer]['name'] + "</>"
            await bot.send_message(buyer, f"Вам выдано {kol} донат коинов. Администратором {admin}")
            await bot.send_message(chat_id, f"Пользователь с id{buyer} получил уведомление о выдачи доната в размере {kol} донат монеток \n\nего аккаунт - {mention}")
        except:
            mention = "<a href='tg://user?id=" + buyer + "'>" + BD[buyer]['name'] + "</>"
            await bot.send_message(chat_id, f"У пользователя с id{buyer} нету личных сообщений. Ему небыло дотавлено уведомление о успешной покупке {kol} донат монеток \n\nему можно сообщить - {mention}")
        await bot.send_message(group_logs, f"Выдан донат: {datetime.now()}\nADMIN: {admin}\nuser: {buyer}\nKOL: {kol}")
    except:
        await bot.send_message(chat_id, f"введите число!")

#MINI GAMES
async def Gol_fun(kol, msg):
    user_id = str(msg.from_user.id)
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if kol < 1000:
            await bot.send_message(msg.chat.id, "Ставка должна быть больше 1000 монет")
        elif kol > BD[user_id]['balance']:
            await bot.send_message(msg.chat.id, f"{mention}, у вас не достаточно монет на балансе")
        else:
            data = await bot.send_dice(msg.chat.id, emoji='⚽')
            if int(data.dice.value) > 2:
                await bot.send_message(msg.chat.id, f"{mention}, ⚽Мяч попал в ворота! Коэффициент x2")
                BD[user_id]['balance'] += kol
                BD[user_id]['win'] += kol
                if BD[user_id]['max_win'] < kol*2:
                    BD[user_id]['max_win'] = kol*2
            else:
                await bot.send_message(msg.chat.id, f"{mention}, ⚽Мяч не попал в ворота. В следующий раз точно повезёт!")
                BD[user_id]['balance'] -= kol
                BD[user_id]['lose'] += kol

            if BD[user_id]['max_stavka'] < kol:
                BD[user_id]['max_stavka'] = kol
            save()

async def Bal_fun(kol, msg):
    user_id = str(msg.from_user.id)
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if kol < 1000:
            await bot.send_message(msg.chat.id, "Ставка должна быть больше 1000 монет")
        elif kol > BD[user_id]['balance']:
            await bot.send_message(msg.chat.id, f"{mention}, у вас не достаточно монет на балансе")
        else:
            data = await bot.send_dice(msg.chat.id, emoji='🏀')
            if int(data.dice.value) > 3:
                await bot.send_message(msg.chat.id, f"{mention}, 🏀Мяч попал в кольцо! Коэффициент x2")
                BD[user_id]['balance'] += kol
                BD[user_id]['win'] += kol
                if BD[user_id]['max_win'] < kol*2:
                    BD[user_id]['max_win'] = kol*2
            else:
                await bot.send_message(msg.chat.id, f"{mention}, 🏀Мяч не попал в кольцо. В следующий раз точно повезёт!")
                BD[user_id]['balance'] -= kol
                BD[user_id]['lose'] += kol

            if BD[user_id]['max_stavka'] < kol:
                BD[user_id]['max_stavka'] = kol
            save()

async def Boul_fun(kol, msg):
    user_id = str(msg.from_user.id)
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if kol < 1000:
            await bot.send_message(msg.chat.id, "Ставка должна быть больше 1000 монет")
        elif kol > BD[user_id]['balance']:
            await bot.send_message(msg.chat.id, f"{mention}, у вас не достаточно монет на балансе")
        else:
            data = await bot.send_dice(msg.chat.id, emoji='🎳')
            if int(data.dice.value) == 6:
                await bot.send_message(msg.chat.id, f"{mention}, 🎳Страйк! Коэффициент x2")
                BD[user_id]['balance'] += kol
                BD[user_id]['win'] += kol
                if BD[user_id]['max_win'] < kol*2:
                    BD[user_id]['max_win'] = kol*2
            else:
                await bot.send_message(msg.chat.id, f"{mention}, 🎳практически! В следующий раз точно повезёт! Коэффициент -x0.5")
                BD[user_id]['balance'] -= kol/2
                BD[user_id]['lose'] += kol/2

            if BD[user_id]['max_stavka'] < kol:
                BD[user_id]['max_stavka'] = kol
            save()

async def Darts_fun(kol, msg):
    user_id = str(msg.from_user.id)
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if kol < 1000:
            await bot.send_message(msg.chat.id, "Ставка должна быть больше 1000 монет")
        elif kol > BD[user_id]['balance']:
            await bot.send_message(msg.chat.id, f"{mention}, у вас не достаточно монет на балансе")
        else:
            data = await bot.send_dice(msg.chat.id, emoji='🎯')
            if int(data.dice.value) == 6:
                await bot.send_message(msg.chat.id, f"{mention}, 🎯5 из 5! Коэффициент x2")
                BD[user_id]['balance'] += kol
                BD[user_id]['win'] += kol
                if BD[user_id]['max_win'] < kol*2:
                    BD[user_id]['max_win'] = kol*2
            else:
                await bot.send_message(msg.chat.id, f"{mention}, 🎯практически! В следующий раз точно повезёт! Коэффициент -x0.5")
                BD[user_id]['balance'] -= kol/2
                BD[user_id]['lose'] += kol/2

            if BD[user_id]['max_stavka'] < kol:
                BD[user_id]['max_stavka'] = kol
            save()

async def Spin_fun(kol, msg):
    user_id = str(msg.from_user.id)
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if kol < 1000:
            await bot.send_message(msg.chat.id, "Ставка должна быть больше 1000 монет")
        elif kol > BD[user_id]['balance']:
            await bot.send_message(msg.chat.id, f"{mention}, у вас не достаточно монет на балансе")
        else:
            data = await bot.send_dice(msg.chat.id, emoji='🎰')
            rez = projectSettings.get_combo_text(data.dice.value)
            l = {rez[0]:"1", rez[1]:"2", rez[2]:"3"}
            t = ""
            for i in rez:
                t += l[i]
            kolichestvo = {}
            for i in t:
                if i not in kolichestvo.keys():
                    kolichestvo[i] = 0
                kolichestvo[i] += 1
            max = 0
            for i, y in kolichestvo.items():
                if y > max:
                    max = y

            if max == 3:
                await bot.send_message(msg.chat.id, f"{mention}, 🎰Джекпот! Коэффициент x3")
                BD[user_id]['balance'] += kol*2
                BD[user_id]['win'] += kol*3
                if BD[user_id]['max_win'] < kol*3:
                    BD[user_id]['max_win'] = kol*3
            elif max == 2:
                await bot.send_message(msg.chat.id, f"{mention}, 🎰2 из 3! Коэффициент x2")
                BD[user_id]['balance'] += kol
                BD[user_id]['win'] += kol
                if BD[user_id]['max_win'] < kol*2:
                    BD[user_id]['max_win'] = kol*2
            else:
                await bot.send_message(msg.chat.id, f"{mention}, 🎰В следующий раз повезёт!")
                BD[user_id]['balance'] -= kol
                BD[user_id]['lose'] += kol

            if BD[user_id]['max_stavka'] < kol:
                BD[user_id]['max_stavka'] = kol
            save()


##///////////////////         GAME

def color_make(num):
    if str(num) in ["1","3","5","7","9","11"]:
        return {"color":"🔴", "name":"красный"}
    elif str(num) in ["2","4","6","8","10","12"]:
        return {"color":"⚫️", "name":"чёрный"}
    elif str(num) in ["0"]:
        return {"color":"💚", "name":"зелёный"}

def money(kol, kkk):
    kol = str(kol)
    if kol[-1][-1] == "%":
        try:
            _kol = ""
            for i in kol:
                if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "%"]:
                    if i != "%":
                        _kol += i
                else:
                    return {"txt":"Не известное число", "type":"error"}

            kol = _kol
            procent = int(kol)
            all = BD[kkk]['balance']
            money = int((all / 100) * procent)
            return {"txt":money, "type":"ok"}
        except:
            return {"txt":"Введите число в процентах от 1 до 100%", "type":"error"}
    else:
        money = ""
        numers = 1
        for i in kol:
            if i in ["m","M","М","м"]:
                money += "000000"
            elif i in ["k","K","к","К"]:
                money += "000"
            elif i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                money += i
            else:
                return {"txt":f"Неизвестный символ [{i}]. Позиция {numers}", "type":"error"}
            numers += 1

        return {"txt":money, "type":"ok"}

def money_form(mon):
    mon = str(mon)
    idd = -1
    ctr = 1
    rez = ""
    for i in range(len(mon)):
        if ctr == 4:
            ctr = 1
            rez += " "
        rez += mon[idd]
        ctr += 1
        idd -= 1

    rez = rez[::-1]
    return rez

async def All_chats(chat_id):
    D_list = {}
    for i, y in CHAT.items():
        D_list[i] = y['win']

    sorted_tuple = dict(sorted(D_list.items(), key=itemgetter(1)))
    sorted_tuple = dict(reversed(sorted_tuple.items()))

    idd = 1
    txt = ""
    for i, y in sorted_tuple.items():
        if i == "-4181636704":
            pass
        else:
            txt += f"{idd}. ID{i} - {money_form(y)}\n" \
                   f"  max_win: {CHAT[i]['max_win']} \n" \
                   f"  soo: {CHAT[i]['soo']}\n" \
                   f"  cmd: {CHAT[i]['cmd']}\n" \
                   f"  Link: {CHAT[i]['link']}\n"
            idd += 1
            if idd >= 16:
                break

    txt = f"Всего чатов: {len(sorted_tuple)-1}\n" + txt + "\n\n!chat (num) -- детальная информация о чате"
    await bot.send_message(chat_id, txt)

async def chek_vip(msg):
    kkk = str(msg.from_user.id)
    if kkk not in DONAT.keys():
        pass
    elif 'vip' not in DONAT[kkk].keys():
        pass
    else:
        if DONAT[kkk]['vip']['act']:
            date_last_farm = datetime.strptime(str(DONAT[kkk]['vip']["date"]), "%Y-%m-%d %H:%M:%S")
            date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
            tm = date2 - date_last_farm
            tm2 = int(tm.total_seconds() // 60)
            if tm2 * 60 >= 10:
                mention = "<a href='tg://user?id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
                DONAT[kkk]['vip']['act'] = False
                save_DONAT()
                await bot.send_message(msg.chat.id, f"{mention}, у вас закончился вип статус :(")
async def vip_watch(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if kkk not in DONAT.keys():
        await bot.send_message(msg.chat.id, f"{mention}, У вас нету ВИП статуса :(")
    elif 'vip' not in DONAT[kkk].keys():
        await bot.send_message(msg.chat.id, f"{mention}, У вас нету ВИП статуса :(")
    else:
        if DONAT[kkk]['vip']['act']:
            if DONAT[kkk]['vip']['vp'] == 1:
                status = "GOLD VIP"
            elif DONAT[kkk]['vip']['vp'] == 2:
                status = "DIMOND VIP"
            await bot.send_message(msg.chat.id, f"{mention}, Вы владеете {status}. \n\nДействует до: {DONAT[kkk]['vip']['date']}")
        else:
            await bot.send_message(msg.chat.id, f"{mention}, У вас нету ВИП статуса :(")
async def Top_List(chat_id, user_id, msg):
    global CHAT_USERS
    D_list = {}
    if msg.chat.type == "private":
        for i, y in BD.items():
            D_list[i] = y['balance']
        txt1 = f"🔝 Топ игроков по монетам в боте.\n👑 Всего в боте: {len(BD)}\n\n"
    else:
        await users_in_chat(chat_id, msg)
        await chek_user_in_chat(chat_id, user_id, msg)
        if chat_id not in CHAT_USERS.keys():
            await bot.send_message(chat_id, f"Из-за правил работы телеграм, мы не смогли отделить ваш чат от всех в боте. ЭТО ВРЕМЕННО, НУЖНО НЕМНОГО ПОДОЖДАТЬ!")
            for i, y in BD.items():
                D_list[i] = y['balance']
            txt1 = f"🔝 Топ игроков по монетам в боте.\n👑 Всего в боте: {len(BD)}\n\n"
        else:
            chat_members = CHAT_USERS[chat_id]
            for i in chat_members:
                await registration(str(i))
                D_list[str(i)] = BD[str(i)]['balance']
                txt1 = f"🔝 Топ игроков по монетам в чате.\n👑 Всего в чате: {len(chat_members)}\n\n"

    sorted_tuple = dict(sorted(D_list.items(), key=itemgetter(1)))
    sorted_tuple = dict(reversed(sorted_tuple.items()))

    idd = 1
    txt = ""
    tp = ""
    for i, y in sorted_tuple.items():
        mention = "<a href='tg://user?id=" + i + "'>" + BD[i]['name'] + "</>"
        if idd == 1:
            txt += f"① {mention} - {money_form(y)} \n"
        if idd == 2:
            txt += f"② {mention} - {money_form(y)} \n"
        if idd == 3:
            txt += f"③ {mention} - {money_form(y)} \n"
        if idd == 4:
            txt += f"④ {mention} - {money_form(y)} \n"
        if idd == 5:
            txt += f"⑤ {mention} - {money_form(y)} \n"
        if idd == 6:
            txt += f"⑥ {mention} - {money_form(y)} \n"
        if idd == 7:
            txt += f"⑦ {mention} - {money_form(y)} \n"
        if idd == 8:
            txt += f"⑧ {mention} - {money_form(y)} \n"
        if idd == 9:
            txt += f"⑨ {mention} - {money_form(y)} \n"
        if idd == 10:
            txt += f"⑩ {mention} - {money_form(y)}"
        if user_id == i:
            txt_num = ""
            for i in str(idd):
                if i == "1":
                    txt_num += "①"
                if i == "2":
                    txt_num += "②"
                if i == "3":
                    txt_num += "③"
                if i == "4":
                    txt_num += "④"
                if i == "5":
                    txt_num += "⑤"
                if i == "6":
                    txt_num += "⑥"
                if i == "7":
                    txt_num += "⑦"
                if i == "8":
                    txt_num += "⑧"
                if i == "9":
                    txt_num += "⑨"
                if i == "0":
                    txt_num += "⓪"
            tp = f"\n\n{txt_num} {mention} - {money_form(y)}"
            if idd > 12:
                break
        idd += 1
        if idd >= 15 and tp != "":
            break
    txt1 += txt
    txt1 = txt1 + "\n➖➖➖➖➖➖➖➖" + tp
    await bot.send_message(chat_id, txt1)

async def bank_deposit_time(user_id, date, status):
    date_last_farm = datetime.strptime(str(BANK[user_id]['time']), "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    tm = date2 - date_last_farm
    tm2 = int(tm.total_seconds())
    mint = tm2 // 60
    if status in [2]:
        deltaTime = 12
    else:
        deltaTime = 24

    if int((mint // 60) // deltaTime) > 0:
        BAL = BANK[user_id]['deposit']
        PROC = BANK[user_id]['procent']

        for i in range(int((mint // 60) // 24)):
            BAL = int(BAL + int((BAL/100) * PROC))

        BANK[user_id]['deposit'] = BAL
        BANK[user_id]['time'] = date
        save_BANK()

async def limit_off(msg):
    user_id = str(msg.reply_to_message.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + str(msg.from_user.id) + "'>" + BD[str(msg.from_user.id)]['name'] + "</>"
    await registration(user_id)
    await asyncio.sleep(1)
    BD[user_id]['limit']['much'] = 0
    save()
    await bot.send_message(msg.chat.id, f"{mention}, вы онулировали лимит. ID: {user_id}")
    await bot.send_message(group_logs, f"{mention} онулировал ЛИМИТ, ID{user_id}")

async def bank_take(chat_id, user_id, kol, date):
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(chat_id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if user_id not in BANK.keys():
            BANK[user_id] = {
                "bank": 0,
                "deposit": 0,
                "chek_deposit": 0,
                "time": date,
                "procent": 1,
            }

        if BD[user_id]['balance'] < kol:
            await bot.send_message(chat_id, f"{mention}, У вас недостаточно монет.")
        else:
            BANK[user_id]['bank'] += kol
            BD[user_id]['balance'] -= kol
            save_BANK()
            save()
            await bot.send_message(chat_id, f"{mention}, в копилку положено {kol} \n\nКоманда просмотра - моя копилка")

async def chat_send(msg):
    chat_id = str(msg.chat.id)
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    txt_chat_inf = f"{mention}, Информация по чату: \n\nID: {chat_id}\nсообщений: {CHAT[chat_id]['msg']}\nмаксимальная ставка: {CHAT[chat_id]['max_stavka']}"
async def bank_give(chat_id, user_id, kol, date):
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(chat_id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if user_id not in BANK.keys():
            BANK[user_id] = {
                "bank": 0,
                "deposit": 0,
                "chek_deposit": 0,
                "time": date,
                "procent": 1,
            }

        if BANK[user_id]['bank'] < kol:
            await bot.send_message(chat_id, f"{mention}, в копилке нету такой суммы")
        else:
            BANK[user_id]['bank'] -= kol
            BD[user_id]['balance'] += kol
            save_BANK()
            save()
            await bot.send_message(chat_id, f"{mention}, вы взяли из копилки {kol} \n\nКоманда просмотра - моя копилка")

async def deposit_give(chat_id, user_id, kol, date, status):
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(chat_id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if user_id not in BANK.keys():
            BANK[user_id] = {
                "bank": 0,
                "deposit": 0,
                "chek_deposit": 0,
                "time": date,
                "procent": 1,
            }
        await bank_deposit_time(user_id, date, status)
        if BANK[user_id]['deposit'] < kol:
            await bot.send_message(chat_id, f"{mention}, на депозите нету такой суммы")
        else:
            BANK[user_id]['deposit'] -= kol
            BANK[user_id]['time'] = date
            BD[user_id]['balance'] += kol

            save_BANK()
            save()
            await bot.send_message(chat_id, f"{mention}, вы взяли из депозита {kol} \n\nКоманда просмотра - моя копилка")

async def deposit_take(chat_id, user_id, kol, date, status):
    kol = money(kol, user_id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if kol['type'] == "error":
        await bot.send_message(chat_id, f"{mention}, введите число")
    elif kol['type'] == "ok":
        kol = int(kol['txt'])
        if user_id not in BANK.keys():
            BANK[user_id] = {
                "bank": 0,
                "deposit": 0,
                "chek_deposit": 0,
                "time": date,
                "procent": 1,
            }
        await bank_deposit_time(user_id, date, status)
        if BD[user_id]['balance'] < kol:
            await bot.send_message(chat_id, f"{mention}, У вас нету такой суммы")
        else:
            BANK[user_id]['deposit'] += kol
            BANK[user_id]['time'] = date
            BD[user_id]['balance'] -= kol

            save_BANK()
            save()
            await bot.send_message(chat_id, f"{mention}, положили на депозит {kol} \n\nКоманда просмотра - моя копилка")

async def Lecenka(chat_id, user_id, kol):
    bt = InlineKeyboardMarkup()
    tr = True
    kol = money(kol, user_id)
    if kol['type'] == "error":
        await bot.send_message(chat_id, f"Введите число!")
    else:
        kol = int(kol['txt'])
        for i in range(5):
            i += 1
            if tr:
                if random.randint(1, 100) > 50:
                    bt.add(InlineKeyboardButton(f"{i}", callback_data=f"Lec_{user_id}:0:0:{kol}"))
                else:
                    bt.add(InlineKeyboardButton(f"{i}", callback_data=f"Lec_{user_id}:1:0:{kol}"))
                    tr = False
            else:
                bt.add(InlineKeyboardButton(f"{i}", callback_data=f"Lec_{user_id}:0:0:{kol}"))

        bt.add(InlineKeyboardButton("Остановиться", callback_data=f"LecS_{user_id}:1:0:{kol}"))
        await bot.send_message(chat_id, "Вы взбираетесь на гору!\n Коэффициент:0 \n\nВам нужно выбрать верную леcенку", reply_markup=bt)

async def play_rulet(chat_id, txt, user_id, stavka):
    global chat_ruletka
    L1 = txt.split(" ")
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if len(L1) > 1 and L1[1] in ["k", "K", "К", "к", "Ч", "ч", "З", "з"]:

        if user_id not in chat_ruletka[chat_id]['stavki'].keys():
            chat_ruletka[chat_id]['stavki'][user_id] = {"nm":[], "cl":[]}

        if int(stavka['txt']) > BD[user_id]['balance']:
            await bot.send_message(int(chat_id), f"{mention}, у вас не достаточно монет")
        elif int(stavka['txt']) < 1000:
            await bot.send_message(int(chat_id), f"{mention}, минимальная ставка 1000")
        else:
            if L1[1] in ["k", "K", "К", "к"]:
                pov = "к"
            elif L1[1] in ["Ч", "ч"]:
                pov = "ч"
            elif L1[1] in ["З", "з"]:
                pov = "з"
            again = False
            for i in chat_ruletka[chat_id]['stavki'][user_id]['cl']:
                if i['gm1'] == True:
                    again = True
            for i in chat_ruletka[chat_id]['stavki'][user_id]['nm']:
                if i['gm2'] == True:
                    again = True
            chat_ruletka[chat_id]['stavki'][user_id]['cl'].append({"color": pov, "gm1": True, "stavka_color": stavka['txt']})
            if again:
                await bot.send_message(chat_id, f"{mention}, дополнил ставку {stavka['txt']} на {pov}")
            else:
                await bot.send_message(chat_id, f"{mention}, вы поставили {stavka['txt']} на {pov}")
            chek_stavki(chat_id, user_id)
            BD[user_id]['balance'] -= int(stavka['txt'])
            save()

    else:
        rule = True
        Comes = []
        summ = 0
        for i in L1[1::]:
            if i not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "0"]:
                rule = False
                break
            else:
                Comes.append(i)
                summ += int(stavka['txt'])

        if int(stavka['txt']) < 1000 and rule:
            await bot.send_message(int(chat_id), f"{mention}, минимальная ставка 1000")
        elif rule:
            if BD[user_id]['balance'] < summ:
                await bot.send_message(chat_id, f"{mention}, у вас не достаточно монет")
            else:
                if user_id not in chat_ruletka[chat_id]['stavki'].keys():
                    chat_ruletka[chat_id]['stavki'][user_id] = {"nm":[], "cl":[]}

                chat_ruletka[chat_id]['stavki'][user_id]['nm'].append({"nums": Comes, "gm2": True, "stavka_num": stavka['txt']})
                again = False
                for i in chat_ruletka[chat_id]['stavki'][user_id]['cl']:
                    if i['gm1'] == True:
                        again = True
                for i in chat_ruletka[chat_id]['stavki'][user_id]['nm']:
                    if i['gm2'] == True:
                        again = True
                if again:
                    txt_upload = f"{mention}, Дополнил ставку: {stavka['txt']} на\n"
                else:
                    txt_upload = f"{mention}, вы поставили {stavka['txt']} на\n"
                for i in Comes:
                    txt_upload += f"  {color_make(i)['color']}{i}\n"
                await bot.send_message(chat_id, txt_upload)
                chek_stavki(chat_id, user_id)
                BD[user_id]['balance'] -= int(summ)
                save()

def chek_stavki(chat_id, user_id):
    idd = 0
    for i in chat_ruletka[str(chat_id)]['stavki'][user_id]['cl']:
        if i['gm1'] == False:
            del chat_ruletka[str(chat_id)]['stavki'][user_id]['cl'][idd]
        idd += 1
    idd = 0
    for i in chat_ruletka[str(chat_id)]['stavki'][user_id]['nm']:
        if i['gm2'] == False:
            del chat_ruletka[str(chat_id)]['stavki'][user_id]['nm'][idd]
        idd += 1

async def pillow(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if BD[kkk]['balance'] < 25000:
        await bot.send_message(msg.chat.id, f"{mention}, Сработала падушка безопастноси! У вас на балансе оставалось: {BD[kkk]['balance']}. \n\n+75 000. [DIMOND VIP]")
        BD[kkk]['balance'] += 75000
        save()

async def ewery_day_gold(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if DONAT[kkk]['vip']['bns'] != str(datetime.now().day):
        await bot.send_message(msg.chat.id, f"{mention}, ЕЖЕДНЕВНЫЙ БОНУС [GOLD VIP] +300 000")
        DONAT[kkk]['vip']['bns'] = str(datetime.now().day)
        save_DONAT()
        BD[kkk]['balance'] += 300000
        save()

async def ewery_day_dimond(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if DONAT[kkk]['vip']['bns'] != str(datetime.now().day):
        await bot.send_message(msg.chat.id, f"{mention}, ЕЖЕДНЕВНЫЙ БОНУС [DIMOND VIP] +1 000 000")
        DONAT[kkk]['vip']['bns'] = str(datetime.now().day)
        save_DONAT()
        BD[kkk]['balance'] += 1000000
        save()

async def vip_send(msg):
    user_id = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if user_id not in DONAT.keys():
        donat_kol = 0
    else:
        donat_kol = DONAT[user_id]['donat']
    txt = f"{mention}, <b>МАГАЗИН СТАТУСОВ</b>\n" \
          f"\n" \
          f"🌀Ваш донатный баланс: {donat_kol}\n" \
          f"" \
          f"<b>VIP GOLD</b>\n" \
          f"  <b>[1]</b> +10% на команды заработка\n" \
          f"  <b>[2]</b> Ежедневнй доход(300к)\n" \
          f"<b>💸Стоимость: 🌀100к (100.000)</b>\n" \
          f"<b>🛒Купить: Кнопка(GOLD VIP| 100k)</b>\n" \
          f"\n" \
          f"<b>VIP DIMOND</b>\n" \
          f"  <b>[1]</b> +20% на команды заработка\n" \
          f"  <b>[2]</b> Ежедневнй доход(1кк)\n " \
          f" <b>[3]</b> Активная падушка безопатности /pillow\n" \
          f"  <b>[4]</b> депозитный рост 24ч -> 12ч\n" \
          f"<b>💸Стоимость: 🌀300к (300.000)</b>\n" \
          f"<b>🛒Купить: Кнопка(DIMOND VIP| 300k)</b>\n" \
          f"\n" \
          f"❗️<b>Вип статус покупается на 2 недели!</b>"
    kb = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("GOLD VIP| 100k", callback_data="buygold")
    b2 = InlineKeyboardButton("DIMOND VIP| 300k", callback_data="buydimond")
    kb.add(b1)
    kb.add(b2)
    await bot.send_message(msg.chat.id, txt, reply_markup=kb)

async def start_rulet(chat_id):
    global chat_ruletka, ruletka_in, CHAT
    soo = await bot.send_message(chat_id, "Рудетка запущена! У вас 15 сек...")
    await asyncio.sleep(5)

    await bot.edit_message_text("Рудетка запущена! У вас 10 сек...", chat_id, soo.message_id)
    await asyncio.sleep(5)

    await bot.edit_message_text("Рудетка запущена! У вас 5 сек...", chat_id, soo.message_id)
    await asyncio.sleep(5)

    await bot.edit_message_text("Результаты рулетки ниже!", chat_id, soo.message_id)

    color_Upset = {"чёрный":"ч", "красный":"к", "зелёный":"з"}
    rand_num = random.randint(0, 12)
    colors = color_make(rand_num)
    t_end = "\n\n"
    t_start = f"Выпало число {rand_num}{colors['color']} \n\n"
    Perfect_color = color_Upset[colors['name']]
    chat_ruletka[chat_id]['log'].append(f"{colors['color']}{rand_num}")
    if len(chat_ruletka[chat_id]['log']) >= 21:
        chat_ruletka[chat_id]['log'].pop(0)

    for i, y in chat_ruletka[chat_id]['stavki'].items():
        mention = "<a href='tg://openmessage?user_id=" + i + "'>" + BD[i]['name'] + "</>"
        idd = 0
        for _i in y['cl']:
            if _i['color'] == Perfect_color and _i['gm1']:
                t_end += f"{mention}, выыйграл {int(_i['stavka_color'])} \n"
                t_start += f"{mention}, поставил {_i['stavka_color']} на {_i['color']} \n"
                BD[i]['balance'] += int(_i['stavka_color']) * 2
                if BD[i]['max_win'] < int(_i['stavka_color']):
                    BD[i]['max_win'] = int(_i['stavka_color'])
                if CHAT[chat_id]['max_win'] < int(_i['stavka_color']):
                    CHAT[chat_id]['max_win'] = int(_i['stavka_color'])
            elif rand_num == 0  and _i['gm1']:
                t_end += f"{mention}, возвращено {int(_i['stavka_color'])/2} \n"
                BD[i]['balance'] += int(_i['stavka_color'])/2
                BD[i]['lose'] += int(_i['stavka_color'])/2
            elif _i['color'] != Perfect_color  and _i['gm1']:
                t_start += f"{mention}, поставил {_i['stavka_color']} на {_i['color']} \n"
                #BD[i]['balance'] -= int(_i['stavka_color'])
                BD[i]['lose'] += int(_i['stavka_color'])
            if BD[i]['max_stavka'] < int(_i['stavka_color']) and _i['gm1']:
                BD[i]['max_stavka'] = int(_i['stavka_color'])

            save()
            save_CHAT()
            chat_ruletka[chat_id]['stavki'][i]['cl'][idd]['gm1'] = False
            idd += 1
        idd = 0
        for _x in y['nm']:
            for _i in _x['nums']:
                if _i == str(rand_num) and _x['gm2']:
                    t_end += f"{mention}, выыйграл {int(_x['stavka_num'])*11} \n"
                    t_start += f"{mention}, поставил {_x['stavka_num']} на {_i} \n"
                    BD[i]['balance'] += int(_x['stavka_num'])*12
                    if BD[i]['max_win'] < int(_x['stavka_num'])*12:
                        BD[i]['max_win'] = int(_x['stavka_num'])*12
                    if CHAT[chat_id]['max_win'] < int(_x['stavka_num'])*12:
                        CHAT[chat_id]['max_win'] = int(_x['stavka_num'])*12
                    BD[i]['win'] += int(_x['stavka_num'])*12
                    CHAT[chat_id]['win'] += int(_x['stavka_num'])*12
                else:
                    if _x['gm2']:
                        t_start += f"{mention}, поставил {_x['stavka_num']} на {_i} \n"
                        #BD[i]['balance'] -= int(_x['stavka_num'])
                        BD[i]['lose'] += int(_x['stavka_num'])

                if BD[i]['max_stavka'] < int(_x['stavka_num']) and _x['gm2']:
                    BD[i]['max_stavka'] = int(_x['stavka_num'])

                save_CHAT()
                save()
            chat_ruletka[chat_id]['stavki'][i]['nm'][idd]['gm2'] = False
            idd += 1
    ruletka_in[str(chat_id)] = False
    await bot.send_message(chat_id, t_start + t_end, reply_to_message_id=soo.message_id)

async def start_blackJ(msg, kol):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    kol = money(kol, kkk)
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"{mention}, ставку")
    else:
        if int(kol['txt']) > BD[kkk]['balance']:
            await bot.send_message(msg.chat.id, f"{mention}, У вас недостаточно монет для такой ставки")
        elif int(kol['txt']) < 1000:
            await bot.send_message(msg.chat.id, f"{mention}, Минимальная ставка 1000")
        else:
            if msg.chat.type != "private":
                await bot.send_message(msg.chat.id, f"{mention}, Игать в эту игру удобнее в личных сообщениях. Можно начать тут и продолжить в любом чате! Всё к вашему удобству!")

            BD[kkk]['balance'] -= int(kol['txt'])
            save()

            await bot.send_message(msg.chat.id, f"{mention}, Игра началась! Ставка: {kol['txt']} \nВаш id(игры): {kkk}\nКарты могут повторятся!\n\n21 очко - множитель X3\nПроиграете - потеряете всё")
            BlackJack[kkk] = {"stavka": int(kol['txt']), "user": 0, "diller":0}
            t = random.randint(2, 10) + random.randint(2, 10)
            BlackJack[kkk]['user'] += t
            BlackJack[kkk]['diller'] += random.randint(2, 10) + random.randint(2, 10)
            kb = InlineKeyboardMarkup()
            kb.add(InlineKeyboardButton("🤑Удвоить", callback_data=f"BJDBL_{kkk}"))
            kb.add(InlineKeyboardButton("😎Взять", callback_data=f"BJTK_{kkk}"))
            kb.add(InlineKeyboardButton("👌Хватит", callback_data=f"BJSTP_{kkk}"))
            await bot.send_message(msg.chat.id, f"👤{mention}, Диллер выдал по две карты. Ваши очки: {t}. \n\n👾Выберите следующие действия:", reply_markup=kb)

async def start_drivars(msg):
    user_id = str(msg.from_user.id)
    chat_id = str(msg.chat.id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if chat_id in Drive.keys():
        await bot.send_message(msg.chat.id, f"{mention}, гонка уже идёт!")
    else:
        Drive[chat_id] = {"start":str(msg.date), "stavki":{}, "max":0}
        soo = await bot.send_message(msg.chat.id, f"Гонка началась!\n"
                                            f"   🚗  | м1 1%\n"
                                            f"   🚕  | м2 1%\n"
                                            f"   🚙  | м3 1%\n"
                                            f"   🚓  | м4 1%\n"
                                            f"   🏎  | м5 1%\n")
        winers = []
        lst_rn = {"1": 0, "2":0, "3":0, "4": 0, "5":0}
        lst = {"1":"🚗", "2":"🚕", "3":"🚙", "4":"🚓", "5":"🏎"}
        await asyncio.sleep(10)
        while True:
            stop_chek = False
            for i in range(5):
                i += 1
                lst_rn[str(i)] += random.randint(0, 15)
                if lst_rn[str(i)] > Drive[chat_id]['max']:
                    Drive[chat_id]['max'] = lst_rn[str(i)]

            for i in range(5):
                i += 1
                if lst_rn[str(i)] >= 100:
                    winers.append(str(i))
                    stop_chek = True
            if stop_chek:
                break
            if random.randint(0, 100) > 65:
                txt_cars = f"Гонка идёт!\n"\
                            f"   🚗  | м1 {lst_rn['1']}%\n"\
                            f"   🚕  | м2 {lst_rn['2']}%\n"\
                            f"   🚙  | м3 {lst_rn['3']}%\n"\
                            f"   🚓  | м4 {lst_rn['4']}%\n"\
                            f"   🏎  | м5 {lst_rn['5']}%\n"
                soo = await bot.edit_message_text(txt_cars, msg.chat.id, soo.message_id)
            await asyncio.sleep(8)

        proigral = ""
        wigral = ""
        txt = f"Результат гонки:\n" \
              f"\n\n"
        for i in winers:
            txt += f"Добралась до финиша машина {lst[str(i)]}\n"
        txt += "\n"
        for i, y in Drive[chat_id]['stavki'].items():
            mention = "<a href='tg://openmessage?user_id=" + i + "'>" + BD[i]['name'] + "</>"
            for _i in y:
                if str(_i['num']) in winers:
                    wigral += f"{mention}, выиграл(а) {int(_i['kol'])*2}💵 {lst[_i['num']]}\n"
                    BD[i]['balance'] += int(_i['kol'])*2
                else:
                    proigral += f"{mention}, проиграл(а) {_i['kol']}💵 {lst[_i['num']]}\n"
                save()
        txt += proigral
        txt += "\n"
        txt += wigral
        await bot.send_message(msg.chat.id, txt)
        del Drive[chat_id]

async def drive_make_stavka(msg, L1):
    user_id = str(msg.from_user.id)
    chat_id = str(msg.chat.id)
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if chat_id not in Drive.keys():
        await bot.send_message(msg.chat.id, f"{mention}, сначала начните гонку! \nКоманда: !Гонка")
    else:
        kol = money(L1[1], user_id)
        nm = L1[0][-1]
        if kol['type'] == "error":
            await bot.send_message(msg.chat.id, f"{mention}, введите корректное число(Доступны сокращения: М К)")
        else:
            if int(kol['txt']) < 1000:
                await bot.send_message(msg.chat.id, f"{mention}, минимальная ставка 1000")
            elif Drive[chat_id]['max'] >= 80:
                await bot.send_message(msg.chat.id, f"{mention}, ставки уже не принимаются. Ждём конца!")
            else:
                if user_id not in Drive[chat_id]['stavki'].keys():
                    Drive[chat_id]['stavki'][user_id] = []
                Drive[chat_id]['stavki'][user_id].append({"num":nm, "kol":kol['txt']})
                BD[user_id]['balance'] -= int(kol['txt'])
                save()
                await bot.send_message(msg.chat.id, f"{mention} поставил {kol['txt']} на {L1[0]}")

async def log_fun(chat_id, user_id):
    global chat_ruletka
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    t1 = f"{mention}, лог группы:\n"
    for i in chat_ruletka[chat_id]['log']:
        t1 = t1 + i + "\n"

    await bot.send_message(chat_id, t1)

async def povtor_stavka(chat_id, user_id):
    global chat_ruletka
    t1 = ""
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    if user_id not in chat_ruletka[chat_id]['stavki'].keys():
        chat_ruletka[chat_id]['stavki'][user_id] = {"nm":[], "cl":[]}
    idd = 0
    for i in chat_ruletka[str(chat_id)]['stavki'][user_id]['cl']:
        chat_ruletka[str(chat_id)]['stavki'][user_id]['cl'][idd]['gm1'] = True
        t1 += f"<b>Повторена ставка</b> {i['stavka_color']} на {i['color']}\n"
        idd += 1
    idd = 0
    t1 += "\n"
    for i in chat_ruletka[str(chat_id)]['stavki'][user_id]['nm']:
        chat_ruletka[str(chat_id)]['stavki'][user_id]['nm'][idd]['gm2'] = True
        t1 += f"<b>Повторена ставка {chat_ruletka[str(chat_id)]['stavki'][user_id]['nm'][idd]['stavka_num']} на:</b>\n"
        for _i in i['nums']:
            t1 += f"  {color_make(_i)['color']}{_i}\n"
        idd += 1

    if t1 == "":
        await bot.send_message(chat_id, f"{mention}, увы. Прошлых ставок не найдено")
    else:
        t1 = f"{mention}, прошлые ставки: \n\n" + t1
        await bot.send_message(chat_id, t1)

async def stavki(chat_id, user_id):
    if user_id not in chat_ruletka[chat_id]['stavki'].keys():
        chat_ruletka[chat_id]['stavki'][user_id] = {"nm":[], "cl":[]}
    t1 = ""
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    idd = 0
    for i in chat_ruletka[str(chat_id)]['stavki'][user_id]['cl']:
        if i['gm1'] == True:
            chat_ruletka[str(chat_id)]['stavki'][user_id]['cl'][idd]['gm1'] = True
            t1 += f"<b>ставка</b> {i['stavka_color']} на {i['color']}\n"
        idd += 1
    idd = 0
    t1 += "\n"
    for i in chat_ruletka[str(chat_id)]['stavki'][user_id]['nm']:
        if i['gm2'] == True:
            chat_ruletka[str(chat_id)]['stavki'][user_id]['nm'][idd]['gm2'] = True
            t1 += f"<b>ставка {chat_ruletka[str(chat_id)]['stavki'][user_id]['nm'][idd]['stavka_num']} на:</b>\n"
            for _i in i['nums']:
                t1 += f"  {color_make(_i)['color']}{_i}\n"
        idd += 1

    if t1 == "":
        await bot.send_message(chat_id, f"{mention}, Ваших ставок не найдено")
    else:
        t1 = f"{mention}, ваши ставки: \n\n" + t1
        await bot.send_message(chat_id, t1)

PROMO_BITWIN = {}
async def make_promo(msg, name, kol, mon):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if kkk not in DONAT.keys():
        await bot.send_message(msg.chat.id, f"{mention}, у вс не достаточно донат коинов!")
    else:
        kol = money(kol, kkk)
        if kol['type'] == "error":
            await bot.send_message(msg.chat.id, f"{mention}, введите павильное количество активаций")
        else:
            mon = money(mon, kkk)
            if mon['type'] == "error":
                await bot.send_message(msg.chat.id, f"{mention}, введите правильное число в призах!")
            else:
                if len(name) < 2 or len(name) > 12:
                    await bot.send_message(msg.chat.id, f"{mention}, введите имя промокода более 2 и менее 12 символов")
                else:
                    if name in PF['promo'].keys():
                        await bot.send_message(msg.chat.id, f"{mention}, Это имя уже занято")
                    else:
                        if int(kol['txt']) * int(mon['txt']) > BD[kkk]['balance']:
                            await bot.send_message(msg.chat.id, f"{mention}, вам не хватает монет. Нужно: {int(kol['txt']) * int(mon['txt'])}")
                        else:
                            kb = InlineKeyboardMarkup()
                            kb.add(InlineKeyboardButton("Без подписки(50к🌀)", callback_data=f"promoNotId_{kkk}"))
                            soo = await bot.send_message(msg.chat.id, f"{mention}, Отправте id канала, на который нужно подписаться для активации промокода. И добавте в него бота(со статусом администратор) \n\nЧерез пробел напишите ссылку, ведущую на канал.", reply_markup=kb)
                            PROMO_BITWIN[kkk] = {"name": name, "kol": int(kol['txt']), "mon": int(mon['txt']), "idd":"000", "type":"0", "chat": str(msg.chat.id), "msg": str(soo.message_id)}


async def chek_promo(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if kkk in PROMO_BITWIN.keys() and PROMO_BITWIN[kkk]['type'] == "0" and str(msg.chat.id) == PROMO_BITWIN[kkk]['chat']:
        L1 = msg.text.split(" ")
        if len(L1) == 2:
            idd = L1[0]
            link = L1[1]
            PROMO_BITWIN[kkk]['idd'] = idd
            kb = InlineKeyboardMarkup()
            kb.add(InlineKeyboardButton("Создать (50к🌀)", callback_data=f"promoId_{kkk}"))
            txt_promo = f"{mention}, Последний шаг в создании промокода:\n" \
                        f"Имя: {PROMO_BITWIN[kkk]['name']}\n" \
                        f"Количество: {PROMO_BITWIN[kkk]['kol']}\n" \
                        f"ID Канала: {PROMO_BITWIN[kkk]['idd']}\n\n" \
                        f"Стоимость создания: 50к🌀"
            PROMO_BITWIN[kkk]['type'] = "1"
            PROMO_BITWIN[kkk]['link'] = link
            await bot.delete_message(PROMO_BITWIN[kkk]['chat'], PROMO_BITWIN[kkk]['msg'])
            await asyncio.sleep(1)
            soo = await bot.send_message(msg.chat.id, txt_promo, reply_markup=kb)
            PROMO_BITWIN[kkk]['msg'] = soo.message_id
        else:
            await bot.send_message(msg.chat.id, f"{mention}, напишите через пробел id канала и ссылку на него. Если ссылка не нужно, то напишите любые символы одним словом.")


async def perevod(chat_id, user_id, replly_usser_id, much):
    global BD, LIMIT

    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    mention2 = "<a href='tg://openmessage?user_id=" + replly_usser_id + "'>" + BD[replly_usser_id]['name'] + "</>"
    much = money(much, user_id)
    if much['type'] == "ok":
        if BD[user_id]['balance'] < int(much['txt']) and BD[user_id]['admin'] == False:
            await bot.send_message(chat_id, f"{mention}, у вас не достаточно баланса для осуществления переводы такой суммы")
        else:
            if LIMIT - BD[user_id]['limit']['much'] - int(much['txt']) < 0 and BD[user_id]['admin'] == False:
                await bot.send_message(chat_id, f"{mention}, превышен лимит на перевод монет ({LIMIT - BD[user_id]['limit']['much'] - int(much['txt'])}/{LIMIT}) \n\nP.S Вы не можете перевести больше {LIMIT - (LIMIT - BD[user_id]['limit']['much'])}")
            else:
                if BD[user_id]['admin'] == False:
                    BD[user_id]['balance'] -= int(much['txt'])
                    BD[user_id]['limit']['much'] += int(much['txt'])
                else:
                    await bot.send_message(group_logs, f"Выданы монеты администратором. {datetime.now()}\nAdmin: tg://openmessage?user_id={user_id}\nUser: tg://openmessage?user_id={replly_usser_id}\n\nKol: {much['txt']}")
                BD[user_id]['give'] += int(much['txt'])
                BD[replly_usser_id]['take'] += int(much['txt'])

                BD[replly_usser_id]['balance'] += int(much['txt'])

                save()
                await bot.send_message(chat_id, f"{mention}, перевёл {much['txt']} этому игроку {mention2}")

async def chat_inf(chat_id, chat):
    soo = await bot.send_message(chat_id, "Поиск чата!")
    idd = 1
    chat_found = ""
    for i in CHAT.keys():
        if i == "-4181636704":
            pass
        else:
            if str(idd) == chat:
                chat_found = i
            idd += 1

    if chat_found == "":
        await bot.edit_message_text("Увы, номер чата не найден", chat_id, soo.message_id)
    else:
        txt = f"CHAT ID: {chat_found}\n" \
              f"Link: {CHAT[chat_found]['link']}\n" \
              f"сообщений: {CHAT[chat_found]['soo']}\n" \
              f"команды: {CHAT[chat_found]['cmd']}\n" \
              f"выиграно: {CHAT[chat_found]['win']}\n" \
              f"макс. выигрыш: {CHAT[chat_found]['max_win']}"
        await bot.send_message(chat_id, txt, reply_to_message_id=soo.message_id)

async def prof_fun(chat_id, user_id):
    mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
    b_prof = InlineKeyboardMarkup()
    b_prof.add(InlineKeyboardButton("💬Чат", url=chat_link))
    b_prof.add(InlineKeyboardButton("Канал", url=chanel_link))
    txt = f"{mention}, ваш профиль: \n" \
          f"🪪ID. {user_id} \n" \
          f"    💰Монеты ⧽ {BD[user_id]['balance']} \n" \
          f"    📨Передано ⧽ {BD[user_id]['give']}\n" \
          f"    📩Получено ⧽ {BD[user_id]['take']}\n" \
          f"    🏆выиграл ⧽ {BD[user_id]['win']}\n" \
          f"    ❌проиграл ⧽ {BD[user_id]['lose']}\n\n" \
          f"    🎲Макс. выигрыш ⧽ {BD[user_id]['max_win']} \n" \
          f"    🎲Макс. ставка ⧽ {BD[user_id]['max_stavka']}\n"
    await bot.send_photo(chat_id, open("assets/photo_2024-04-28 11.59.43.jpeg", "rb"), caption=txt, reply_markup=b_prof)

async def show_prof(chat_id, user_id):
    if user_id not in BD.keys():
        mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + "'Не зарегестрированый'" + "</>"
        await bot.send_message(chat_id, f"Информация о {mention}, id: {user_id} не найдена")
    else:
        mention = "<a href='tg://openmessage?user_id=" + user_id + "'>" + BD[user_id]['name'] + "</>"
        txt = f"Профиль {mention}\n" \
              f"ID. {user_id} \n" \
              f"    Монеты ⧽ {BD[user_id]['balance']} \n" \
              f"    Передано ⧽ {BD[user_id]['give']}\n" \
              f"    Получено ⧽ {BD[user_id]['take']}\n" \
              f"    выиграл ⧽ {BD[user_id]['win']}\n" \
              f"    проиграл ⧽ {BD[user_id]['lose']}\n\n" \
              f"    Макс. выигрыш ⧽ {BD[user_id]['max_win']} \n" \
              f"    Макс. ставка ⧽ {BD[user_id]['max_stavka']}\n"
        await bot.send_photo(chat_id, open("assets/photo_2024-04-28 11.59.43.jpeg", "rb"), caption=txt)

async def send_ref(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"

    if kkk not in REF.keys():
        REF[kkk] = {
            "usr": []
        }
        save_REF()
    txt = f"<b><i>{mention}, РЕФЕРАЛЬНАЯ СИСТЕМА</i></b>\n" \
          f"❗️ Приглашая людей в бота, вы и приглашенный получаете:\n" \
          f" • 100.000 💰\n" \
          f"\n" \
          f"〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️️\n" \
          f"<b><i>Информация по вашей ссылке:</i></b>\n" \
          f" • Ваша ссылка: https://t.me/GMCasioBot?start={kkk }\n" \
          f" • По вашей ссылке присоеденилось: {len(REF[kkk]['usr'])}\n" \
          f"〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️️\n" \
          f"<b><i>Дополнительная награда:</i></b>\n" \
          f" • 5 приглашений: 250 000💰\n" \
          f" • 10 приглашений: 300 000💰\n" \
          f" • 15 приглашений: 1 000 000💰\n" \
          f" • 20 приглашений: 1 500 000💰\n" \
          f" • Продолжение следует... "
    await bot.send_message(msg.chat.id, txt)

async def send_part(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if kkk not in WORK.keys():
        await bot.send_message(msg.chat.id, f"Вы не партнёр. Но можете им стать! \n\nСвязь: @Trykaban || @Ttypok")
    else:
        await bot.send_message(msg.chat.id, f"{mention}, ваша партнёрская программа:\n\n"
                                            f"🔗Ваша ссылка: https://t.me/GMCasioBot?start={WORK[kkk]['lnk']}\n"
                                            f"👤Инвайтов: {WORK[kkk]['kol']}\n"
                                            f"💬Сообщений в чатах: {WORK[kkk]['msg']}\n"
                                            f"\n"
                                            f"🗣Не забывайте присылать свои работы в чат! Там чаще и больше мы выдаём благодарностей!\n"
                                            f"⚡️Чат - {partner_chat_link}")

def timer(chat_id, user_id, msg):
    global BD, PF
    date_last_farm = datetime.strptime(str(PF['date']), "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
    tm = date2 - date_last_farm
    tm2 = int(tm.total_seconds())
    if tm2 >= 43200:
        PF['id'] += 1
        PF['date'] = str(msg.date)
        save_PF()

def person_limit(user_id):
    global BD, PF
    if BD[user_id]['limit']['time'] != str(PF['id']):
        BD[user_id]['limit']['time'] = str(PF['id'])
        BD[user_id]['limit']['much'] = 0
        save()

def chat_ruletka_fun(kkk):
    global chat_ruletka
    if kkk not in chat_ruletka:
        chat_ruletka[kkk] = {"log":[], "stavki":{}}

async def Promo(msg, promo):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if promo not in PF['promo'].keys():
        await bot.send_message(msg.chat.id, f"{mention}, такого промокода нету")
    else:
        if PF['promo'][promo]['end'] == "full":
            limit = True
        else:
            if PF['promo'][promo]['end'] > 0:
                limit = True

            else:
                limit = False
                await bot.send_message(msg.chat.id, f"{mention}, Промокод закончился", reply_to_message_id=msg.message_id)
        if kkk in PF['promo'][promo]['activ']:
            limit = False
            await bot.send_message(msg.chat.id, f"{mention}, вы уже его активировали!", reply_to_message_id=msg.message_id)
        if limit:
            if PF['promo'][promo]['id'] != "000":
                if "link" not in PF['promo'][promo].keys():
                    PF['promo'][promo]['link'] = "None"

                chek_chanel = True
                try:
                    user_channel_status = await bot.get_chat_member(chat_id=PF['promo'][promo]['id'], user_id=kkk)
                    if user_channel_status["status"] != 'left':
                        chanel = True
                    else:
                        await bot.send_message(msg.chat.id, f"{mention}, Вы не подписались на канал! Link: {PF['promo'][promo]['link']}")
                        chanel = False
                except:
                    await bot.send_message(msg.chat.id, f"{mention}, увы. На стороне создателя этого промокода произошла ошибка. Мы не можем работать с ним!")
            else:
                chek_chanel = False

            t1 = ""
            if chek_chanel:
                if chanel:
                    if PF['promo'][promo]['win'] == "balance":
                        t1 = f"{mention}, вы активировали промокод {promo}, и получили +{PF['promo'][promo]['kol']} монет"
                        PF['promo'][promo]['end'] -= 1
                    BD[kkk][PF['promo'][promo]['win']] += int(PF['promo'][promo]['kol'])
                    PF['promo'][promo]['activ'].append(kkk)
                    save()
                    await bot.send_message(msg.chat.id, t1, reply_to_message_id=msg.message_id)
            else:
                if PF['promo'][promo]['win'] == "balance":
                    t1 = f"{mention}, вы активировали промокод {promo}, и получили +{PF['promo'][promo]['kol']} монет"
                    PF['promo'][promo]['end'] -= 1
                BD[kkk][PF['promo'][promo]['win']] += int(PF['promo'][promo]['kol'])
                PF['promo'][promo]['activ'].append(kkk)
                save()
                await bot.send_message(msg.chat.id, t1, reply_to_message_id=msg.message_id)
        save_PF()

async def send_ban(msg, status):
    if status == "1":
        await bot.send_message(msg.chat.id, "Забанен, но не доставлено сообщение о бане. Когда бот заметит этого игрока в каком-нибудь чате, он ему сообщит")
    elif status == "2":
        await bot.send_message(msg.chat.id, "Забанен, оповещение доставлено")

async def give_ban_id(msg, l1):
    kkk2 = str(l1[2])
    mention = "<a href='tg://openmessage?user_id=" + kkk2 + "'>" + BD[kkk2]['name'] + "</>"
    sec = l1[1]
    clock = datetime.now() + timedelta(seconds=int(sec))
    txt_ban = f"{mention}, вы заблокированы. Администратор: {BD[str(msg.from_user.id)]['name']}\n" \
              f"\n" \
              f"дата в боте: {datetime.now()}\n" \
              f"бан до: {clock} || ({sec} секунд) ||\n" \
              f"\n" \
              f"Ваш статус в боте - /status\n" \
              f"❓Не согласны с решением? Напишите сообщение, и ответе на него командой !реп. Так оно дойдёт до нас!"
    try:
        await bot.send_message(kkk2, txt_ban)
        status = "2"
    except:
        status = "1"
    BAN[kkk2] = {"time":str(clock), "status":status}
    save_Ban()
    await send_ban(msg, status)
    await bot.send_message(group_logs, f"Бан, {datetime.now()}\n\nAdmin: {msg.from_user.id}\nUser: {kkk2}")

async def unban_id(msg, L1):
    kkk2 = str(L1[1])
    mention = "<a href='tg://openmessage?user_id=" + kkk2 + "'>" + BD[kkk2]['name'] + "</>"
    if kkk2 not in BAN.keys():
        await bot.send_message(msg.chat.id, f"на него не наложено никаких ограничений")
    else:
        del BAN[kkk2]
        save_Ban()
        try:
            await bot.send_message(kkk2, f"{mention}, с вас снят бан! Приятной игры")
            await bot.send_message(msg.chat.id, f"Ограничения сняты, сообщение доставлено до игрока. Ссылка на него - tg://openmessage?user_id={kkk2}")
        except:
            await bot.send_message(msg.chat.id, f"Ограничения сняты, но сообщение не доставлено до игрока. Ссылка на него - tg://openmessage?user_id={kkk2}")
        await bot.send_message(group_logs, f"Разбан, {datetime.now()}\n\nAdmin: {msg.from_user.id}\nUser: {kkk2}")
async def give_ban(msg, l1):
    kkk2 = str(msg.reply_to_message.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk2 + "'>" + BD[kkk2]['name'] + "</>"
    sec = l1[1]
    clock = datetime.now() + timedelta(seconds=int(sec))
    txt_ban = f"{mention}, вы заблокированы. Администратор: {BD[str(msg.from_user.id)]['name']}\n" \
              f"\n" \
              f"дата в боте: {datetime.now()}\n" \
              f"бан до: {clock} || ({sec} секунд) ||\n" \
              f"\n" \
              f"Ваш статус в боте - /status\n" \
              f"❓Не согласны с решением? Напишите сообщение, и ответе на него командой !реп. Так оно дойдёт до нас!"
    try:
        await bot.send_message(kkk2, txt_ban)
        status = "2"
    except:
        status = "1"
    BAN[kkk2] = {"time":str(clock), "status":status}
    save_Ban()
    await send_ban(msg, status)
    await bot.send_message(group_logs, f"Бан, {datetime.now()}\n\nAdmin: {msg.from_user.id}\nUser: {kkk2}")

async def chek_ban(msg):
    kkk2 = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk2 + "'>" + BD[kkk2]['name'] + "</>"
    date_last_farm = datetime.strptime(str(BAN[kkk2]["time"]).split(".")[0], "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
    tm = date2 - date_last_farm
    tm2 = int(tm.total_seconds())
    if tm2 >= 0:
        del BAN[kkk2]
        save_Ban()
        await bot.send_message(msg.chat.id, f"{mention}, бан прошёл! Спасибо за ожидание, мы желаем вам приятной, а главное удачной игры!", reply_to_message_id=msg.message_id)

async def unban(msg):
    kkk2 = str(msg.reply_to_message.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk2 + "'>" + BD[kkk2]['name'] + "</>"
    if kkk2 not in BAN.keys():
        await bot.send_message(msg.chat.id, f"на него не наложено никаких ограничений")
    else:
        del BAN[kkk2]
        save_Ban()
        try:
            await bot.send_message(kkk2, f"{mention}, с вас снят бан! Приятной игры")
            await bot.send_message(msg.chat.id, f"Ограничения сняты, сообщение доставлено до игрока. Ссылка на него - tg://openmessage?user_id={kkk2}")
        except:
            await bot.send_message(msg.chat.id, f"Ограничения сняты, но сообщение не доставлено до игрока. Ссылка на него - tg://openmessage?user_id={kkk2}")
        await bot.send_message(group_logs, f"Бан, {datetime.now()}\n\nAdmin: {msg.from_user.id}\nUser: {kkk2}")

async def Bonus(msg, status):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    cmd = False
    if "bonus" not in BD[kkk].keys():
        BD[kkk]['bonus'] = str(datetime.now().date())
        cmd = True
    elif BD[kkk]['bonus'] != str(datetime.now().date()):
        BD[kkk]['bonus'] = str(datetime.now().date())
        cmd = True

    if cmd:
        rz = random.randint(10000, 15000)
        t1 = ''
        if status == 1:
            rz += int((rz / 100)*10)
            t1 = "+20% [GOLD VIP]"
        elif status == 2:
            rz += int((rz / 100)*20)
            t1 = "+20% [DIMOND VIP]"
        await bot.send_message(msg.chat.id, f"{mention}, вы залутали ежедневынй бонус +{rz}. {t1}")
        BD[kkk]['balance'] += int(rz)
    else:
        await bot.send_message(msg.chat.id, f"{mention}, вы сегодня уже лутали боус")
    save()

async def Koder(msg, status):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    cmd = False
    if "kod" not in BD[kkk].keys():
        BD[kkk]['kod'] = str(datetime.now().date())
        cmd = True
    elif BD[kkk]['kod'] != str(datetime.now().date()):
        BD[kkk]['kod'] = str(datetime.now().date())
        cmd = True

    if cmd:
        rz = random.randint(100000, 150000)
        t1 = ''
        if status == 1:
            rz += int((rz / 100)*10)
            t1 = "+20% [GOLD VIP]"
        elif status == 2:
            rz += int((rz / 100)*20)
            t1 = "+20% [DIMOND VIP]"
        await bot.send_message(msg.chat.id, f"{mention}, Вы написали код, и он вам принёс +{rz}. {t1}")
        BD[kkk]['balance'] += int(rz)
    else:
        await bot.send_message(msg.chat.id, f"{mention}, вы за сегодня стёрли все пальцы. Отдохните!")
    save()
async def start_tir(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if "TIR" not in BD[kkk].keys():
        BD[kkk]['TIR'] = str(msg.date)
        cmd = True
    else:
        date_last_farm = datetime.strptime(str(BD[kkk]["TIR"]), "%Y-%m-%d %H:%M:%S")
        date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
        tm = date2 - date_last_farm
        tm2 = int(tm.total_seconds() // 60)
        if tm2 * 60 >= 7200:
            BD[kkk]['TIR'] = str(msg.date)
            cmd = True
            save()
        else:
            await bot.send_message(msg.chat.id, f"{mention}, Играть в тир можно раз в 2 часа! Подождите немного")
            cmd = False
    if cmd:
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("Винтовка #1", callback_data=f"TIR_{kkk}:1"))
        kb.add(InlineKeyboardButton("Винтовка #2", callback_data=f"TIR_{kkk}:2"))
        kb.add(InlineKeyboardButton("Винтовка #3", callback_data=f"TIR_{kkk}:3"))
        await bot.send_message(msg.chat.id, f"{mention}, Тир! \n\nВсё просто, у тебя на выбор 3 ружья, ты 100% получишь свой приз, но чем метче стреляет твоя винтовка, тем больше шнасов получить приз больше! \n\nПришло время выбирать винтовку. Удачи!", reply_markup=kb)

async def Mask(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    cmd = False
    if "mask" not in BD[kkk].keys():
        BD[kkk]['mask'] = str(datetime.now().date())
        cmd = True
    elif BD[kkk]['mask'] != str(datetime.now().date()):
        BD[kkk]['mask'] = str(datetime.now().date())
        cmd = True
    else:
        await bot.send_message(msg.chat.id, f"{mention}, Вы сегодня уже писали маску")

    if cmd:
        if random.randint(1, 100) > 95:
            rz = random.randint(100000, 300000)
            await bot.send_message(msg.chat.id, f"{mention}, маск вам ответил, и дал {money_form(str(rz))}")
            BD[kkk]['balance'] += int(rz)
        else:
            await bot.send_message(msg.chat.id, f"{mention}, Маск вас проигнорировал :(")
    save()

async def lotery_buy(msg, kol):
    global Lot
    kkk = str(msg.chat.id)
    await registration(kkk)
    kol = money(kol, kkk)
    if kol['type'] == "error":
        await bot.send_message(msg.chat.id, f"Введите число!")
    else:
        stom = int(kol['txt']) * 10000
        if stom > BD[kkk]['balance']:
            await bot.send_message(msg.chat.id, f"У вас не достаточно монет")
        else:
            if kkk not in Lot['lot']['usr'].keys():
                Lot['lot']['usr'][kkk] = 0

            Lot['lot']['kol'] += int(kol['txt'])
            Lot['lot']['usr'][kkk] += int(kol['txt'])
            BD[kkk]['balance'] -= stom
            save()
            save_LOT()
            await bot.send_message(msg.chat.id, f"🎟{BD[kkk]['name']}, вы купили {kol['txt']} билетиков. \n💸Общая сумма оплаты составила: {stom}")
            try:
                await bot.edit_message_text(f"🎟Лотерейный магазинчик🎟\n"
                                            f"\n"
                                            f"🔱Главный приз ⧽ 50.000.000 (10м)\n"
                                            f"💸Стоимость билетика ⧽ 10.000 (10к)\n"
                                            f"\n"
                                            f"👤Купленных билетиков ⧽ {Lot['lot']['kol']}\n"
                                            f"❓Купить билетик можно в боте ⧽ /lot [количество]", chanel_id, Lot['lot']['ID'])
            except:
                pass

async def lotery_start(msg):
    global Lot
    List = []
    for i, y in Lot['lot']['usr'].items():
        for _i in range(int(y)):
            List.append(i)

        if i not in BD.keys():
            await registration(str(i))

    winer = random.choice(List)
    List = []
    Lot['lot']['valid'] = False
    Lot['lot']['usr'] = {}


    BD[winer]['balance'] += 10000000
    save()
    try:
        await bot.send_message(winer, "Вы выйграли в лотерею! +10 000 000")
    except:
        pass


    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("Лотерея прошла!", url="https://t.me/TryChanel_casino"))
    await bot.edit_message_text(f"🎟Лотерейный магазинчик🎟\n"
                                f"\n"
                                f"🔱Главный приз ⧽ 10.000.000 (10м)\n"
                                f"👤Купленных билетиков: {Lot['lot']['kol']}\n"
                                f"\n"
                                f"🔱Определён победитель с ID:{winer}! Проверь свой ID в профиле ;)", chanel_id, Lot['lot']['ID'])

    Lot['lot']['kol'] = 0
    save_LOT()

async def rassel(msg):
    control = 1
    await bot.send_message(group_logs, f"Рассылка: {datetime.now()}\n\nAdmin: {msg.from_user.id}")
    if msg.reply_to_message:
        col = 0
        col2 = 0
        kol1 = 1
        txt_publ = "лист не получившихся рассылок: \n\n"
        for i in CHAT.keys():
            try:
                await bot.forward_message(i, msg.chat.id, msg.reply_to_message.message_id)
                col += 1
            except:
                txt_publ += f"\n{kol1}. операция провалилась: {i}"
                col2 += 1
            kol1 += 1

        await bot.send_message(msg.chat.id, f"Успешных рассылок: {col} \nпровалы: {col2}")
    else:
        await bot.send_message(msg.chat.id, "Нужно ответом на сообщение")

async def send_ahelp(msg):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    await bot.send_message(msg.chat.id, f"{mention}, вы администратор. Вам доступны команды:\n\n"
                                        f"<b>[1]</b>  +админ/-админ <b>⧽</b> + или - на должность администратора.\n"
                                        f"<b>[2]</b>  !inf [id] <b>⧽</b> информация о человеке по id\n"
                                        f"<b>[3]</b>  .id <b>⧽</b> получить id игрока\n"
                                        f"<b>[4]</b>  чаты <b>⧽</b> топ 15 чатов\n"
                                        f"<b>[5]</b>  !chat [num] <b>⧽</b> статистика о чате\n"
                                        f"<b>[6]</b>  !donat [id player] [kol] <b>⧽</b> выдача донатов\n"
                                        f"<b>[7]</b>  !publ <b>⧽</b> рассылка по чатам\n"
                                        f"<b>[8]</b>  !slot <b>⧽</b> Конец лотереи\n"
                                        f"<b>[9]</b>  !lot <b>⧽</b> Начало лотереи\n"
                                        f"<b>[10]</b>  !бан [секунды] [ответом или ID] <b>⧽</b> бан на время\n"
                                        f"<b>[11]</b>  !разбан [ответом или ID] <b>⧽</b> досрочный разбан\n"
                                        f"<b>[12]</b> [!work / !unwork] <b>⧽</b> Выкл/Вкл работу бота\n"
                                        f"<b>[13]</b> /lim - снять лимит, ответом на сообщение\n")
async def send_help(msg):
    await asyncio.sleep(1)
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    txt_help = f"Дилер: {mention}, чем могу помочь? \n\n" \
           f"  1.💰 заработок \n" \
           f"  2.🎰 игры \n" \
           f"  3.🚀 Базовые\n\n" \
           f"❓Нажми на кнопки, чтобы узнать подробнее."

    bt_m = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("💰заработок", callback_data="job")
    b2 = InlineKeyboardButton("🎰игры", callback_data="happy")
    b3 = InlineKeyboardButton("🚀базовые", callback_data="main")
    b4 = InlineKeyboardButton("⚡️Команды(/)", callback_data="cmds")
    bt_m.add(b1, b2)
    bt_m.add(b3)
    bt_m.add(b4)
    await bot.send_sticker(msg.chat.id, sticker="CAACAgIAAxkBAAEFBnxmLMH_B7eyi4f4FpRC88vBLknTHwACSQMAApzW5wqc5uBBhM3jHjQE")
    await bot.send_message(msg.chat.id, txt_help, reply_markup=bt_m)

CHAT_INVITE = []
@dp.message_handler(content_types=['new_chat_members'])
async def new_user_joined(message: types.Message):
    global Chat_id
    try:
        for i in message.new_chat_members:
            if str(message.chat.id) == Chat_id:
                kkk = str(message.from_user.id)
                id_chat = str(message.chat.id)
                kkk2 = str(i['id'])
                mention = "<a href='tg://user?id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
                await registration(kkk2)
                await asyncio.sleep(0.2)
                mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + BD[kkk2]['name'] + "</>"
                if kkk2 not in CHAT_INVITE:
                    await bot.send_message(message.chat.id, f"{mention}, вы добавили {mention2}! +1 000 000 000(MK)")
                    BD[kkk]['balance'] += 1000000000
                    save()
                    CHAT_INVITE.append(kkk2)
                    try:
                        await bot.send_message(group_logs, f"Приглашён в чат новый игрок. \nID Приглашённого: {kkk2} ({mention2})\nID Приглашающего: {kkk} ({mention})")
                    except:
                        pass
                else:
                    await bot.send_message(message.chat.id, f"{mention}, этого пользователя уже добавляли за сеанс ({mention2}) уже добавляли")
    except:
        pass
@dp.message_handler(commands=["Buyvip", "buyvip"])
async def Spirit_Help(msg: types.Message):
    await registration(str(msg.from_user.id))
    await vip_send(msg)

@dp.message_handler(commands=["Spirit", "spirit"])
async def Spirit_Help(msg: types.Message):
    kkk = str(msg.from_user.id)
    await registration(kkk)

    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"

    txt = f"{mention}, Что такое Spirit coin? \n\n" \
          f"spirit Coin🌀 - это донатная валюта. Вы можете её приобрести в магазине(Подробнее: Донат), или получить в раздаче:) \n" \
          f"\n" \
          f"Покупая её вы поддерживаете проект, и в замен мы разрешаем вам восполоваться бустами! Подробнее можно ознакомится в магазине донатов: Донат \n"

    await bot.send_message(msg.chat.id, txt)

@dp.message_handler(commands=["moneybox", "Moneybox"])
async def money_box_help(msg: types.Message):
    kkk = str(msg.from_user.id)
    await registration(kkk)

    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"

    txt = f"{mention}, быстрая помощь по копилке:" \
          f"Копилка это способ фонового заработка. Положите деньги на депозит и не трогайте их в течении 24 часов. И вам добавится процент! \n" \
          f"\n" \
          f"1. Копилка [положить/снять] [сумма] - положить монетки в обычный банк\n" \
          f"\n" \
          f"2. Депозит [положить/снять] [сумма] - Положить денюжку под процент роста\n" \
          f"\n" \
          f"!Важно понимать, что если вы взаимодействуете с депозитным счётом - таймер обнуляется!\n"

    await bot.send_message(msg.chat.id, txt)
@dp.message_handler(commands=["donat", "Donat"])
async def donat_send(msg: types.Message):
    await send_donat_list(msg)

@dp.message_handler(commands=["pillow", "Pillow"])
async def donat_send(msg: types.Message):
    await bot.send_message(msg.chat.id, "🛏Подушка безопастности - Если ваш баланс составит менее 25к, падушка безопастности поможет избежать вам полного краха и вернёт 75к")

@dp.message_handler(commands=["Ref", "ref"])
async def donat_send(msg: types.Message):
    await send_ref(msg)

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

@dp.message_handler(commands=["status", "Status"])
async def start_command(msg: types.Message):
    kkk = str(msg.from_user.id)
    await registration(kkk)
    if kkk in BAN.keys():
        await chek_ban(msg)

    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if kkk not in BAN.keys():
        await bot.send_message(msg.chat.id, f"{mention}, на вас не наложено никаких ограничений. Приятной игры! \n\nЕсли вам нужна помощь, так и напиши 'помощь' - мы отправим все существующие команды")
    else:

        date_last_farm = datetime.strptime(str(BAN[kkk]["time"]).split(".")[0], "%Y-%m-%d %H:%M:%S")
        date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
        tm = date_last_farm - date2
        tm2 = int(tm.total_seconds())
        await bot.send_message(msg.chat.id, f"{mention}, на вас наложены ограничения!\n"
                                            f"\n"
                                            f"Ограничение: Бан\n"
                                            f"Продлится до: {str(BAN[kkk]['time']).split('.')[0]}\n"
                                            f"Осталось ждать: {tm2} сек")

@dp.message_handler(commands=["promokod", "Promokod"], state="*")
async def start_command(msg: types.Message):
    kkk = str(msg.from_user.id)
    await registration(kkk)
    await asyncio.sleep(1)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    txt_promo = f"{mention}, Промокоды! Это просто и интересно\n" \
                f"Стоимость создания: 500🌀\n\n" \
                f"<b>[1]</b> Пропишите команду: Создать промо [имя] [кол. активаций] [приз]\n" \
                f"\n" \
                f"<b>[2]</b> Бот предложит вам ввести ID канала, на который нужно подписаться прежде чем активировать промокод. (Вы можете выбрать без обязательной подписки)\n" \
                f"\n" \
                f"<b>[3]</b> Добавте меня в качестве администратора в ваш канал/чат и всё, промокод готов! \n" \
                f"\n" \
                f"❓Зачем добавлять бота в качестве администратора? -Только так мы сможем проверить подписку на канал или чат человека при активации промокода! Достаточны минимальные права администратора.\n" \
                f"\n" \
                f"❓Как узнать id канала/чата? -в чате: /chat_id || в канале: скопируйте username и вставте в бота(@username_to_id_bot)"
    await bot.send_message(msg.chat.id, txt_promo)

@dp.message_handler(commands=["start", "Start"], state="*")
async def start_command(msg: types.Message):
    await users_in_chat(str(msg.chat.id), msg)
    await chek_user_in_chat(str(msg.chat.id), msg.from_user.id, msg)
    kkk = str(msg.from_user.id)
    unique_code = str(extract_unique_code(msg.text))
    await registration(kkk)
    CMD = False
    work = False
    if unique_code in BD.keys():
        CMD = True
    if str(unique_code).split("_")[0] == "w":
        work = True
    b_start = InlineKeyboardMarkup()
    b_start.add(InlineKeyboardButton("💬Чат", url=chat_link))
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    txt = f"{mention}, Приветсвуем тебя в Казино бот! Тут ты можешь: \n" \
          f"\n" \
          f"🔥Играть в представленый игры! /games\n" \
          f"🔝Бороться за место в топе \n" \
          f"💬Общаться с единомышленниками\n" \
          f"⏰Убить время :)\n" \
          f"\n" \
          f"😎И вы этом мы тебе поможем! \n" \
          f"/games - узнай о играх в боте.\n" \
          f"/help - получи помощь по команда и др.\n" \
          f"/contact - Канал, чат.\n" \
          f"\n" \
          f"❤️Приятной игры!"
    await bot.send_message(msg.chat.id, txt, reply_markup=b_start)
    if work:
        idd = 0
        for i, y in WORK.items():
            if y['lnk'] == unique_code:
                idd = i
                break
        if idd != 0 and "users" not in WORK[idd].keys():
            WORK[idd]['users'] = []
        if idd != 0:
            try:
                if kkk not in WORK[idd]['users']:
                    WORK[idd]['users'].append(kkk)
                    if kkk in BD.keys():
                        BD[idd]['balance'] += 150000
                        await bot.send_message(idd, f"ПАРТНЁР СИСТЕМА ОБНАРУЖИЛА ПРИСОЕДЕНИВШЕГОСЯ УЧАСТНИКА К ПРОЕКТУ!\n\nОн уже был зарегестрирован. "
                                                    f"\n\nНо мы выдадим вам 150к!\n"
                                                    f"Игрок - {mention}")
                    else:
                        BD[idd]['balance'] += 100000
                        WORK[idd]['kol'] += 1
                        await bot.send_message(idd, f"ПАРТНЁР СИСТЕМА ОБНАРУЖИЛА ПРИСОЕДЕНИВШЕГОСЯ УЧАСТНИКА К ПРОЕКТУ!\n\nНовый участник в прокте! Привлеките его к проекту ещё сильнее и поделитесь с нами результатом в рабочем чате! "
                                                    f"\n\nПервая из наград за это 100к\n"
                                                    f"Игрок - {mention}")

            except:
                pass
            save()
            save_WORK()
    if CMD:
        if unique_code not in REF.keys():
            REF[unique_code] = {
                "usr": []
            }
        if kkk == unique_code:
            await bot.send_message(msg.chat.id, f"{mention}, Не хитри :)")
        elif kkk in REF[unique_code]['usr']:
            await bot.send_message(msg.chat.id, f"{mention}, Вы уже присоедениялись по этой реферальной ссылке")
        else:
            REF[unique_code]['usr'].append(kkk)
            await registration(unique_code)
            if len(REF[unique_code]['usr']) == 5:
                p = 250000
                try:
                    await bot.send_message(unique_code, f'{mention}, По вашей реферальной ссылке присоеденились <b>5 ЧЕЛОВЕК</b>\n'
                                                        f'Вы получили супер награду: {p}')
                except:
                    pass
                BD[unique_code]['balance'] += p
            elif len(REF[unique_code]['usr']) == 10:
                p = 300000
                try:
                    await bot.send_message(unique_code, f'{mention}, По вашей реферальной ссылке присоеденились <b>5 ЧЕЛОВЕК</b>\n'
                                                        f'Вы получили супер награду: {p}')
                except:
                    pass
                BD[unique_code]['balance'] += p
            elif len(REF[unique_code]['usr']) == 15:
                p = 1000000
                try:
                    await bot.send_message(unique_code, f'{mention}, По вашей реферальной ссылке присоеденились <b>5 ЧЕЛОВЕК</b>\n'
                                                        f'Вы получили супер награду: {p}')
                except:
                    pass
                BD[unique_code]['balance'] += p
            elif len(REF[unique_code]['usr']) == 20:
                p = 1000000
                try:
                    await bot.send_message(unique_code, f'{mention}, По вашей реферальной ссылке присоеденились <b>5 ЧЕЛОВЕК</b>\n'
                                                        f'Вы получили супер награду: {p}')
                except:
                    pass
                BD[unique_code]['balance'] += p
            else:
                p = 100000
                try:
                    await bot.send_message(unique_code, f'{mention}, По вашей реферальной ссылке присоеденились\n'
                                                        f'Вы получили: 100 000')
                except:
                    pass
                BD[unique_code]['balance'] += p


            BD[kkk]['balance'] += 100000
            await bot.send_message(msg.chat.id, f'{mention}, Вы присоеденились по реферальной ссылке!\n'
                                                f'Вы получили: 100 000')
            await send_ref(msg)
            await bot.send_message(group_logs, f"По рефу +1\n\nOwner Link: {unique_code}\nComes: {kkk}")
            save()
            save_REF()

@dp.message_handler(commands=["contact", "Contact"])
async def money_box_help(msg: types.Message):
    kkk = str(msg.from_user.id)
    await registration(kkk)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"

    b_game = InlineKeyboardMarkup()
    b_game.add(InlineKeyboardButton("💬Чат", url=chat_link))
    b_game.add(InlineKeyboardButton("Канал", url=chanel_link))
    txt = f"{mention}, На даный момент у нас есть:\n1) чат\n2)Канал"
    await bot.send_message(msg.chat.id, txt, reply_markup=b_game)

@dp.message_handler(commands=["games", "Games"])
async def money_box_help(msg: types.Message):
    kkk = str(msg.from_user.id)
    await registration(kkk)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"

    b_game = InlineKeyboardMarkup()
    b_game.add(InlineKeyboardButton("Рулетка", url="https://t.me/TryChat_casino/4"))
    b_game.add(InlineKeyboardButton("Лесенка", url="https://t.me/TryChat_casino/6"))

    txt = f"{mention}, мы представляем вам игры поддерживаемые ботом: \n" \
          f"\n" \
          f"🔥Рулетка: Всё просто, введи число(это ставка), а дальше нужно выбрать на что поставите\n" \
          f"   1. Ч, к - или(Черный, красный). Если выпадет число с красным цветом ставка умножается на 2\n" \
          f"   2, 0,1,2..12 - Введи числа на которые хочешь поставить, их можно ввести без ограничений. выигрыш умножается на 2.\n" \
          f"\n" \
          f"🔥Лесенка. Довольно популярная игра. Активируетеся командо Лесена (ставка).\n" \
          f"   Нажимайте на правильную кнопку, чтобы повысить множитель ставики. Главное вовремя остановиться, а то припдющет!\n" \
          f"\n" \
          f"Полная информация о играх играх:\n\n"

    await bot.send_message(msg.chat.id, txt, reply_markup=b_game)

@dp.message_handler(commands=["games", "Games"])
async def money_box_help(msg: types.Message):
    kkk = str(msg.from_user.id)
    await registration(kkk)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"

    b_game = InlineKeyboardMarkup()
    b_game.add(InlineKeyboardButton("Рулетка", url="https://t.me/TryChat_casino/4"))
    b_game.add(InlineKeyboardButton("Лесенка", url="https://t.me/TryChat_casino/6"))

    txt = f"{mention}, помощь по командам и работе бота: \n\n" \
          f"" \
          f""

    await bot.send_message(msg.chat.id, txt, reply_markup=b_game)

users_in_mini_ban = ["1299946843"]
work = True
@dp.message_handler()
async def sistema(msg: types.Message):
    global ruletka_in, BD, CHAT, chat_ruletka, users_in_mini_ban, work
    kkk = str(msg.from_user.id)
    await registration(kkk)
    await chek_vip(msg)
    await users_in_chat(str(msg.chat.id), msg)
    await chek_user_in_chat(str(msg.chat.id), msg.from_user.id, msg)
    await chat_registration(str(msg.chat.id), msg)
    if kkk not in BAN.keys():
        ban_contoll = True
    else:
        if BAN[kkk]['status'] == "1":
            await bot.send_message(msg.chat.id, reply_to_message_id=msg.message_id, text=f"ID{kkk}, вы заблокированы. \n\n"
                                                                                         f"Дата в боте: {datetime.now()}\n"
                                                                                         f"бан до: {BAN[kkk]['time']}\n\n"
                                                                                         f"Ps. Нам не удалось отправить это сообщения в личных с ботом, поэтому вы получили его только что.\n\n"
                                                                                         f"❓Не согласны с решением? Напишите сообщение, и ответе на него командой !реп. Так оно дойдёт до нас!")
            BAN[kkk]['status'] = "2"
        ban_contoll = False

    if msg.chat.id == "-1002042398001" and kkk in WORK.keys():
        WORK[kkk]['mag'] += 1
        if WORK[kkk]['dt'] != str(datetime.now().day):
            WORK[kkk]['msg'] = 1
            WORK[kkk]['dt'] = str(datetime.now().day)
        save_WORK()

    if work and kkk not in users_in_mini_ban and ban_contoll or kkk == str(GLAVA) or BD[kkk]['admin']:
        status_vip = 0
        await chek_promo(msg)
        if kkk in DONAT.keys() and 'vip' in DONAT[kkk].keys():
            if DONAT[kkk]['vip']['act'] == True:
                status_vip = DONAT[kkk]['vip']['vp']
        if status_vip == 1:
            await ewery_day_gold(msg)
        elif status_vip == 2:
            await ewery_day_dimond(msg)
            await pillow(msg)

        chat_ruletka_fun(str(msg.chat.id))
        person_limit(kkk)
        timer(str(msg.chat.id), kkk, msg)

        BD[kkk]['balance'] = int(BD[kkk]['balance'])
        save()

        mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
        L1 = msg.text.split(" ")

        COMMAND = False
        try:
            L_kontrol = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "*", "+", "-", "(", ")"," ", "", "0"]
            ctr = 0
            for i in msg.text:
                if i not in L_kontrol:
                    ctr = 1
                    break
            if ctr == 1:
                pass
            elif ctr == 0:
                await bot.send_message(msg.chat.id, f"{mention}, ответ на ваш пример: \n{msg.text} = {eval(msg.text)}")
                COMMAND = True
        except:
            pass
        if msg.chat.id == -1002072084420 and msg.from_user.id == 777000:
            await bot.unpin_chat_message(msg.chat.id, msg.message_id)
            await bot.send_message(msg.chat.id, f"📌Сообщение откреплено \n\n🚀Присоеденяйся к нам в чат, тут часто проходят раздачи, сливы и тд...", reply_to_message_id=msg.message_id)

        stavka = money(L1[0], kkk)
        if stavka['type'] == "ok":
            await play_rulet(str(msg.chat.id), msg.text, kkk, stavka)
            COMMAND = True
        if msg.text in ["Донат", "донат"]:
            await send_donat_list(msg)
            COMMAND = True
        if msg.text in ["Ставки", "ставки"]:
            await stavki(str(msg.chat.id), kkk)
        if msg.text in ["vip", "Vip", "/myvip", "/Myvip"]:
            await vip_watch(msg)
        if msg.text in ["б", "Б", "баланс", "Баланс"]:
            mn = ""
            if kkk in DONAT.keys():
                mn = f"   ⌈🌀Spirit ⧽ {DONAT[kkk]['donat']}⌋\n"
            await bot.send_message(msg.chat.id, f"{mention}, ваш баланс:\n\n   ⌈🪙монет ⧽ {BD[kkk]['balance']}⌋\n{mn}\n❓Что такое Spirit coin - /Spirit")
            COMMAND = True
        if msg.text in ["бб", "Бб", "ББ"]:
            await bot.send_message(msg.chat.id, "Скрытый баланс", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("Посматреть", callback_data="BB")))
        if msg.text in ["Go","go", "Го", "го"]:
            if str(msg.chat.id) not in ruletka_in.keys() or ruletka_in[str(msg.chat.id)] == False:
                ruletka_in[str(msg.chat.id)] = True
                await start_rulet(str(msg.chat.id))
                COMMAND = True
        if msg.text in ["Лог", "лог"]:
            await log_fun(str(msg.chat.id), kkk)
            COMMAND = True
        if L1[0] in ["BlackJack", "Blackjack", "blackJack", "blackjack"] and len(L1) >= 2:
            await start_blackJ(msg, L1[1])
        if msg.text in ["Повторить", "повторить"]:
            await povtor_stavka(str(msg.chat.id), kkk)
            COMMAND = True
        if msg.text[0] == "+" and msg.reply_to_message:
            await perevod(str(msg.chat.id), kkk, str(msg.reply_to_message.from_user.id), str(msg.text[1::]))
            COMMAND = True
        if msg.text in ["проф","Проф", "!Проф", "!проф", "Профиль", "профиль"]:
            await prof_fun(str(msg.chat.id), kkk)
            COMMAND = True
        if msg.text in ["Узнать ник", "узнать ник"]:
            await bot.send_message(msg.chat.id, f"{mention}, ваш ник: {BD[kkk]['name']}")
            COMMAND = True
        if L1[0] in ["лесенка", "Лесенка"] and len(L1) == 2:
            await Lecenka(str(msg.chat.id), kkk, L1[1])
            COMMAND = True
        if msg.text in ["топ", "Топ"]:
            await Top_List(str(msg.chat.id), kkk, msg)
            COMMAND = True
        if msg.text in ["чат", "Чат"]:
            await chat_send(msg)
        if msg.text in ["Помощь", "помощь", "/help", "/Help", "/help@GMCasioBot", "/Help@GMCasioBot"]:
            await send_help(msg)
            COMMAND = True
        if msg.text in ["!Бонус", "!бонус"]:
            await Bonus(msg, status_vip)
            COMMAND = True
        if msg.text in ["Написать Маску", "Написать маску", "написать Маску", "написать маску"]:
            await Mask(msg)
            COMMAND = True
        if msg.text in ["Программировать", "программировать", "Програмировать", "програмировать"]:
            await Koder(msg, status_vip)
            COMMAND = True
        if msg.text in ["Тир", "тир"]:
            await start_tir(msg)
            COMMAND = True
        if L1[0] in ["Гол", "гол"] and len(L1) == 2:
            await Gol_fun(L1[1], msg)
            COMMAND = True
        if L1[0] in ["Бас", "бас"] and len(L1) == 2:
            await Bal_fun(L1[1], msg)
            COMMAND = True
        if L1[0] in ["Боул", "боул"] and len(L1) == 2:
            await Boul_fun(L1[1], msg)
            COMMAND = True
        if L1[0] in ["Дартс", "дартс"] and len(L1) == 2:
            await Darts_fun(L1[1], msg)
            COMMAND = True
        if L1[0] in ["Спин", "спин"] and len(L1) == 2:
            await Spin_fun(L1[1], msg)
            COMMAND = True
        if msg.text in ["!Реп", "!реп"] and msg.reply_to_message:
            await bot.send_message(msg.chat.id, f"〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️️\nСообщение от {mention}, ID: {kkk}", reply_to_message_id=msg.reply_to_message.message_id)
            await bot.forward_message(GLAVA, msg.chat.id, msg.reply_to_message.message_id)
            await bot.send_message(msg.chat.id, f"{mention}, вы отправили сообщение владельцу.", reply_to_message_id=msg.reply_to_message.message_id)
            COMMAND = True
        if L1[0] in ["Промо", "промо", "Промокод", "промокод"] and len(L1) == 2:
            await Promo(msg, L1[1])
            COMMAND = True
        if msg.text in ["!Гонка", "!гонка"]:
            await start_drivars(msg)
            COMMAND = True
        if L1[0] in ["м1", "М1", "м2", "М2", "М3", "м3", "М4", "м4", "М5", "м5"] and len(L1) == 2:
            await drive_make_stavka(msg, L1)
            COMMAND = True
        if L1[0] in ["!Депозит", "!депозит"]:
            if len(L1) < 2:
                await bot.send_message(msg.chat.id, f"{mention}, введите номер товара, посматреть можно в донат магазине\n\nКоманда: донат")
            elif len(L1) >= 2:
                await DepDonat(msg, L1[1])
            COMMAND = True
        if L1[0] in ["Обменять", "обменять"]:
            if len(L1) < 2:
                await bot.send_message(msg.chat.id, f"{mention}, Введите коичество spirit coin🌀 которое хотите обменять.\n\n P.s В боте встреный калькулятор. Просто введи пример")
            elif len(L1) >= 2:
                await ObmDonat(msg, L1[1])
            COMMAND = True
        if msg.text in ["партнёр", "Партнёр"]:
            await send_part(msg)
        if len(L1) >= 3:
            if L1[0] in ["Сменить", "сменить"]:
                if L1[1] in ["ник", "Ник", "Имя", "имя"]:
                    name = ""
                    for i in L1[2::]:
                        name += i
                        name += " "

                    if len(name) > 18:
                        await bot.send_message(msg.chat.id, f"{mention}, ваше имя сильно большое. Уменьшите его до 18 символом")
                    else:
                        BD[kkk]['name'] = name
                        save()
                        await bot.send_message(msg.chat.id, f"{mention}, вы сменили нак на {name}")
                    COMMAND = True
        if L1[0] in ["/lot", "/Lot"] and len(L1) >= 2:
            await lotery_buy(msg, str(L1[1]))
        if msg.text in ["Моя копилка", "моя Копилка", "моя копилка", "Моя Копилка"]:
            if kkk not in BANK.keys():
                BANK[kkk] = {
                    "bank": 0,
                    "deposit": 0,
                    "chek_deposit": 0,
                    "time": str(msg.date),
                    "procent": 1,
                }
                save_BANK()
            await bank_deposit_time(kkk, str(msg.date), status_vip)
            await asyncio.sleep(1)
            txt = f"{mention}, ваша копилка: \n" \
                  f"Накоплено: {BANK[kkk]['bank']} \n" \
                  f"под процент: {BANK[kkk]['deposit']}\n" \
                  f"процент: {BANK[kkk]['procent']}%\n" \
                  f"\n" \
                  f"помощь по копилке - /moneybox"

            await bot.send_message(msg.chat.id, txt)
            COMMAND = True
        if L1[0] in ["Создать", "создать"] and len(L1) >= 5 and L1[1] in ["промо", "Промо"]:
            await make_promo(msg, L1[2], L1[3], L1[4])
            COMMAND = True
        if L1[0] in ["Копилка", "копилка"] and len(L1) == 3:
            kol = L1[2]
            if kkk not in BANK.keys():
                BANK[kkk] = {
                    "bank": 0,
                    "deposit": 0,
                    "chek_deposit": 0,
                    "time": str(msg.date),
                    "procent": 1,
                }
                save_BANK()
            if L1[1] in ["положить","Положить"]:
                await bank_take(str(msg.chat.id), kkk, kol, str(msg.date))
            elif L1[1] in ["снять", "Снять", "взять", "Взять"]:
                await bank_give(str(msg.chat.id), kkk, kol, str(msg.date))
            COMMAND = True
        if msg.text in ["Реф", "реф", "Реферал", "реферал"]:
            await send_ref(msg)
        if L1[0] in ["Депозит", "депозит"] and len(L1) == 3:
            kol = L1[2]
            if kkk not in BANK.keys():
                BANK[kkk] = {
                    "bank": 0,
                    "deposit": 0,
                    "chek_deposit": 0,
                    "time": str(msg.date),
                    "procent": 1,
                }
                save_BANK()
            if L1[1] in ["положить","Положить"]:
                await deposit_take(str(msg.chat.id), kkk, kol, str(msg.date), status_vip)
            elif L1[1] in ["снять", "Снять", "взять", "Взять"]:
                await deposit_give(str(msg.chat.id), kkk, kol, str(msg.date), status_vip)
            COMMAND = True
        if COMMAND:
            CHAT[str(msg.chat.id)]['cmd'] += 1
            save_CHAT()

        if BD[kkk]['admin'] or kkk == GLAVA:
            if msg.text in ["+Админ","+админ"] and msg.reply_to_message:
                BD[str(msg.reply_to_message.from_user.id)]['admin'] = True
                save()
                await bot.send_message(msg.chat.id, f"{mention}, вы назначили администратором проекта ID:{msg.reply_to_message.from_user.id}")
            if msg.text in ["-Админ","-админ"] and msg.reply_to_message:
                if str(msg.reply_to_message.from_user.id) != GLAVA:
                    BD[str(msg.reply_to_message.from_user.id)]['admin'] = False
                    save()
                    await bot.send_message(msg.chat.id, f"{mention}, вы сняли с администрации ID:{msg.reply_to_message.from_user.id}")
            if L1[0] in ["/par", "/Par", "/partner", "/Partner"] and len(L1) == 2:
                link_user = "w_" + str(int(L1[1]) // 2) + "ork"
                for _i, _y in WORK.items():
                    if _y['lnk'] == link_user:
                        link_user = "w_" + str(L1[1]) + "ork"
                        break
                WORK[str(L1[1])] = {"lnk": link_user, "kol": 0, "dt": "0", "msg": 0}
                save_WORK()
            if L1[0] in ["!inf", "!Inf"] and len(L1) == 2:
                idd = L1[1]
                await show_prof(str(msg.chat.id), idd)
            if msg.text in [".ID", ".id", ".Id", ".iD"] and msg.reply_to_message:
                await bot.send_message(msg.chat.id, f"Id: {msg.reply_to_message.from_user.id}")
            if msg.text in ["чаты", "Чаты"]:
                await All_chats(str(msg.chat.id))
            if L1[0] in ["!chat", "!Chat"] and len(L1) == 2:
                idd = str(L1[1])
                await chat_inf(str(msg.chat.id), idd)
            if L1[0] in ["!donat", "!Donat"] and len(L1) == 3:
                idd = L1[1]
                kol = L1[2]
                await donat_buy(str(msg.chat.id), kol, idd, BD[kkk]['name'])
            if L1[0] == "!publ" and BD[kkk]['admin'] == True:
                await rassel(msg)
            if msg.text in ["!slot", "!Slot", "//slot", "//Slot"]:
                await lotery_start(msg)
            if L1[0] in ["!Бан", "!бан"] and len(L1) == 2 and msg.reply_to_message:
                print("1")
                await give_ban(msg, L1)
            if L1[0] in ["!Бан", "!бан"] and len(L1) == 3 and str(msg.reply_to_message) == 'None':
                await give_ban_id(msg, L1)
            if L1[0] in ["!Разбан", "!разбан"] and len(L1) == 1 and msg.reply_to_message:
                await unban(msg)
            if L1[0] in ["!Разбан", "!разбан"] and len(L1) == 2 and str(msg.reply_to_message) == 'None':
                await unban_id(msg, L1)
            if msg.text in ["/lim", "/Lim"] and msg.reply_to_message:
                await limit_off(msg)
            if msg.text in ["!work", "!Work"] and work==False:
                work = True
                await bot.send_message(msg.chat.id, f"{mention}, бот снова работает!")
            if msg.text in ["!unwork", "!Unwork"] and work:
                work = False
                await bot.send_message(msg.chat.id, f"{mention}, бот отключён для всех, кроме админов")
            if msg.text in ["!lot", "!Lot", "//Lot", "//lot"]:
                kb = InlineKeyboardMarkup()
                kb.add(InlineKeyboardButton("Купить 🤑", callback_data="LotBuy"))
                soo = await bot.send_message(chanel_id, f"🎟Лотерейный магазинчик🎟\n"
                                                  f"\n"
                                                  f"🔱Главный приз ⧽ 10.000.000 (10м)\n"
                                                  f"💸Стоимость билетика ⧽ 10.000 (10к)\n"
                                                  f"\n"
                                                  f"👤Купленных билетиков: 0\n"
                                                  f"❓Купить билетик в боте можно по команде /lot [количество]", reply_markup=kb)

                Lot['lot'] = {"kol": 0, "ID": str(soo.message_id), "valid":True, "usr":{}}
                save_LOT()
            if msg.text in ["!ahelp", "!Ahelp", "/Ahelp", "/ahelp"]:
                await send_ahelp(msg)
    elif kkk in users_in_mini_ban and msg.chat.type == "private":
        await bot.send_message(msg.chat.id, f"А ну молчать")
    elif ban_contoll == False:
        await chek_ban(msg)
    elif work == False:
        if msg.chat.type == "private":
            await bot.send_message(msg.chat.id, f"Бот временно закрыт! Просим прощения за ожидание :(")

@dp.callback_query_handler(lambda call: call.data.startswith('BB'))
async def bonusik(call: types.CallbackQuery):
    kkk = str(call.from_user.id)
    mn = ""
    if kkk in DONAT.keys():
        mn = f"   ⌈🌀Spirit ⧽ {DONAT[kkk]['donat']}⌋\n"
    await bot.answer_callback_query(callback_query_id=call.id, text=f"Ваш баланс:\n\n   ⌈🪙монет ⧽ {BD[kkk]['balance']}⌋\n{mn}\n❓Что такое Spirit coin - /Spirit", show_alert=True)

@dp.callback_query_handler(lambda call: call.data.startswith('LotBuy'))
async def bonusik(call: types.CallbackQuery):
    kkk = str(call.from_user.id)
    await registration(kkk)
    if BD[kkk]['balance'] < 10000:
        await bot.answer_callback_query(callback_query_id=call.id, text=f"Ваш баланс:\n\n   ⌈🪙монет ⧽ {BD[kkk]['balance']}⌋ \n❗Количество билетиков - {Lot['lot']['usr'][kkk]}\n❗️Вам не хватает монет! {int(10000) - int(BD[kkk]['balance'])}", show_alert=True)
    else:
        user_channel_status = await bot.get_chat_member(chat_id=f'{chanel_id}', user_id=kkk)
        if user_channel_status["status"] != 'left':
            if kkk not in Lot['lot']['usr'].keys():
                Lot['lot']['usr'][kkk] = 0

            Lot['lot']['usr'][kkk] += 1
            Lot['lot']['kol'] += 1
            BD[kkk]['balance'] -= 10000
            save_LOT()
            save()

            kb = InlineKeyboardMarkup()
            kb.add(InlineKeyboardButton("Купить 🤑", callback_data="LotBuy"))
            await bot.edit_message_text(f"🎟Лотерейный магазинчик🎟\n"
                                        f"\n"
                                        f"🔱Главный приз ⧽ 10.000.000 (10м)\n"
                                        f"💸Стоимость билетика ⧽ 10.000 (10к)\n"
                                        f"\n"
                                        f"👤Купленных билетиков: {Lot['lot']['kol']}\n"
                                        f"❓Купить билетик в боте можно по команде /lot [количество]", call.message.chat.id, call.message.message_id, reply_markup=kb)
            await bot.answer_callback_query(callback_query_id=call.id, text=f"вы купили билетик, общее количество - {Lot['lot']['usr'][kkk]}")
        else:
            await bot.answer_callback_query(callback_query_id=call.id, text=f"Вы не подписаны на канал! :(", show_alert=True)


@dp.callback_query_handler(lambda call: call.data.startswith('Lec_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    user_id, Win, k, kol = call.data.replace('Lec_', '', 1).split(':')
    kkk = str(call.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + BD[kkk]['name'] + "</>"
    if user_id != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text=f"Это не ваша игра! Её можно вызвать командой лесенка (ставка)", show_alert=True)
    else:
        if Win == "1":
            await bot.send_message(call.message.chat.id, f"Увы, вы выбрали не ту лестницу. Оступились и упали.")
            BD[user_id]['balance'] -= int(kol)
            BD[user_id]['lose'] += int(kol)
            save()
        elif Win == "0":
            if k == "0":
                kafec = 1
            elif k == "1":
                kafec = 1.25
            elif k == "1.25":
                kafec = 1.75
            elif k == "1.75":
                kafec = 2
            elif k == "2.2":
                kafec = 100
                await bot.send_message(call.message.chat.id, f"{mention}, Вы забрались на вершину! Коэффициент: 2.2x")
                b = int(int(kol) + int((int(kol)/100) * 2.2))
                BD[user_id]['balance'] += b
                BD[user_id]['win'] += b
                save()
            else:
                kafec = 2.2

            if kafec != 100:
                bt = InlineKeyboardMarkup()
                tr = True
                kol = money(kol, user_id)
                kol = int(kol['txt'])
                for i in range(4):
                    i += 1
                    if tr:
                        if random.randint(1, 100) > 50:
                            bt.add(InlineKeyboardButton(f"{i}", callback_data=f"Lec_{user_id}:0:{kafec}:{kol}"))
                        else:
                            bt.add(InlineKeyboardButton(f"{i}", callback_data=f"Lec_{user_id}:1:{kafec}:{kol}"))
                            tr = False
                    else:
                        bt.add(InlineKeyboardButton(f"{i}", callback_data=f"Lec_{user_id}:0:{kafec}:{kol}"))

                bt.add(InlineKeyboardButton("Остановиться", callback_data=f"LecS_{user_id}:1:{kafec}:{kol}"))

                await bot.send_message(call.message.chat.id, f"Вы взбираетесь на гору!\n Коэффициент:{kafec} \n\nВам нужно выбрать верную леcенку", reply_markup=bt)
        await bot.delete_message(call.message.chat.id, call.message.message_id)

@dp.callback_query_handler(lambda call: call.data.startswith('LecS_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    user_id, Win, k, kol = call.data.replace('LecS_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if user_id != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text=f"Это не ваша игра! Её можно вызвать командой лесенка (ставка)", show_alert=True)
    else:
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        if k == "0":
            await bot.send_message(call.message.chat.id, "Вы решили не лезть?")
            BD[user_id]['balance'] -= int(kol)
            BD[user_id]['lose'] += int(kol)
            save()
        if k == "1":
            await bot.send_message(call.message.chat.id, "Вы не лишились и не заработали!")
        else:
            kaf = float(k)
            b = int(int(kol) + int((int(kol)/100) * kaf))
            BD[user_id]['balance'] += b
            BD[user_id]['win'] += b
            save()
            await bot.send_message(call.message.chat.id, f"Вы забрались достаточно высоко, чтобы получить монеты. Так держать! \n+{int(int(kol) + int((int(kol)/100) * kaf))}")

@dp.callback_query_handler(lambda call: call.data.startswith('TIR_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    user_id, num = call.data.replace('TIR_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if user_id != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text=f"Это не ваша игра! Её можно вызвать командой тир", show_alert=True)
    else:
        mention = "<a href='tg://user?id=" + kkk + "'>" + BD[kkk]['name'] + "</a>"
        q = random.randint(1, 8)
        if q == 3:
            await bot.send_message(call.message.chat.id, f"{mention}, вы попали точно в цель! Ваша награда: 250к")
            BD[kkk]['balance'] += 250000
        elif q == 4:
            await bot.send_message(call.message.chat.id, f"{mention}, Это очень близко к цели! Ваша награда: 100к")
            BD[kkk]['balance'] += 100000
        else:
            await bot.send_message(call.message.chat.id, f"{mention}, Не близко, не далеко! Ваша награда: 75к")
            BD[kkk]['balance'] += 75000
        save()
        await bot.delete_message(call.message.chat.id, call.message.message_id)

@dp.callback_query_handler(lambda call: call.data.startswith("back1"))
async def backer(call: types.CallbackQuery):
    kkk = str(call.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + BD[kkk]['name'] + "</a>"
    txt_help = f"Дилер: {mention}, чем могу помочь? \n\n" \
               f"  1.💰 заработок \n" \
               f"  2.🎰 игры \n" \
               f"  3.🚀 Базовые\n\n" \
               f"❓Нажми на кнопки, чтобы узнать подробнее."

    bt_m = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("💰заработок", callback_data="job")
    b2 = InlineKeyboardButton("🎰игры", callback_data="happy")
    b3 = InlineKeyboardButton("🚀Базовые", callback_data="main")
    b4 = InlineKeyboardButton("⚡️Команды(/)", callback_data="cmds")
    bt_m.add(b1, b2)
    bt_m.add(b3)
    bt_m.add(b4)
    await bot.edit_message_text(txt_help, call.message.chat.id, call.message.message_id, reply_markup=bt_m)


@dp.callback_query_handler(lambda call: call.data.startswith("job"))
async def job_make(call: types.CallbackQuery):
    txt = f"🚀!Бонус\n" \
          f"🧑‍💻Программировать\n" \
          f"💬Написать маску\n" \
          f"🔫Тир\n"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)

@dp.callback_query_handler(lambda call: call.data.startswith("happy"))
async def job_make(call: types.CallbackQuery):
    txt = f"🎰Рулетка (10к ч/з)\n" \
          f"🪜Лесенка (ставка)\n" \
          f"\n" \
          f"➖➖➖➖➖➖➖➖\n" \
          f"🏀баc (ставка)\n" \
          f"⚽гол (ставка)\n" \
          f"🎰спин (ставка)\n" \
          f"🎯дратс (ставка)\n" \
          f"🎳боул (ставка)\n"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)

@dp.callback_query_handler(lambda call: call.data.startswith("main"))
async def job_make(call: types.CallbackQuery):
    txt = f"👤 проф - откроет ваше портфолио\n" \
          f"💵 баланс (б)\n" \
          f"💵 бб - скрытый баланс \n" \
          f"💸 +(монеты) - передайте монетки другому\n" \
          f"🏠 Сменить ник (имя)\n" \
          f"👑 Топ — лучшие игроки!\n" \
          f"\n" \
          f"🔱Донат - магазин бустов😎"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)

@dp.callback_query_handler(lambda call: call.data.startswith("cmds"))
async def job_make(call: types.CallbackQuery):
    txt = f"все бысрые команды в боте:\n" \
          f"/start\n" \
          f"/promokod\n" \
          f"/buyvip\n" \
          f"/games\n" \
          f"/help\n" \
          f"/contact\n" \
          f"/Spirit\n"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)

@dp.callback_query_handler(lambda call: call.data.startswith("DONAT_LIST"))
async def job_make(call: types.CallbackQuery):
    kkk = str(call.from_user.id)
    txt_donat = f"<b>💵 курс В РУБЛЯХ:</b>\n" \
                f"\n" \
                f"104 руб = 150.000🌀 (300.000.000🪙)\n" \
                f"208 руб = 750.000🌀 (1.500.000.000🪙)\n" \
                f"312 руб = 1.500.000🌀 (3.000.000.000🪙)\n" \
                f"416 руб = 2.250.000🌀 (4.500.000.000🪙)\n" \
                f"520 руб = 3.500.000🌀 (7.000.000.000🪙)\n" \
                f"624 руб = 5.000.000🌀 (10.000.000.000🪙)\n" \
                f"\n" \
                f"<b>💵 курс В ТЕНГЕ:</b>\n" \
                f"\n" \
                f"500тг - 150.000🌀 (300.000.000🪙)\n" \
                f"1000тг - 750.000🌀 (1.500.000.000🪙)\n" \
                f"1500тг - 1.500.000🌀 (3.000.000.000🪙)\n" \
                f"2000тг - 2.250.000🌀 (4.500.000.000🪙)\n" \
                f"2500тг - 3.500.000🌀 (7.000.000.000🪙)\n" \
                f"3000тг - 5.000.000🌀 (10.000.000.000🪙)\n" \
                f"\n" \
                f"❗️Не забудте указать id в донате или отправить скрин администратору! Зачисление быстрое\n"\
                f"\n"\
                f"🆔Ваш id: {kkk}\n" \
                f"🧑‍💻Связь с нами: @Trykaban || @Ttypok\n"

    await bot.send_message(call.message.chat.id, txt_donat)

@dp.callback_query_handler(lambda call: call.data.startswith('promoNotId_'))
async def robyFun(call: types.CallbackQuery):
    global BD
    kkk2 = str(call.from_user.id)
    kkk = call.data.replace('promoNotId_', '', 1).split(':')[0]
    if kkk2 == kkk:
        if DONAT[kkk]['donat'] < 50000:
            await bot.send_message(call.message.chat.id, f"ID: {kkk},  У вас не достаточно донат монет.")
        else:
            if BD[kkk]['balance'] < PROMO_BITWIN[kkk]['kol'] * PROMO_BITWIN[kkk]['mon']:
                await bot.send_message(call.message.chat.id, f"У вас недостаточно средств для создания промокода. Нужно: {PROMO_BITWIN[kkk]['kol'] * PROMO_BITWIN[kkk]['mon']}")
            else:
                PF['promo'][PROMO_BITWIN[kkk]['name']] = {"end": PROMO_BITWIN[kkk]['kol'], "win": "balance", "id": "000", "kol": PROMO_BITWIN[kkk]['mon'], "activ": []}
                save_PF()
                await bot.delete_message(PROMO_BITWIN[kkk]['chat'], PROMO_BITWIN[kkk]['msg'])
                await bot.send_message(call.message.chat.id, "Вы создали промокод! \n\n"
                                                             f"Промокод: {PROMO_BITWIN[kkk]['name']}\n"
                                                             f"Приз: {PROMO_BITWIN[kkk]['mon']}\n"
                                                             f"Активаций: {PROMO_BITWIN[kkk]['kol']}")
                BD[kkk]['balance'] -= PROMO_BITWIN[kkk]['kol'] * PROMO_BITWIN[kkk]['mon']
                DONAT[kkk]['donat'] -= 50000
                save()
                save_DONAT()
                del PROMO_BITWIN[kkk]

@dp.callback_query_handler(lambda call: call.data.startswith('promoId_'))
async def robyFun(call: types.CallbackQuery):
    global BD
    kkk2 = str(call.from_user.id)
    kkk = call.data.replace('promoId_', '', 1).split(':')[0]
    if kkk2 == kkk:
        print("1")
        print(PROMO_BITWIN)
        if DONAT[kkk]['donat'] < 50000:
            await bot.send_message(call.message.chat.id, f"ID: {kkk},  У вас не достаточно донат монет.")
        else:
            if BD[kkk]['balance'] < PROMO_BITWIN[kkk]['kol'] * PROMO_BITWIN[kkk]['mon']:
                await bot.send_message(call.message.chat.id, f"У вас недостаточно средств для создания промокода. Нужно: {PROMO_BITWIN[kkk]['kol'] * PROMO_BITWIN[kkk]['mon']}")
            else:
                PF['promo'][PROMO_BITWIN[kkk]['name']] = {"end": PROMO_BITWIN[kkk]['kol'], "owner":f"{kkk}", "link":f"{PROMO_BITWIN[kkk]['link']}", "win": "balance", "id": PROMO_BITWIN[kkk]['idd'], "kol": PROMO_BITWIN[kkk]['mon'], "activ": []}
                save_PF()
                await bot.delete_message(PROMO_BITWIN[kkk]['chat'], PROMO_BITWIN[kkk]['msg'])
                await bot.send_message(call.message.chat.id, "Вы создали промокод! С обязательной подпиской на канал.\n\n"
                                                             f"Промокод: {PROMO_BITWIN[kkk]['name']}\n"
                                                             f"Приз: {PROMO_BITWIN[kkk]['mon']}\n"
                                                             f"Активаций: {PROMO_BITWIN[kkk]['kol']}\n"
                                                             f"ссылка: {PROMO_BITWIN[kkk]['link']}")
                BD[kkk]['balance'] -= PROMO_BITWIN[kkk]['kol'] * PROMO_BITWIN[kkk]['mon']
                DONAT[kkk]['donat'] -= 50000
                save()
                save_DONAT()
                del PROMO_BITWIN[kkk]

@dp.callback_query_handler(lambda call: call.data.startswith('buygold'))
async def buygold(call: types.CallbackQuery):
    global BD
    kkk = str(call.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + BD[kkk]['name'] + "</a>"
    if kkk not in DONAT.keys() or DONAT[kkk]['donat'] < 100000:
        await bot.send_message(call.message.chat.id, f"{mention}, У вас не хватает Спирит коинов. \n\nИх можно приобрести: /donat")
    else:
        if "vip" not in DONAT[kkk].keys():
            vips = True
        else:
            if DONAT[kkk]['vip']['act'] == True:
                vips = False
            else:
                vips = True

        if vips:
            DONAT[kkk]['donat'] -= 100000
            clock = datetime.now() + timedelta(days=14)
            DONAT[kkk]['vip'] = {"act": True, "date": str(clock).split(".")[0], "vp":1, "bns":f"0"}
            save_DONAT()
            await bot.send_message(call.message.chat.id, f"{mention}, Вы приобрели GOLD VIP за 100.000 Spirit coins. На 2 недели(до {DONAT[kkk]['vip']['date']})\n\n🕔Время в боте: {str(datetime.now()).split('.')[0]}")
        else:
            await bot.send_message(call.message.chat.id, f"{mention}, У вас ещё не закончился предыдущий вип статус. При возникших проблемах можно обратиться в поддержку!")

@dp.callback_query_handler(lambda call: call.data.startswith('buydimond'))
async def buydmd(call: types.CallbackQuery):
    global BD
    kkk = str(call.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + BD[kkk]['name'] + "</a>"
    if kkk not in DONAT.keys() or DONAT[kkk]['donat'] < 300000:
        await bot.send_message(call.message.chat.id, f"{mention}, У вас не хватает Спирит коинов. \n\nИх можно приобрести: /donat")
    else:
        if "vip" not in DONAT[kkk].keys():
            vips = True
        else:
            if DONAT[kkk]['vip']['act'] == True:
                vips = False
            else:
                vips = True

        if vips:
            DONAT[kkk]['donat'] -= 300000
            clock = datetime.now() + timedelta(days=14)
            DONAT[kkk]['vip'] = {"act": True, "date": str(clock).split(".")[0], "vp":2, "bns":f"0"}
            save_DONAT()
            await bot.send_message(call.message.chat.id, f"{mention}, Вы приобрели DIMOND VIP за 300.000 Spirit coins. На 2 недели(до {DONAT[kkk]['vip']['date']})\n\n🕔Время в боте: {str(datetime.now()).split('.')[0]}")
        else:
            await bot.send_message(call.message.chat.id, f"{mention}, У вас ещё не закончился предыдущий вип статус. При возникших проблемах можно обратиться в поддержку!")

@dp.callback_query_handler(lambda call: call.data.startswith('takeBonus'))
async def buydmd(call: types.CallbackQuery):
    global BD
    kkk = str(call.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + kkk + "</a>"
    txt_bonus_chat = f"💸Каждые 200 сообщений в чате приходит магическая кнопка.\n" \
                     f"\n" \
                     f"💪Успей забрать по ней 10 миллионов!\n" \
                     f"\n" \
                     f"😎Актуальность: Забрали. (ID: {mention})"

    await bot.edit_message_text(txt_bonus_chat, call.message.chat.id, call.message.message_id)
    BD[kkk]['balance'] += 10000000
    save()

#######             BLACK JACK

@dp.callback_query_handler(lambda call: call.data.startswith('BJDBL_'))
async def robyFun(call: types.CallbackQuery):
    global BD
    kkk2 = str(call.from_user.id)
    kkk = call.data.replace('BJDBL_', '', 1).split(':')[0]
    mention = "<a href='tg://user?id=" + kkk + "'>" + kkk + "</a>"
    if kkk != kkk2:
        await bot.answer_callback_query(callback_query_id=call.id, text=f"Это не ваша игра! Начните её по команде: blackjack [ставка]  или  /blackjack [ставка]", show_alert=True)
    else:
        if BD[kkk]['balance'] < BlackJack[kkk]['stavka']:
            await bot.send_message(call.message.chat.id, f"{mention} У вас недостаточно средств для этого действия")
        else:
            BD[kkk]['balance'] -= BlackJack[kkk]['stavka']
            t = random.randint(2, 11)
            if t in [10, 9, 11]:
                t = random.randint(2, 11)

            BlackJack[kkk]['user'] += t
            BlackJack[kkk]['stavka'] += BlackJack[kkk]['stavka']
            await bot.delete_message(call.message.chat.id, call.message.message_id)
            kb = InlineKeyboardMarkup()
            kb.add(InlineKeyboardButton("🤑Удвоить", callback_data=f"BJDBL_{kkk}"))
            kb.add(InlineKeyboardButton("😎Взять", callback_data=f"BJTK_{kkk}"))
            kb.add(InlineKeyboardButton("👌Хватит", callback_data=f"BJSTP_{kkk}"))
            await bot.send_message(call.message.chat.id, f"{mention}, Вы удвоили ставку. Теперь ваши очки составляют: {BlackJack[kkk]['user']}\nСтавка: {BlackJack[kkk]['stavka']}\n\nВаш следующий шаг?", reply_markup=kb)

@dp.callback_query_handler(lambda call: call.data.startswith('BJTK_'))
async def robyFun(call: types.CallbackQuery):
    global BD
    kkk2 = str(call.from_user.id)
    kkk = call.data.replace('BJTK_', '', 1).split(':')[0]
    mention = "<a href='tg://user?id=" + kkk + "'>" + kkk + "</a>"
    if kkk != kkk2:
        await bot.answer_callback_query(callback_query_id=call.id, text=f"Это не ваша игра! Начните её по команде: blackjack [ставка]  или  /blackjack [ставка]", show_alert=True)
    else:
        t = random.randint(2, 11)
        if t in [10, 9, 11]:
            t = random.randint(2, 11)

        BlackJack[kkk]['user'] += t
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("🤑Удвоить", callback_data=f"BJDBL_{kkk}"))
        kb.add(InlineKeyboardButton("😎Взять", callback_data=f"BJTK_{kkk}"))
        kb.add(InlineKeyboardButton("👌Хватит", callback_data=f"BJSTP_{kkk}"))
        await bot.send_message(call.message.chat.id, f"{mention}, Диллер выдал вам карту. Теперь ваши очки составляют: {BlackJack[kkk]['user']}\nСтавка: {BlackJack[kkk]['stavka']}\n\nВаш следующий шаг?", reply_markup=kb)

@dp.callback_query_handler(lambda call: call.data.startswith('BJSTP_'))
async def robyFun(call: types.CallbackQuery):
    global BD
    kkk2 = str(call.from_user.id)
    kkk = call.data.replace('BJSTP_', '', 1).split(':')[0]
    mention = "<a href='tg://user?id=" + kkk + "'>" + kkk + "</a>"
    if kkk != kkk2:
        await bot.answer_callback_query(callback_query_id=call.id, text=f"Это не ваша игра! Начните её по команде: blackjack [ставка]  или  /blackjack [ставка]", show_alert=True)
    else:
        if BlackJack[kkk]['user'] == 21:
            b = random.randint(1, 12)
            if b == 1:
                await bot.send_message(call.message.chat.id, f"{mention}, НИЧЬЯ\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: 21")
                BD[kkk]['balance'] += BlackJack[kkk]['stavka']
            else:
                if b > 3:
                    await bot.send_message(call.message.chat.id, f"{mention}, Победа\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(22, 25)}")
                    BD[kkk]['balance'] += (BlackJack[kkk]['stavka'] * 2)
                else:
                    await bot.send_message(call.message.chat.id, f"{mention}, Победа\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(18, 20)}")
                    BD[kkk]['balance'] += (BlackJack[kkk]['stavka'] * 2)
        else:
            if BlackJack[kkk]['user'] > 21:
                b = random.randint(1, 5)
                if b == 1:
                    if BlackJack[kkk]['user'] > 26:
                        await bot.send_message(call.message.chat.id, f"{mention}, ПОРАЖЕНИЕ.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(18, 25)}")
                    else:
                        await bot.send_message(call.message.chat.id, f"{mention}, ПОБЕДА.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(BlackJack[kkk]['user'], BlackJack[kkk]['user']+3)}")
                        BD[kkk]['balance'] += (BlackJack[kkk]['stavka'] * 2)
                else:
                    await bot.send_message(call.message.chat.id, f"{mention}, ПОРАЖЕНИЕ.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(18, 21)}")
            elif BlackJack[kkk]['user'] == 20:
                b = random.randint(1, 5)
                if b == 1:
                    await bot.send_message(call.message.chat.id, f"{mention}, ПОРАЖЕНИЕ.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: 21")
                else:
                    await bot.send_message(call.message.chat.id, f"{mention}, ПОБЕДА.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(22, 25)}")
                    BD[kkk]['balance'] += (BlackJack[kkk]['stavka'] * 2)
            elif BlackJack[kkk]['user'] <= 19 and BlackJack[kkk]['user'] > 15:
                b = random.randint(1, 4)
                if b == 1:
                    await bot.send_message(call.message.chat.id, f"{mention}, ПОРАЖЕНИЕ.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: 21")
                else:
                    if b == 2 or b == 3:
                        await bot.send_message(call.message.chat.id, f"{mention}, ПОБЕДА.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(22, 24)}")
                        BD[kkk]['balance'] += (BlackJack[kkk]['stavka'] * 2)
                    else:
                        await bot.send_message(call.message.chat.id, f"{mention}, ПОРАЖЕНИЕ.\n\nВаши очки: {BlackJack[kkk]['user']}\n{random.randint(20, 21)}")
            elif BlackJack[kkk]['user'] <= 15:
                b = random.randint(1, 10)
                if b == 1:
                    await bot.send_message(call.message.chat.id, f"{mention}, ПОБЕДА.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(21, 27)}")
                    BD[kkk]['balance'] += (BlackJack[kkk]['stavka'] * 2)
                else:
                    await bot.send_message(call.message.chat.id, f"{mention}, ПОРАЖЕНИЕ.\n\nВаши очки: {BlackJack[kkk]['user']}\nОчки диллера: {random.randint(16, 21)}")

        await bot.delete_message(call.message.chat.id, call.message.message_id)
        save()


if __name__ == "__main__":
    load()
    print(f"[{str(datetime.now()).split('.')[0]}]Бот работает! \nЗарегестрированых: {len(BD)}")
    executor.start_polling(dp)
