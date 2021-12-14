#@Gadzhiyavov_Dzhamal_bot
import telebot
from telebot import types
import psycopg2, time
token = "5055933944:AAEB35DgwO08yrlNnOCW6D6gU8U1es_y7gs"
bot = telebot.TeleBot(token)

conn = psycopg2.connect(
                        database="timetable_db",
                        user="postgres",
                        password="123456",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()
def rasp(den,day):
    cursor.execute(f"SELECT * FROM timetable WHERE day='{den}'")
    records = list(cursor.fetchall())
    a = day+"\n----------------------------------------\n"
    for i in records:
        ii = i[2].encode("cp1251").decode("cp866")
        a += ii
        if i[3] == 0:
            a += " Дистанционно "
        else:
            a += " "+str(i[3])+"ауд. "
        a += str(i[4] // 60) + ":" + str(i[4] % 60) + " "
        c = f"SELECT * FROM teacher WHERE subject='{i[2]}';"
        cursor.execute(c)
        rec = list(cursor.fetchall())
        cc = rec[0][1].encode("cp1251").decode("cp866")
        cc = cc.split()
        a += cc[0] + " " + cc[1][0] + "." + cc[2][0] + "."
        a += "\n"
    a += "----------------------------------------"
    return a


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.max_row_keys=3
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Расписание на текущую неделю","Расписание на следующую неделю")
    bot.send_message(message.chat.id, 'Доброго времени суток. Хотите посмотреть расписание? Нажмите на кнопку ниже.', reply_markup=keyboard)


@bot.message_handler(commands=['week'])
def start(message):
    nt=int((time.time()//1-1630443600)/3600/24/7)+2
    ntt = ""
    if nt % 2 == 0:
        ntt = "Нижняя неделя"
    else:
        ntt = "Верхняя неделя"
    bot.send_message(message.chat.id, f"{ntt} №{nt}")

@bot.message_handler(commands=['mtuci'])
def start(message):
    bot.send_message(message.chat.id, "Официальный сайт МТУСИ – https://mtuci.ru/")


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Я - бот, отображающий расписание группы БВТ2107. Вот список моих команд:\n'
                                      '/help - информация о боте\n'
                                      '/mtuci - ссылка на официальный сайт МТУСИ\n'
                                      '/week - узнать какая сейчас неделя\n'
                                      'Чтобы узнать расписание, нажимайте на кнопки на вашем экране.')


@bot.message_handler(content_types=['text'])
def answer(message):
    nt=(int((time.time()//1-1630270800)/3600/24/7)+1)
    ntt=1
    nttt=2
    if nt%2==0:
        ntt=2
        nttt=1
    else:
        ntt=1
        nttt=2

    if message.text.lower() == "понедельник":
        bot.send_message(message.chat.id, rasp(f"1.{ntt}",message.text.lower()))
    elif message.text.lower() == "вторник":
        bot.send_message(message.chat.id, rasp(f"2.{ntt}",message.text.lower()))
    elif message.text.lower() == "среда":
        bot.send_message(message.chat.id, rasp(f"3.{ntt}",message.text.lower()))
    elif message.text.lower() == "четверг":
        bot.send_message(message.chat.id, rasp(f"4.{ntt}",message.text.lower()))
    elif message.text.lower() == "пятница":
        bot.send_message(message.chat.id, rasp(f"5.{ntt}",message.text.lower()))
    elif message.text.lower() == "суббота":
        bot.send_message(message.chat.id, rasp(f"6.{ntt}",message.text.lower()))
    elif message.text.lower() == "расписание на текущую неделю":
        bot.send_message(message.chat.id, rasp(f"1.{ntt}","понедельник")+"\n"+rasp(f"2.{ntt}","вторник")+"\n"+rasp(f"3.{ntt}","среда")+"\n"+
                         rasp(f"4.{ntt}","четверг")+"\n"+rasp(f"5.{ntt}","пятница")+"\n"+rasp(f"6.{ntt}","суббота")+"\n")
    elif message.text.lower() == "расписание на следующую неделю":
        bot.send_message(message.chat.id,
                         rasp(f"1.{nttt}", "понедельник") + "\n" + rasp(f"2.{nttt}", "вторник") + "\n" + rasp(f"3.{nttt}","среда") + "\n" +
                         rasp(f"4.{nttt}", "четверг") + "\n" + rasp(f"5.{nttt}", "пятница") + "\n" + rasp(f"6.{nttt}","суббота") + "\n")
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понял.')

bot.polling()