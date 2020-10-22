import telebot
import mysql.connector
import config
from telebot import types
import re
import links

bot = telebot.TeleBot(config.db_token)

db = mysql.connector.connect(
    host=config.db_name,
    user=config.db_username,
    passwd=config.db_password,
    port=config.db_port,
    database=config.db_database
)

cursor = db.cursor()

back = links.backend_link
front = links.frontend_link
mobile = links.mobile_link

user_data = {}


class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ''
        self.phone_number = ''
        self.email_address = ''
        self.team_select = ''
        self.task_status = ''


@bot.message_handler(commands=['register'])
def try_register(message):
    if check_register_status(message.chat.id):
        bot.send_message(message.chat.id, "You are already registered!", parse_mode='HTML', reply_markup=keyboard3())
    else:
        send_welcome(message)


def send_welcome(message):
    msg = bot.send_message(message.chat.id, "What's your name?")
    bot.register_next_step_handler(msg, process_firstname_step)


def process_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)

        msg = bot.send_message(message.chat.id, "What's your surname?")
        bot.register_next_step_handler(msg, process_lastname_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_lastname_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text

        msg = bot.send_message(message.chat.id, "Tell me your phone number (Starting with 0...)")
        bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        bot.reply_to(message, "You are already registered")


def check_phone_valid(str):
    try:
        phone_num = int(str)
    except ValueError:
        return False
    if len(str) == 9 and str[0] == '0':
        return phone_num
    else:
        return False


def process_phone_step(message):
    user_id = message.from_user.id
    user = user_data[user_id]
    user.phone_number = message.text

    if check_phone_valid(message.text):
        msg = bot.send_message(message.chat.id, "Your email address?")
        bot.register_next_step_handler(msg, process_email_step)
    else:
        msg = bot.send_message(message.chat.id, "Your number is incorrect.Type your real cell-phone number!")
        bot.register_next_step_handler(msg, process_phone_step)


def check_email_valid(str):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, str)):
        return True
    else:
        return False


def process_email_step(message):
    user_id = message.from_user.id
    user = user_data[user_id]
    user.email_address = message.text

    if check_email_valid(message.text):
        msg = bot.send_message(message.chat.id, "Select your team!", reply_markup=keyboard2())
        bot.register_next_step_handler(msg, process_select_step)
    else:
        msg = bot.send_message(message.chat.id, "Your Email address is incorrect.Type your real Email address!")
        bot.register_next_step_handler(msg, process_email_step)


