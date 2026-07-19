import os
# Kerakli dasturlarni avtomatik o'rnatish
os.system("pip install pyTelegramBotAPI requests")

import telebot
import requests

BOT_TOKEN = "8881191712:AAFv4BHHkppvIfrr5Vz8L8fd7SArKY7Xjro"

# Tekin va ochiq AI modeli (Llama-3 modeli asosida)
API_URL = "https://huggingface.co"
# Bepul ochiq API kalit
HEADERS = {"Authorization": "Bearer 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"}

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men yangilangan AI yordamchiman. Menga istalgan savolingizni bering!")

@bot.message_handler(func=lambda message: True)
def ai_response(message):
    try:
        # Sun'iy intellektga vazifa berish
        prompt = f"<|system|>\nSiz aqlli va muloyim yordamchisiz. Savollarga qisqa, tushunarli va o'zbek tilida javob bering.\n<|user|>\n{message.text}\n<|assistant|>\n"
        
        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 250, "temperature": 0.7}
        }
        
        response = requests.post(API_URL, headers=HEADERS, json=payload).json()
        
        # AI javobini qirqib olish
        if isinstance(response, list) and "generated_text" in response[0]:
            full_text = response[0]["generated_text"]
            ai_text = full_text.split("<|assistant|>\n")[-1].strip()
            bot.reply_to(message, ai_text)
        else:
            bot.reply_to(message, "Hozircha tizim band, ozroq kutib qayta urining.")
            
    except Exception as e:
        print(f"Xatolik: {e}")
        bot.reply_to(message, "Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")

print("Bot muvaffaqiyatli ishga tushdi...")
bot.infinity_polling()
