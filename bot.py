import telebot
from telebot import types

# GANTI DENGAN TOKEN BARU ANDA
BOT_TOKEN = "MASUKKAN_TOKEN_BARU_ANDA_DI_SINI"
bot = telebot.TeleBot(BOT_TOKEN)

WEBSITE_URL = "https://cryptoretjeh.github.io/Cr/"

# ==========================================
# FUNGSI MENU UTAMA (DASHBOARD)
# ==========================================
def get_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Baris 1: Tombol Website dan Admin
    btn_web = types.InlineKeyboardButton("🌐 Buka Website", url=WEBSITE_URL)
    btn_admin = types.InlineKeyboardButton("💬 Hubungi Admin", url="https://wa.me/6281279499478")
    
    # Baris 2: Tombol Katalog dan Cara Order (Callback Data)
    btn_katalog = types.InlineKeyboardButton("📋 Katalog Harga", callback_data="menu_katalog")
    btn_cara = types.InlineKeyboardButton("📖 Cara Order", callback_data="menu_cara")
    
    # Baris 3: Tombol Bantuan
    btn_bantuan = types.InlineKeyboardButton("❓ Bantuan / FAQ", callback_data="menu_bantuan")

    markup.add(btn_web, btn_admin)
    markup.add(btn_katalog, btn_cara)
    markup.add(btn_bantuan)
    return markup

# ==========================================
# HANDLER PESAN /START
# ==========================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    teks = (f"Halo <b>{message.from_user.first_name}</b>! 👋\n\n"
            "Selamat datang di <b>Retjeh Store</b>.\n"
            "Kami menyediakan layanan Sosmed 100% Manual (Real Human).\n\n"
            "Silakan pilih menu di bawah ini:")
    
    bot.reply_to(message, teks, parse_mode='HTML', reply_markup=get_main_menu())

# ==========================================
# HANDLER TOMBOL (CALLBACK QUERY)
# ==========================================
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # Jika tombol Katalog diklik
    if call.data == "menu_katalog":
        teks = ("📋 <b>DAFTAR HARGA</b>\n\n"
                "✈️ Telegram: Follower Rp 500, Refferal Rp 1.500\n"
                "🎵 TikTok: Follower Rp 500, Like Rp 250\n"
                "📸 Instagram: Follower Rp 500, Like Rp 250\n"
                "▶️ YouTube: Subscriber Rp 500, Like Rp 250\n\n"
                "Untuk melihat katalog lengkap dan melakukan order, silakan klik tombol di bawah:")
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Lihat Harga Lengkap", url=WEBSITE_URL))
        markup.add(types.InlineKeyboardButton("⬅️ Kembali ke Menu", callback_data="menu_utama"))
        
        # Edit pesan lama menjadi pesan katalog
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text=teks, parse_mode='HTML', reply_markup=markup)
        
    # Jika tombol Cara Order diklik
    elif call.data == "menu_cara":
        teks = ("📖 <b>CARA ORDER</b>\n\n"
                "1️⃣ Buka website resmi kami\n"
                "2️⃣ Pilih layanan dan isi form order\n"
                "3️⃣ Lakukan pembayaran (BCA/DANA)\n"
                "4️⃣ Kirim bukti transfer ke Admin\n"
                "5️⃣ Admin akan memproses pesanan Anda secara manual.\n\n"
                "Klik tombol di bawah untuk mulai order:")
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🛒 Order Sekarang", url=WEBSITE_URL))
        markup.add(types.InlineKeyboardButton("⬅️ Kembali ke Menu", callback_data="menu_utama"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text=teks, parse_mode='HTML', reply_markup=markup)

    # Jika tombol Bantuan diklik
    elif call.data == "menu_bantuan":
        teks = ("❓ <b>BANTUAN / FAQ</b>\n\n"
                "🔒 <b>Aman?</b> Ya, 100% aman. Kami tidak meminta password akun Anda.\n\n"
                "⏳ <b>Berapa lama?</b> Proses manual bertahap, admin akan memberi estimasi.\n\n"
                "💳 <b>Pembayaran?</b> BCA dan DANA.\n\n"
                "Jika masih ada kendala, silakan hubungi admin:")
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💬 Chat Admin", url="https://wa.me/6281279499478"))
        markup.add(types.InlineKeyboardButton("⬅️ Kembali ke Menu", callback_data="menu_utama"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text=teks, parse_mode='HTML', reply_markup=markup)

    # Jika tombol Kembali ke Menu diklik
    elif call.data == "menu_utama":
        teks = (f"Halo <b>{call.from_user.first_name}</b>! 👋\n\n"
                "Silakan pilih menu di bawah ini:")
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text=teks, parse_mode='HTML', reply_markup=get_main_menu())

# ==========================================
# HANDLER PESAN TEKS BIASA (BUKAN COMMAND)
# ==========================================
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Ketik /start untuk membuka menu utama, atau klik link website berikut: " + WEBSITE_URL)

print("Bot berjalan...")
bot.infinity_polling()
