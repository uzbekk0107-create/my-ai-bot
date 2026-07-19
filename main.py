import os
# Kutubxonalarni majburiy o'rnatish buyrug'i
os.system("pip install pyTelegramBotAPI google-generativeai")

import telebot
from google import generativeai as genai

BOT_TOKEN = "8881191712:AAFv4BHHkppvIfrr5Vz8L8fd7SArKY7Xjro"
GEMINI_API_KEY = "AIzaSyDGtpmIbSif23EEcZTRHokJ1443P4aTvak"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sizning AI yordamchingizman. Menga istalgan savolingizni berishingiz mumkin.")

@bot.message_handler(func=lambda message: True)
def ai_response(message):
    try:
        prompt = f"Siz bot egasining o'rniga mijozlar bilan gaplashuvchi o'ta aqlli va muloyim yordamchisiz. Savollarga qisqa, tushunarli va o'zbek tilida javob bering. Mijoz xabari: {message.text}"
        response = model.generate_content(prompt)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Xatolik: {e}")
        bot.reply_to(message, "Kechirasiz, tizim yuklamasi yuqori. Birozdan so'ng qayta urining.")

print("Bot ishga tushdi...")
bot.infinity_polling()
