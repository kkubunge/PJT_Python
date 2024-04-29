from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os

token = "6763521890:AAHhSPmC402k91oDmbqRjt1Sg7yQaaASesk"
chat_id = "7134204973"

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")


async def crawl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #
    # code blocks for crawling
    #
    await context.bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def echo2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = ""
    message = update.message.text
    if message == "안녕":
        reply = "너도 안녕!"
    elif message == "바보":
        reply = "반사!"
    elif message == "날씨":
        reply = "좋음!"

    if (reply == ""):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

async def img(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open('8158731421.jpg', 'rb'))

# async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await os._exit(1) # 스크립트 강제 종료

application = ApplicationBuilder().token(token).build()


crawl_handler = CommandHandler('c', crawl)
application.add_handler(crawl_handler)

help_handler = CommandHandler('h', help)
application.add_handler(help_handler)

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo2)
application.add_handler(echo_handler)

img_handler = CommandHandler('img', img)
application.add_handler(img_handler)

application.run_polling()