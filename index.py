import os
from io import BytesIO
from queue import Queue
import requests
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler, Dispatcher


TOKEN = "6274458564:AAHr_I4iQfTIA9LubgfwaJeD_FYaBSVEmsc"
URL = "https://movies-downloader-bot-gules-xi.vercel.app"
bot = Bot(TOKEN)


def welcome(update, context) -> None:
   
    update.message.reply_text("👇 Enter Movie Name 👇")




def setup():
    update_queue = Queue()
    dispatcher = Dispatcher(bot, update_queue, use_context=True)
    dispatcher.add_handler(CommandHandler('start', welcome))
    
    return dispatcher


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Wttorld!'


@app.route('/{}'.format(TOKEN), methods=['GET', 'POST'])
def respond():
    update = Update.de_json(request.get_json(force=True), bot)
    setup().process_update(update)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setuptt ok"
    else:
        return "webhook setup failed"
