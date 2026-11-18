import os
import telebot
from telebot import types

# Ganti dengan Token Bot baru Anda (Jangan gunakan token yang sudah bocor)
BOT_TOKEN = "9122151061:AAEXxMjlrQspl7EOC815YL4iekiInPTVu9s"
bot = telebot.TeleBot(BOT_TOKEN)

# Link Website Anda
WEBSITE_URL = "https://cryptoretjeh.github.io/Cr/"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Membuat tombol inline
    markup = types.InlineKeyboardMarkup()
    btn_website = types.InlineKeyboardButton("🛒 Buka Website", url=WEBSITE_URL)
    btn_wa = types.InlineKeyboardButton("💬 Hubungi Admin", url="https://wa.me/6281279499478")
    markup.add(btn_website)
    markup.add(btn_wa)

    teks = (f"Halo <b>{message.from_user.first_name}</b>! 👋\n\n"
            "Selamat datang di <b>Retjeh Store</b>.\n"
            "Kami menyediakan layanan Sosmed 100% Manual (Real Human).\n\n"
            "Silakan klik tombol di bawah untuk melihat katalog harga dan melakukan order:")
    
    bot.reply_to(message, teks, parse_mode='HTML', reply_markup=markup)

@bot.message_handler(commands=['harga'])
def send_harga(message):
    teks = ("📋 <b>DAFTAR HARGA</b>\n\n"
            "✈️ Telegram: Follower Rp 500, Refferal Rp 1.500\n"
            "🎵 TikTok: Follower Rp 500, Like Rp 250\n"
            "📸 Instagram: Follower Rp 500, Like Rp 250\n"
            "▶️ YouTube: Subscriber Rp 500, Like Rp 250\n\n"
            "Untuk detail lengkap, silakan buka website:")
    
    markup = types.InlineKeyboardMarkup()
    btn_website = types.InlineKeyboardButton("Lihat Harga Lengkap", url=WEBSITE_URL)
    markup.add(btn_website)
    
    bot.reply_to(message, teks, parse_mode='HTML', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Membalas pesan apapun yang tidak dikenali
    bot.reply_to(message, "Ketik /start untuk membuka menu utama, atau klik link website berikut: " + WEBSITE_URL)

print("Bot berjalan...")
bot.infinity_polling()
