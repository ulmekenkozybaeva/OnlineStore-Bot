import telebot
from telebot import types
import mysql.connector
import os

fake_db = []
channel_id = 'channel id'

db = mysql.connector.connect(
    host="your host",
    user="your username",
    password="your password",
    database="database name"
)

cursor = db.cursor()

bot = telebot.TeleBot("token")

ITEMS_PER_PAGE = 1
current_page = 1
current_device_type = ""

pagination_markup = types.InlineKeyboardMarkup(row_width=2)
prev_button = types.InlineKeyboardButton('<< ', callback_data='prev')
next_button = types.InlineKeyboardButton(' >>', callback_data='next')
basket = types.InlineKeyboardButton('Add to basket🛒', callback_data='basket')
open_basket = types.InlineKeyboardButton('Basket🛒', callback_data='open_basket')
pagination_markup.add(prev_button, next_button, basket, open_basket)


def markup_func(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Phone 📱', callback_data='btn1')
    btn2 = types.InlineKeyboardButton('Tablet 📱', callback_data='btn2')
    btn3 = types.InlineKeyboardButton('PC 💻', callback_data='btn3')
    markup.add(btn1, btn2, btn3)
    bot.reply_to(message, "Welcome!")
    bot.send_message(message.chat.id, 'Choose the type:', reply_markup=markup)


def send_item(message, item):
    name_devices, price, photo_name, description_devices = item

    photo_path = os.path.join(os.getcwd(), photo_name)

    with open(photo_path, 'rb') as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=f"<b>{name_devices}</b>\n Price: {price}\n\n{description_devices}",
            parse_mode="HTML"
        )


# replace the 'database' to your database name
def online_store_telegram(message, page, device_type):
    cursor.execute(f"SELECT database.name_devices, database.price, database.photo_name, database.description_devices FROM database WHERE database.type_devices = '{device_type}' LIMIT %s, 1", (page - 1,))
    result = cursor.fetchone()

    if result:
        send_item(message, result)
    else:
        bot.send_message(message.chat.id, f"There is no product in category: {device_type}")


@bot.message_handler(commands=['start'])
def start(message):
    send_info_message = "For more information /info."
    send_store_message = "To open the store /store"

    if message.from_user.last_name is not None:
        bot.send_message(message.chat.id, f"Welcome, {message.from_user.first_name} {message.from_user.last_name}!")
        bot.reply_to(message, text=send_info_message)
        bot.reply_to(message, text=send_store_message)
    else:
        bot.send_message(message.chat.id, f"Welcome, {message.from_user.first_name}!")
        bot.reply_to(message, text=send_info_message)
        bot.reply_to(message, text=send_store_message)


@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id, "There are available commands:\n /start to restart the bot \n /info to see the info about commands,"
                                      "\n /store to open the store")


@bot.message_handler(commands=['store'])
def online_store(message):
    global current_page, current_device_type

    current_page = 1
    current_device_type = ""
    markup_func(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global current_page, current_device_type

    if call.data.startswith('btn'):
        current_device_type = {'btn1': 'Phone', 'btn2': 'Tablet', 'btn3': 'PC'}.get(call.data, '')
        current_page = 1

        online_store_telegram(call.message, current_page, current_device_type)
        bot.send_message(call.message.chat.id, f'Page: {current_page}', reply_markup=pagination_markup)

    elif call.data == 'prev':
        if current_page > 1:
            current_page -= 1
            online_store_telegram(call.message, current_page, current_device_type)
            bot.send_message(call.message.chat.id, f'Page: {current_page}', reply_markup=pagination_markup)

    elif call.data == 'next':
        current_page += 1
        online_store_telegram(call.message, current_page, current_device_type)
        bot.send_message(call.message.chat.id, f'Page: {current_page}', reply_markup=pagination_markup)


    # replace the 'database' to your database name
    elif call.data == 'basket':
        cursor.execute(f"SELECT database.name_devices, database.price FROM database WHERE database.type_devices = '{current_device_type}' LIMIT %s, 1", (current_page - 1,))
        result = cursor.fetchone()

        if result:
            name_devices, price = result
            cursor.execute(f"INSERT INTO basket (name_devices, price) VALUES ('{name_devices}', '{price}')")
            db.commit()

            bot.send_message(call.message.chat.id, "The commodity was added to the basket! Enter /done if you want to end your shopping.")

        else:
            bot.send_message(call.message.chat.id, f"There is no {current_device_type}")

    elif call.data == 'open_basket':
        cursor.execute("SELECT name_devices, price FROM basket")
        basket_items = cursor.fetchall()

        if basket_items:
            basket_message = "Selected goods:\n"
            for item in basket_items:
                name_devices, price = item
                basket_message += f"Item: {name_devices}. Price: {price}\n"
                bot.send_message(call.message.chat.id, basket_message)


# user information

@bot.message_handler(commands=['done'])
def handle_info(message):
    chat_id = message.chat.id
    q1 = bot.send_message(chat_id, "<b>Enter</b> your name.", parse_mode='HTML')
    bot.register_next_step_handler(q1, enter_first_name)


def enter_first_name(message):
    fake_db.append(message.text)
    q2 = bot.reply_to(message, "Enter your city.".title())
    bot.register_next_step_handler(q2, enter_city)


def enter_city(message):
    fake_db.append(message.text)
    q3 = bot.reply_to(message, "Enter your address.".title())
    bot.register_next_step_handler(q3, enter_address)


def enter_address(message):
    fake_db.append(message.text)
    q4 = bot.reply_to(message, "Enter your phone number.".title())
    bot.register_next_step_handler(q4, enter_phone_number)


@bot.message_handler(content_types=['message'])
def enter_phone_number(message):
    fake_db.append(message.text)

    sql = "INSERT INTO orders (first_name, city, address, phone_number) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, fake_db)
    db.commit()
    bot.reply_to(message, "Thank you for choosing Us.")

    combined_message = "\n".join(fake_db[:100])
    bot.send_message(chat_id=channel_id, text=combined_message)

    fake_db.clear()

    cursor.execute("SELECT name_devices, price FROM basket")
    basket_items = cursor.fetchall()

    if basket_items:
        basket_message = "Selected goods:\n"
        for item in basket_items:
            name_devices, price = item
            basket_message += f"Item: {name_devices}. Price: {price}\n"

        bot.send_message(chat_id=channel_id, text=basket_message)

        cursor.execute("DELETE FROM basket")
        db.commit()

    else:
        bot.send_message(message.chat.id, "Empty.")


bot.polling()