def process_select_step(message):
    try:
        if message.text == "Back-End":
            user_id = message.from_user.id
            user = user_data[user_id]
            user.team_select = message.text

            sql = """INSERT INTO users
            (first_name, last_name, phone_number, email_address, team_select, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (user.first_name, user.last_name, user.phone_number, user.email_address, user.team_select, user_id)
            cursor.execute(sql, val)
            db.commit()

            bot.send_message(message.chat.id, f"Okay {user.first_name}, you can now get a new task!",
                             reply_markup=keyboard3())

        elif message.text == "Front-End":
            user_id = message.from_user.id
            user = user_data[user_id]
            user.team_select = message.text

            sql = """INSERT INTO users
            (first_name, last_name, phone_number, email_address, team_select, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (user.first_name, user.last_name, user.phone_number, user.email_address, user.team_select, user_id)
            cursor.execute(sql, val)
            db.commit()

            bot.send_message(message.chat.id, f"Okay {user.first_name}, you can now get a new task!",
                             reply_markup=keyboard3())

        elif message.text == "Mobile":
            user_id = message.from_user.id
            user = user_data[user_id]
            user.team_select = message.text

            sql = """INSERT INTO users
            (first_name, last_name, phone_number, email_address, team_select, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (user.first_name, user.last_name, user.phone_number, user.email_address, user.team_select, user_id)
            cursor.execute(sql, val)
            db.commit()

            bot.send_message(message.chat.id, f"Okay {user.first_name}, you can now get a new task!",
                             reply_markup=keyboard3())

        else:
            msg = bot.send_message(message.chat.id, "Invalid command,  try again.")
            bot.register_next_step_handler(msg, process_select_step)

    except Exception as e:
        bot.reply_to(message, "You are already registered")


def check_register_status(id):
    sql = "select * from users"
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        if row[6] == id:
            return True
    return False


@bot.message_handler(commands=['start'])
def select_team(message):
    if check_register_status(message.chat.id):
        bot.send_message(message.chat.id, "Welcome back!", parse_mode='HTML', reply_markup=keyboard3())
    else:
        bot.send_message(
            message.chat.id,
            '''Greetings!
My name is "All-In Bot"
Click "Register" button to register''',
            reply_markup=keyboard()
        )


def check_task_status(id):
    sql = "select * from users where user_id={0}".format(id)
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        if row[7] == "Get task":
            return 1
        elif row[7] == "Finish task":
            return 2
        else:
            return 0


def check_team(id):
    sql = "select * from users where user_id={0}".format(id)
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        if row[4] == "Back-End":
            return 1
        elif row[4] == "Front-End":
            return 2
        elif row[4] == "Mobile":
            return 3
        else:
            return 0


@bot.message_handler(commands=['tasks'])
def task(message, msg_to_user="Would you like to get a new task?"):
    if check_register_status(message.chat.id):
        msg = bot.send_message(message.chat.id, msg_to_user, reply_markup=keyboard1())
        bot.register_next_step_handler(msg, process_get_task_step)
    else:
        bot.send_message(message.chat.id, "You need to be registered to get a task!", reply_markup=keyboard())


def process_get_task_step(message):
    task_status_current = check_task_status(message.chat.id)
    if message.text != "Get task":
        task(message, "Invalid command,  try again.")
        return
    if task_status_current == 1:
        msg = bot.send_message(message.chat.id, "You have task to finish yet", reply_markup=keyboard4())
        bot.register_next_step_handler(msg, process_finish_task_step)
    elif task_status_current != 2:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.task_status = message.text

        sql = "UPDATE users SET task_status = %s\
                WHERE user_id = %s"

        val = (user.task_status, user_id)
        cursor.execute(sql, val)
        db.commit()

        # Giving task
        if check_team(message.chat.id) == 1:
            msg = bot.send_message(message.chat.id, "Here is a task for you!", reply_markup=keyboard4())
            bot.send_message(message.chat.id, back)
            bot.register_next_step_handler(msg, process_finish_task_step)
        elif check_team(message.chat.id) == 2:
            msg = bot.send_message(message.chat.id, "Here is a task for you!", reply_markup=keyboard4())
            bot.send_message(message.chat.id, front)
            bot.register_next_step_handler(msg, process_finish_task_step)
        elif check_team(message.chat.id) == 3:
            msg = bot.send_message(message.chat.id, "Here is a task for you!", reply_markup=keyboard4())
            bot.send_message(message.chat.id, mobile)
            bot.register_next_step_handler(msg, process_finish_task_step)


def process_finish_task_step(message):
    task_status_current = check_task_status(message.chat.id)
    if task_status_current == 1:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.task_status = message.text

        sql = "UPDATE users SET task_status = %s\
                WHERE user_id = %s"
        val = (user.task_status, user_id)
        cursor.execute(sql, val)
        db.commit()

        if task_status_current != 0:
            bot.send_message(message.chat.id, "Congratulations!!!")


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('/register')
    markup.add(btn1)
    return markup


def keyboard1():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn7 = types.KeyboardButton('Get task')
    markup.add(btn7)
    return markup


def keyboard2():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn3 = types.KeyboardButton('Front-End')
    btn4 = types.KeyboardButton('Back-End')
    btn5 = types.KeyboardButton('Mobile')
    markup.add(btn3, btn4, btn5)
    return markup


def keyboard3():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn6 = types.KeyboardButton('/tasks')
    markup.add(btn6)
    return markup


def keyboard4():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn8 = types.KeyboardButton('Finish task')
    markup.add(btn8)
    return markup


@bot.message_handler(commands=['clean'])
def delete(message):
    dez = "DELETE FROM users WHERE id>0"
    cursor.execute(dez)
    db.commit()


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
